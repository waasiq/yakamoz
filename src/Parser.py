from helpers.ErrHandler import InvalidSyntax 

#* ParseResult contains the node and error and the Parse is actually wrapped around
#* the Parse Class for error checking
from helpers.ParseResult import ParseResult

from AST import *
from Tokens import *

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
       if not res.error and self.currTok.type != TOK_EOF:
            return res.failure(InvalidSyntax(
                self.currTok.pos_start, self.currTok.pos_end,
                'Expected an operator '
            ))
       return res

    #* Chained function working:
    #* Expression runs binaryOP which runs Term which runs binaryOP which runs factor.
    
    #* General function to reduce code repititive code
    def binaryOP(self, funcA, ops, funcB = None):        
        if funcB == None: funcB = funcA

        res = ParseResult()
        left  = res.register(funcA()) 
        if res.error: return res
             
        while self.currTok.type in ops:
            opToken = self.currTok
            res.register(self.advance())
            right = res.register(funcB())
            if res.error: return res
            left = BinOPNode(opToken, left, right)

        return res.success(left)

    def power(self):
            return self.binaryOP(self.atom, (TOK_POW), self.factor)

    def factor(self):
        res = ParseResult()
        token = self.currTok

        if token.type in (TOK_ADD, TOK_SUB):
            self.advance()
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOPNode(token, factor))
        
        
        return self.power()


    def atom(self):
        res = ParseResult()
        token = self.currTok

        if token.type in (TOK_INT, TOK_FLOAT):
            #* Idea is to return correct response here
            res.register(self.advance()) 
            return NumberNode(token)
        elif token.type == TOK_IDENTIFIER:
            res.register(self.advance())
            return VarAccessNode(token)
        elif token.type == TOK_LBRACKET:
            res.register(self.advance())
            expr = res.register(self.expression())
            if res.error: return res
            if self.currTok.type == TOK_RBRACKET: #* Right bracket found return expr
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
            'Expected int, float, +, - or ( '
        ))

    #* Term returns two number nodes as it calls factor function
    def term(self):
        return self.binaryOP(self.factor, (TOK_MUL, TOK_DIV))        

    #* Expression runs the code term and term runs the factor
    def expression(self): 
        res = ParseResult()

        if self.currTok.matches(TOK_KEYWORD, 'oyleki'):
            res.register(self.advance())
            
            if self.currTok.type != TOK_IDENTIFIER:
                return res.failure(InvalidSyntax(
                    self.currTok.pos_start, self.currTok.pos_end,
                    'Expected an identifier'   
                ))
            
            varName = self.currTok
            res.register(self.advance())

            if self.currTok.type != TOK_EQUAL:
                return res.failure(InvalidSyntax(
                    self.currTok.pos_start, self.currTok.pos_end,
                    'Expected ='   
                ))
            
            res.register(self.advance())
            #* expr is the value returned after parsing all the expressions after equal
            value = res.register(self.expression()) 
            
            if res.error: return res
            
            return res.success(VarAssignNode(varName, value))
        else:
            return self.binaryOP(self.term, (TOK_ADD, TOK_SUB))  