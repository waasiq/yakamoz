import helpers.ErrHandler as err
import helpers.Position as pos
import Tokens as tk

from Interpreter import *
from Parser import Parser
from helpers.Context import Context

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

        while self.currChar != None and self.currChar in tk.DIGITS + '.':
            if self.currChar == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.currChar
            self.advance()

        if dot_count == 0:
            return tk.Token(tk.TOK_INT, int(num_str), pos_start, self.pos)
        else:
            return tk.Token(tk.TOK_FLOAT, float(num_str),pos_start, self.pos)

    def lexeme(self):
        tokens = []
       
        while self.currChar != None:   
            if self.currChar in ' \t':
                self.advance()
            elif self.currChar in tk.DIGITS:
                tokens.append(self.tokenize_num())
            elif tk.OP_TOK_TAG.get(self.currChar) != None:
                tokens.append(tk.Token(tk.OP_TOK_TAG.get(self.currChar), pos_start=self.pos))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.currChar
                self.advance()
                return [], err.IllegalChar(pos_start, self.pos, "'" + char + "'")

        tokens.append(tk.Token(tk.TOK_EOF, pos_start = self.pos))
        return tokens, None

#! Run
def runLexer(fn, text):
    lex = Lexer(fn , text)
    tokens, error = lex.lexeme()
    
    if error: return None, error

    #* Parse returns us the AST 
    #* ParseResult contains the node and error and the Parse is actually wrapped around
    #* the Parse Class
    psr = Parser(tokens)
    ast = psr.parse() 
    if ast.error: return None, ast.error

    intrpt = Interpreter()
    context = Context('<program>')
    result = intrpt.visit(ast.node, context)

    return  result.value, result.error