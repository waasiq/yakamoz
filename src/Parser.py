from errors.ErrHandler import InvalidSyntaxError 

#* ParseResult contains the node and error and the Parse is actually wrapped around
#* the Parse Class for error checking
from wrappers.ParseResult import ParseResult

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
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                'Expected an operator '
            ))
       return res

    #? Chained function working:
    #? Expression runs binaryOP which runs Term which runs binaryOP which runs factor.
    
    #* General function to reduce code repititive code
    def binaryOP(self, funcA, ops, funcB = None):        
        if funcB == None: funcB = funcA

        res = ParseResult()
        left  = res.register(funcA()) 
        if res.error: return res
             
        while self.currTok.type in ops or (self.currTok.value , self.currTok.value) in ops:
            opToken = self.currTok
            res.register_advancement()
            self.advance()
            right = res.register(funcB())
            if res.error: return res
            left = BinOPNode(opToken, left, right)

        return res.success(left)
    
    def comp_expr(self):
        res = ParseResult()

        if self.currTok.matches(TOK_KEYWORD, 'yoket'):
            opTOK = self.currTok
            res.register_advancement()
            self.advance()
            node = res.register(self.comp_expr())
            if res.error: return res 
            return res.success(UnaryOPNode(opTOK, node))

        node = res.register(self.binaryOP(self.arith_expr, (TOK_DEQUAL, TOK_KEYWORD, TOK_NTEQUAL , TOK_GT, TOK_GTE, TOK_LTE, TOK_LT)))

        if res.error: 
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                'Expected int, float, identifier,+, - ,( , YOKET '
            ))

        return res.success(node)

    def arith_expr(self):
        return self.binaryOP(self.term, (TOK_ADD, TOK_SUB))

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
            res.register_advancement()
            self.advance() 
            return NumberNode(token)
        elif token.type == TOK_IDENTIFIER:
            res.register_advancement()
            self.advance()
            return VarAccessNode(token)
        elif token.type == TOK_LBRACKET:
            res.register_advancement()
            self.advance()
            expr = res.register(self.expression())
            if res.error: return res
            if self.currTok.type == TOK_RBRACKET: #* Right bracket found return expr
                res.register_advancement()
                self.advance()
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(
                    self.currTok.pos_start, self.currTok.pos_end,
                    "Expected ')'"
                ))
       
        return res.failure(InvalidSyntaxError(
            token.pos_start,
            token.pos_end ,
            'Expected int, float, identifier,+, - or ( '
        ))

    #* Term returns two number nodes as it calls factor function
    def term(self):
        return self.binaryOP(self.factor, (TOK_MUL, TOK_DIV))  
   
    def power(self):
        return self.binaryOP(self.atom, (TOK_POW, ), self.factor)

    #* Expression runs the code term and term runs the factor
    def expression(self): 
        res = ParseResult()

        if self.currTok.matches(TOK_KEYWORD, 'oyleki'):
            res.register_advancement()
            self.advance()
            
            if self.currTok.type != TOK_IDENTIFIER:
                return res.failure(InvalidSyntaxError(
                    self.currTok.pos_start, self.currTok.pos_end,
                    'Expected an identifier'   
                ))
            
            varName = self.currTok
            res.register_advancement()
            self.advance()

            if self.currTok.type != TOK_EQUAL:
                return res.failure(InvalidSyntaxError(
                    self.currTok.pos_start, self.currTok.pos_end,
                    'Expected ='   
                ))
            
            res.register_advancement()
            self.advance()
            #* value is the expression and its subnodes nodes parsed into an AST         
            value = res.register(self.expression())
            
            if res.error: return res
            return res.success(VarAssignNode(varName, value))
        
        
        node = res.register(self.binaryOP(self.comp_expr, ((TOK_KEYWORD, 've'), (TOK_KEYWORD, 'veya'))))

        if res.error:
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                "Expected 'oyleki', int, float, identifier, '+', '-' or '('"
            ))

        return res.success(node)