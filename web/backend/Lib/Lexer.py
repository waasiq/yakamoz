
#* Helper function import
import Helpers.Position as pos
from Helpers.Context    import Context

#* Main function import
from Lib.Parser import Parser

from Lib.Tokens                 import *
from Lib.Interpreter            import *
from Objects.Numbers        import *
from Objects.SymbolTable    import *
from Errors.ErrHandler      import *
from Funcs.BuiltInFunc      import *

#! Lexer Main Class
class Lexer:
    def __init__(self, fn, text):
        self.fn = fn 
        self.text = text 
        self.pos = pos.Position(-1, 0,-1, fn , text)
        self.currChar = None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.currChar)
        if self.pos.indx < len(self.text):
            self.currChar = self.text[self.pos.indx]
        else:
            self.currChar = None

    #* Tokenizes the amount of digits sent here to float or int
    def tokenize_num(self):
        num_str = ''
        dot_count = 0
        pos_start = self.pos.copy()

        while self.currChar != None and self.currChar in DIGITS + '.':
            if self.currChar == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.currChar
            self.advance()

        if dot_count == 0:
            return Token(TOK_INT, int(num_str), pos_start, self.pos)
        else:
            return Token(TOK_FLOAT, float(num_str),pos_start, self.pos)

    #* Tokenize the letters 
    def tokenize_letters(self):
        id_str = ''
        pos_start = self.pos.copy()

        while self.currChar is not None and self.currChar in LETTERS_DIGITS + '_':
            id_str += self.currChar
            self.advance()

        tok_type = TOK_KEYWORD if id_str in KEYWORDS else TOK_IDENTIFIER
        return Token(tok_type, id_str , pos_start, self.pos)
    
    def tokenize_notEQ(self):
        pos_copy = self.pos.copy()
        self.advance()

        if self.currChar == '=':
            self.advance()
            return Token(TOK_NTEQUAL, pos_start = pos_copy, pos_end= self.pos), None

        self.advance()
        return None, ExpectedCharError(pos_copy, self.pos, "'=' (after !)") 
    
    def tokenize_equal(self):
        pos_copy = self.pos.copy()
        self.advance()
        
        if self.currChar == '=':
            self.advance()
            return Token(TOK_DEQUAL, pos_start = pos_copy, pos_end= self.pos)
        
        return Token(TOK_EQUAL, pos_start = pos_copy, pos_end = self.pos) 


    def tokenize_greater(self):
        pos_copy = self.pos.copy()
        self.advance()

        if self.currChar == '=':
            self.advance()
            return Token(TOK_GTE, pos_start = pos_copy, pos_end = self.pos) 
        
        return Token(TOK_GT, pos_start = pos_copy, pos_end = self.pos) 

    def tokenize_lessor(self):
        pos_copy = self.pos.copy()
        self.advance()

        if self.currChar == '=':
            self.advance()
            return Token(TOK_LTE, pos_start = pos_copy, pos_end = self.pos) 
        
        return Token(TOK_LT, pos_start = pos_copy, pos_end = self.pos) 

    def tokenize_minus_or_arrow(self):
        pos_copy = self.pos.copy()
        self.advance()

        if self.currChar == '>':
            self.advance()
            return Token(TOK_ARROW, pos_start = pos_copy, pos_end = self.pos)
        
        return Token(TOK_SUB, pos_start = pos_copy, pos_end = self.pos)

    def tokenize_string(self):
        pos_copy = self.pos.copy()
        str = ''
        self.advance()

        while self.currChar != None and self.currChar != "'":
            str += self.currChar
            self.advance()

        self.advance()
        return Token(TOK_STRING, str, pos_copy, self.pos) 

    def skip_comment(self):
        self.advance()

        while self.currChar != '\n':
            self.advance()
        
        self.advance()

    def lexeme(self):
        tokens = []
       
        while self.currChar != None:   
            if self.currChar in ' \t':
                self.advance()
            #elif self.currChar == '#':
            #    self.skip_comment()
            elif self.currChar in ';\n':
                tokens.append(Token(TOK_NEWLINE, pos_start=self.pos))
                self.advance()
            elif self.currChar in DIGITS:
                tokens.append(self.tokenize_num())
            elif self.currChar in LETTERS:
                tokens.append(self.tokenize_letters())
            elif self.currChar == '>':
                tokens.append(self.tokenize_greater())
            elif self.currChar == '<':
                tokens.append(self.tokenize_lessor())
            elif self.currChar == '!':
                token, error = self.tokenize_notEQ()
                if error: return [], error
                tokens.append(token)
            elif self.currChar == '=':
                tokens.append(self.tokenize_equal())
            elif self.currChar == ',':
                tokens.append(Token(TOK_COMMA, pos_start=self.pos))
                self.advance()
            elif self.currChar == '-':
                tokens.append(self.tokenize_minus_or_arrow())
            elif self.currChar == "'":
                tokens.append(self.tokenize_string())
            elif OP_TOK_TAG.get(self.currChar) != None:
                tokens.append(Token(OP_TOK_TAG.get(self.currChar), pos_start=self.pos))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.currChar
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        tokens.append(Token(TOK_EOF, pos_start = self.pos))
        return tokens, None

#! Run

global_symbol_table = SymbolTable()
global_symbol_table.set("NULL", Number.null)
global_symbol_table.set("Yanlis", Number.false)
global_symbol_table.set("Dogru", Number.true)

global_symbol_table.set("yazdir", BuiltInFunction.print)
global_symbol_table.set("input", BuiltInFunction.input)
global_symbol_table.set("input_int", BuiltInFunction.input_int)
global_symbol_table.set("temizle", BuiltInFunction.clear)

global_symbol_table.set("isNumber", BuiltInFunction.is_number)
global_symbol_table.set("isString", BuiltInFunction.is_string)
global_symbol_table.set("isList",BuiltInFunction.is_list)
global_symbol_table.set("isFunction", BuiltInFunction.is_function)

global_symbol_table.set("ekle",  BuiltInFunction.append)
global_symbol_table.set("cikar", BuiltInFunction.pop)

#global_symbol_table.set('getElement', BuiltInFunction.getElement)
global_symbol_table.set('uzunluk', BuiltInFunction.len)
global_symbol_table.set('run', BuiltInFunction.run)


def runLexer(fn, text):   
    if text == 'cls': 
        print("\033[H\033[J", end="")
        return None,None

    lex = Lexer(fn , text)
    tokens, error = lex.lexeme()  #* Returns the tokens  
    if error: return None, error   

    #? Sole purpose of the Parser class is to make a Abstract Syntax Tree which will be 
    #? interpreted by our interpreter
    psr = Parser(tokens)  
    ast = psr.parse() #* Parser.parse returns us the AST 
    if ast.error: return None, ast.error

   
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    intrpt = Interpreter()    
    result = intrpt.visit(ast.node, context) #* ast.node -> Head node

    return  result.value, result.error