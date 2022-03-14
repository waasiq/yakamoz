from lib2to3.pgen2 import token
import helpers.ErrHandler as err
import helpers.Position as pos

from Parser import Parser

#! Tokens and Tokenizer

DIGITS = '0123456789'

TOK_INT     = 'INT'
TOK_FLOAT   = 'FLOAT'

OP_TOK_TAG = {
    '+' : 'ADD',
    '-' : 'SUB',
    '/' : 'DIV',
    '*' : 'MUL',
    '{' : 'LBRACKET',
    '}' : 'RBRACKET',
    '(' : 'LBRACKET',
    ')' : 'RBRACKET'   
}

class Token:
    def __init__(self, type, value = None):
        self.type = type
        self.value = value
    
    def __repr__(self):
        if self.value: return f'{self.value} : {self.type}'
        return f'{self.type}'


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

        while self.currChar != None and self.currChar in DIGITS + '.':
            if self.currChar == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.currChar
            self.advance()

        if dot_count == 0:
            return Token(TOK_INT, int(num_str))
        else:
            return Token(TOK_FLOAT, float(num_str))

    def lexeme(self):
        tokens = []
       
        while self.currChar != None:   
            if self.currChar in ' \t':
                self.advance()
            elif self.currChar in DIGITS:
                tokens.append(self.tokenize_num())
            elif OP_TOK_TAG.get(self.currChar) != None:
                tokens.append(Token(OP_TOK_TAG.get(self.currChar), None)) #! Change the val later
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.currChar
                self.advance()
                return [], err.IllegalChar(pos_start, self.pos, "'" + char + "'")

        return tokens, None

#! Run
def runLexer(fn, text):
    lex = Lexer(fn , text)
    tokens, error = lex.lexeme()
    
    if error: return None, error
    psr = Parser(tokens)
    psr.factor()

    return  tokens, error