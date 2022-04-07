import string

#! Tokens and Tokenizers

DIGITS  = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

#! TOKEN
TOK_INT       = 'INT'
TOK_FLOAT     = 'FLOAT'
TOK_STRING    = 'STRING'

TOK_MUL       = 'MUL'
TOK_DIV       = 'DIV'
TOK_ADD       = 'ADD'
TOK_SUB       = 'SUB'
TOK_POW       = 'POW'
TOK_EOF       = 'EOF'
TOK_REMAINDER = 'REMAINDER'

TOK_LBRACKET = 'LBRACKET'
TOK_RBRACKET = 'RBRACKET'
TOK_LSQUARE  = 'LSQUARE'
TOK_RSQUARE  = 'RSQUARE'

TOK_IDENTIFIER = 'IDENTIFIER'
TOK_KEYWORD    = 'KEYWORD'
TOK_EQUAL      = 'EQUALS'

TOK_DEQUAL      = 'DOUBLEQUALS'
TOK_NTEQUAL     = 'NOTEQUALS'
TOK_GT          = 'GREATERTHAN'
TOK_GTE         = 'GREATERTHANEQTO'
TOK_LT          = 'LESSTHAN'
TOK_LTE         = 'LESSTHANEQTO'

TOK_ARROW       = 'ARROW'
TOK_COMMA       = 'COMMA' 

TOK_NEWLINE     = 'NEWLINE'

TOK_BREAK       = 'BREAK'
TOK_RETURN      = 'RETURN'
TOK_CONTINUE    = 'CONTINUE'

TOK_END         = 'END'

#! Dict for the Operator
OP_TOK_TAG = {
    '+'     : 'ADD',
    '/'     : 'DIV',
    '*'     : 'MUL',
    '{'     : 'LBRACKET',
    '}'     : 'RBRACKET',
    '('     : 'LBRACKET',
    ')'     : 'RBRACKET',
    '['     : 'LSQUARE',
    ']'     : 'RSQUARE',
    '^'     : 'POW',
    '%'     : 'REMAINDER'
}

#! A list of the keywords for yakamoz
KEYWORDS = [
    'oyleki',
    'yoket',
    've',
    'veya',

    'if',
    'then',
    'elseif',
    'else',

    'for',
    'to',
    'step',
    'while',
    'func', 
    'return',
    'continue',
    'break',
    'end'
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

    def matches(self, type_, value):
        return self.type == type_ and self.value == value

    def __repr__(self):
        if self.value: return f'{self.value} : {self.type}'
        return f'{self.type}'