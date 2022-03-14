#! Tokens and Tokenizer

DIGITS = '0123456789'

TOK_INT     = 'INT'
TOK_FLOAT   = 'FLOAT'
TOK_MUL = 'MUL'
TOK_DIV = 'DIV'
TOK_ADD = 'ADD'
TOK_SUB = 'SUB'
TOK_EOF = 'EOF'

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