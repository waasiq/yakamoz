import string

#! Tokens and Tokenizers

DIGITS  = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

#! TOKEN
TOK_INT      = 'INT'
TOK_FLOAT    = 'FLOAT'
TOK_MUL      = 'MUL'
TOK_DIV      = 'DIV'
TOK_ADD      = 'ADD'
TOK_SUB      = 'SUB'
TOK_POW      = 'POW'
TOK_EOF      = 'EOF'
TOK_LBRACKET = 'LBRACKET'
TOK_RBRACKET = 'RBRACKET'

TOK_IDENTIFIER = 'IDENTIFIER'
TOK_KEYWORD    = 'KEYWORD'
TOK_EQUAL      = 'EQUALS'


#! Dict for the Operator
OP_TOK_TAG = {
    '+'     : 'ADD',
    '-'     : 'SUB',
    '/'     : 'DIV',
    '*'     : 'MUL',
    '='     : 'EQUALS',
    'oyleki': 'KEYWORD',
    '{'     : 'LBRACKET',
    '}'     : 'RBRACKET',
    '('     : 'LBRACKET',
    ')'     : 'RBRACKET',
    '^'     : 'POW' 
}

#! A list of the keywords for yakamoz
KEYWORDS = [
    'oyleki'
]

class Token:
    def __init__(self, type_ , value=None , pos_start=None , pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end        

    def __repr__(self):
        if self.value: return f'{self.value} : {self.type}'
        return f'{self.type}'