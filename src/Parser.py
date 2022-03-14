from AST import NumberNode

TOK_INT     = 'INT'
TOK_FLOAT   = 'FLOAT'

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_indx = -1 
        self.advance()

    def __repr__(self):
        pass

    def advance(self):
        self.tok_indx += 1 
        if self.tok_indx < len(self.tokens):
            self.currTok = self.tokens[self.tok_indx]
        return self.currTok
    
    def expression(self):
        pass
    
    def term(self):
        left = self.factor()

        if (left != None):
            pass
            # if ()
        
    
    def factor(self):
        token = self.currTok
        if token.type in (TOK_INT, TOK_FLOAT):
            self.advance() 
            return NumberNode(token)
        return None
