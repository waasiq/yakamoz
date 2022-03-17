from helpers.ErrHandler import InvalidSyntax 
from AST import NumberNode,BinOPNode, UnaryOPNode

import Tokens as tk

#! Class for parsing the result w.r.t Error Handling
class ParseResult:
	def __init__(self):
		self.error = None
		self.node = None

	def register(self, res):
		if isinstance(res, ParseResult):
			if res.error: self.error = res.error
			return res.node
		return res

	def success(self, node):
		self.node = node
		return self

	def failure(self, error):
		self.error = error
		return self

#! Parse result
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_indx = -1
        self.advance()

    def advance(self):
        self.tok_indx += 1 
        if self.tok_indx < len(self.tokens):
            self.currTok = self.tokens[self.tok_indx]
        return self.currTok

    def parse(self):
       res = self.expression()
       if not res.error and self.currTok.type != tk.TOK_EOF:
            return res.failure(InvalidSyntax(
                self.currTok.pos_start, self.currTok.pos_end,
                'Expected an operator '
            ))
       return res

    #* Chained function working:
    #* Expression runs opCode which runs Term which runs opCode which runs factor.
    
    #* General function to reduce code repititive code
    def opCode(self, func, ops):        
        res = ParseResult()
        left  = res.register(func()) 
        if res.error: return res
             
        while self.currTok.type in ops:
            opToken = self.currTok
            res.register(self.advance())
            right = res.register(func())
            if res.error: return res
            left = BinOPNode(opToken, left, right)

        return res.success(left)

    def factor(self):
        res = ParseResult()
        token = self.currTok

        if token.type in (tk.TOK_ADD, tk.TOK_SUB):
            self.advance()
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOPNode(token, factor))
        elif token.type in (tk.TOK_INT, tk.TOK_FLOAT):
            #* Idea is to return correct response here
            res.register(self.advance()) 
            return NumberNode(token)
        elif token.type == tk.TOK_LBRACKET:
            res.register(self.advance())
            expr = res.register(self.expression())
            if res.error: return res
            if self.currTok.type == tk.TOK_RBRACKET: #* Right bracket found return expr
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failure(InvalidSyntax(
                    self.currTok.pos_start, self.currTok.pos_end,
                    "Expected ')'"
                ))

        
        return res.failure(InvalidSyntax(
            token.pos_start,
            token.pos_end ,
            'Expected int or float '
        ))
        
    #* Term returns two number nodes as it calls factor function
    def term(self):
        return self.opCode(self.factor, (tk.TOK_MUL, tk.TOK_DIV))        

    #* Expression runs the code term and term runs the factor
    def expression(self):        
        return self.opCode(self.term, (tk.TOK_ADD, tk.TOK_SUB))  