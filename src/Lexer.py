
#* Helper function import
import helpers.Position as pos
from helpers.Context import Context

#* Main function import
from Parser import Parser

from Tokens import *
from Interpreter import *
from objects.SymbolTable import *
from errors.ErrHandler import *

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


    def lexeme(self):
        tokens = []
       
        while self.currChar != None:   
            if self.currChar in ' \t':
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
global_symbol_table.set("NULL", Number(0))
global_symbol_table.set("Dogru", Number(1))
global_symbol_table.set("Yanlis", Number(0))

def runLexer(fn, text):
    #* cleans the console
    if text == 'cls': 
        print("\033[H\033[J", end="")
        return None,None
    
    lex = Lexer(fn , text)
    tokens, error = lex.lexeme()  #* Returns the tokens  
    if error: return None, error   

    #return tokens, None

    #? Sole purpose of the Parser class is to make a Abstract Syntax Tree which will be 
    #? interpreted by our interpreter
    psr = Parser(tokens)  
    ast = psr.parse() #* Parser.parse returns us the AST 
    if ast.error: return None, ast.error


    #return ast.node, None
    
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    intrpt = Interpreter()    
    result = intrpt.visit(ast.node, context) #* ast.node -> Head node

    return  result.value, result.error