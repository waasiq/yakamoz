from Errors.ErrHandler import InvalidSyntaxError 

#* ParseResult contains the node and error and the Parse is actually wrapped around
#* the Parse Class for error checking
from Wrappers.ParseResult import ParseResult

from Lib.AST import *
from Lib.Tokens import *

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

    def reverse(self, amount=1):
        self.tok_indx -= amount
        if self.tok_indx < len(self.tokens):
            self.currTok = self.tokens[self.tok_indx]
        return self.currTok
        
    def parse(self):
       res = self.statements()
       if not res.error and self.currTok.type != TOK_EOF:
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                'Expected an operator '
            ))
       return res

    def statements(self):
        res = ParseResult()
        statements = []
        pos_start = self.currTok.pos_start.copy()

        while self.currTok.type == TOK_NEWLINE:
            res.register_advancement()
            self.advance()

        statement = res.register(self.statement())
        if res.error: return res
        statements.append(statement)

        more_statements = True

        while True:
            newline_count = 0
            while self.currTok.type == TOK_NEWLINE:
                res.register_advancement()
                self.advance()
                newline_count += 1
            if newline_count == 0:
                more_statements = False
            
            if not more_statements: break
            statement = res.try_register(self.statement())
            if not statement:
                self.reverse(res.to_reverse_count)
                more_statements = False
                continue
            statements.append(statement)

        return res.success(listNode(
            statements,
            pos_start,
            self.currTok.pos_end.copy()
        ))

    def statement(self):
        res = ParseResult()
        pos_start = self.currTok.pos_start.copy()

        if self.currTok.matches(TOK_KEYWORD, 'return'):
            res.register_advancement()
            self.advance()

            expr = res.try_register(self.expr())
            if not expr:  self.reverse(res.to_reverse_count)
            return res.success(ReturnNode(expr, pos_start, self.currTok.pos_start.copy()))

        if self.currTok.matches(TOK_KEYWORD, 'continue'):
            res.register_advancement()
            self.advance()
            return res.success(ContinueNode(pos_start,self.currTok.pos_start.copy()))
        
        if self.currTok.matches(TOK_KEYWORD, 'break'):
            res.register_advancement()
            self.advance()
            return res.success(BreakNode(pos_start, self.currTok.pos_start.copy()))
        
        expr = res.register(self.expr())
        if res.error: 
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                "Expected 'oyleki', 'if', 'for', 'while', 'fun', int, float, identifier, '+', '-', '(', '[' or 'not'"
            ))

        return res.success(expr)
        
    #? Chained function working:
    #? Expression runs binaryOP which runs Term which runs binaryOP which runs factor.
    
    #* General function to reduce code repititive code
    def binaryOP(self, funcA, ops, funcB = None):        
        if funcB == None: funcB = funcA

        res = ParseResult()
        left  = res.register(funcA()) 
        if res.error: return res

        while self.currTok.type in ops or (self.currTok.type , self.currTok.value) in ops:
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

        node = res.register(self.binaryOP(self.arith_expr, (TOK_DEQUAL,TOK_REMAINDER, TOK_NTEQUAL , TOK_GT, TOK_GTE, TOK_LTE, TOK_LT)))

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

    def if_expr(self):
        res = ParseResult()
        all_cases = res.register(self.if_expr_cases('if'))
        if res.error: return res
        cases, else_case = all_cases
        return res.success(ifNode(cases, else_case))
    
    
    def if_expr_b(self):
        return self.if_expr_cases('elseif')
    
    def if_expr_c(self):
        res = ParseResult()
        else_case = None
        
        if self.currTok.matches(TOK_KEYWORD, 'else'):
            res.register_advancement()
            self.advance()
            
            if self.currTok.type == TOK_NEWLINE:
            
                res.register_advancement()
                self.advance()

                statements = res.register(self.statements())
                if res.error: return res
                else_case = (statements, True)

               
                if self.currTok.matches(TOK_KEYWORD, 'end'):
                    res.register_advancement()
                    self.advance()
                else:
                    return res.failure(InvalidSyntaxError(
                        self.currTok.pos_start, self.currTok.pos_end,
                        "Expected 'end'"
                    ))
            else:
                expr = res.register(self.statement())
                if res.error: return res
                else_case = (expr, False)

        return res.success(else_case)

    def if_expr_b_or_c(self):
        res = ParseResult()
        cases, else_case = [], None

        if self.currTok.matches(TOK_KEYWORD, 'elseif'):
            all_cases = res.register(self.if_expr_b())
            if res.error: return res
            cases, else_case = all_cases
        else:
            else_case = res.register(self.if_expr_c())
            if res.error: return res
        
        return res.success((cases, else_case))
    
    def if_expr_cases(self, case_keyword):
        res = ParseResult()
        cases = []
        else_case = None

        if not self.currTok.matches(TOK_KEYWORD, case_keyword):
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                f"Expected '{case_keyword}'"
            ))

        res.register_advancement()
        self.advance()

        condition = res.register(self.expr())
        if res.error: return res

        if not self.currTok.matches(TOK_KEYWORD, 'then'):
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                f"Expected 'then'"
            ))

        res.register_advancement()
        self.advance()

        if self.currTok.type == TOK_NEWLINE:
            res.register_advancement()
            self.advance()

            statements = res.register(self.statements())
            if res.error: return res
            cases.append((condition, statements, True))

            if self.currTok.matches(TOK_KEYWORD, 'end'):
                res.register_advancement()
                self.advance()
            else:
                all_cases = res.register(self.if_expr_b_or_c())
                if res.error: return res
                new_cases, else_case = all_cases
                cases.extend(new_cases)
        else:
            expr = res.register(self.statement())
            if res.error: return res
            cases.append((condition, expr, False))

            all_cases = res.register(self.if_expr_b_or_c())
            if res.error: return res
            new_cases, else_case = all_cases
            cases.extend(new_cases)
        
        return res.success((cases, else_case))




    #! While expression
    def while_expr(self):
        res = ParseResult()
        
        if self.currTok.matches(TOK_KEYWORD, 'while') == False:
            return res.failure(
                self.currTok.pos_start, self.currTok.pos_end,
                "Expected 'while' keyword"
            )
        
        res.register_advancement()
        self.advance()

        condition = res.register(self.expr())
        if res.error: return res

        if self.currTok.matches(TOK_KEYWORD, 'then') == False:
            return res.failure(
                self.currTok.pos_start, self.currTok.pos_end,
                "Expected 'then' keyword"
            )
        
        res.register_advancement()
        self.advance()

        if self.currTok.type == TOK_NEWLINE:
            res.register_advancement()
            self.advance()

            body = res.register(self.statements())
            if res.error: return res

            if not self.currTok.matches(TOK_KEYWORD, 'end'):
                return res.failure(InvalidSyntaxError(
                     self.currTok.pos_start, self.currTok.pos_end,
                    f"Expected 'end'"
                ))

            res.register_advancement()
            self.advance()

            return res.success(whileNode(condition, body, True))
            
        body = res.register(self.statement())
        if res.error: return res

        return res.success(whileNode(condition, body, False))
        
    #! For expression
    def for_expr(self):
        res = ParseResult()

        if self.currTok.matches(TOK_KEYWORD, 'for') == False:
            return res.failure(InvalidSyntaxError(
                self.pos_start, self.pos_end,
                "Expected 'for' keyword"
            ))

        res.register_advancement()
        self.advance()

        if self.currTok.type != TOK_IDENTIFIER: 
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                'Expected an identifier'
            ))

        var_name = self.currTok

        res.register_advancement()
        self.advance()

        if self.currTok.type != TOK_EQUAL:
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                "Expected '='"
            ))

        res.register_advancement()
        self.advance()

        first_expr = res.register(self.expr())
        if res.error: return res

        if self.currTok.matches(TOK_KEYWORD, 'to') == False:
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                "Expected 'to' keyword"
            ))

        res.register_advancement()
        self.advance()
        
        second_expr = res.register(self.expr())
        if res.error: return res


        if self.currTok.matches(TOK_KEYWORD, 'step'):
            res.register_advancement()
            self.advance()

            step_value = res.register(self.expr())
            if res.error: return res
        else:
            step_value = None

        if self.currTok.matches(TOK_KEYWORD, 'then') == False:
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                "Expected 'then' keyword"
            ))

        res.register_advancement()
        self.advance()

        if self.currTok.type == TOK_NEWLINE:
            res.register_advancement()
            self.advance()

        body = res.register(self.statements())
        if res.error: return res

        if not self.currTok.matches(TOK_KEYWORD, 'end'):
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                f"Expected 'end'"
            ))

        res.register_advancement()
        self.advance()

        return res.success(forNode(var_name, first_expr, second_expr, step_value, body, True))

    #!Function define parser
    def func_def(self):
        res = ParseResult()

        if self.currTok.matches(TOK_KEYWORD, 'func') == False:
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                "Expected 'func' keyword"
            ))
        
        res.register_advancement()
        self.advance()

        
        if self.currTok.type == TOK_IDENTIFIER: 
           var_name_token = self.currTok

           res.register_advancement()
           self.advance()
           if self.currTok.type != TOK_LBRACKET:
               return res.failure(InvalidSyntaxError(
                   self.currTok.pos_start, self.currTok.pos_end, 
                   'Expected Left Bracket'
               ))
        else:
            var_name_token = None

            res.register_advancement()
            self.advance()
            if self.currTok.type != TOK_LBRACKET:
               return res.failure(InvalidSyntaxError(
                   self.currTok.pos_start, self.currTok.pos_end, 
                   'Expected ('
               ))

        res.register_advancement()
        self.advance()

        arg_name_tokens = []

        if self.currTok.type == TOK_IDENTIFIER:
            arg_name_tokens.append(self.currTok)

            res.register_advancement()
            self.advance()

            while self.currTok.type == TOK_COMMA:
                res.register_advancement()
                self.advance()

                if self.currTok.type != TOK_IDENTIFIER:
                    return res.failure(InvalidSyntaxError(
                        self.currTok.pos_start, self.currTok.pos_end,
                        'Expected an identifier'
                    ))

                arg_name_tokens.append(self.currTok)
                res.register_advancement()
                self.advance()

            if self.currTok.type != TOK_RBRACKET:
                return res.failure(InvalidSyntaxError(
                    self.currTok.pos_start, self.currTok.pos_end,
                    'Expected ) identifier'
                ))
        else:
            if self.currTok.type != TOK_RBRACKET:
                return res.failure(InvalidSyntaxError(
                    self.currTok.pos_start, self.currTok.pos_end,
                    'Expected ) identifier'
                ))
    
        res.register_advancement()
        self.advance()

        if self.currTok.type == TOK_ARROW:
            res.register_advancement()
            self.advance()

            body = res.register(self.expr())
            if res.error: return res

            return res.success(funcDefNode(
                var_name_token,
                arg_name_tokens,
                body,
                True
            ))


        if self.currTok.type != TOK_NEWLINE:
            return res.failure(InvalidSyntaxError(
            self.currTok.pos_start, self.currTok.pos_end,
            f"Expected '->' or NEWLINE"
        ))
        
        res.register_advancement()
        self.advance()
        
        body = res.register(self.statements())
        if res.error: return res

        if not self.currTok.matches(TOK_KEYWORD, 'end'):
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                f"Expected 'end'"
        ))

        res.register_advancement()
        self.advance()
        
        return res.success(funcDefNode(
            var_name_token,
            arg_name_tokens,
            body,
            False
        ))

    def list_expr(self):
        res = ParseResult()
        elements = []
        pos_start = self.currTok.pos_start.copy()

        if self.currTok.type != TOK_LSQUARE:
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                "Expected '['"
            ))

        res.register_advancement()
        self.advance()

        if self.currTok.type == TOK_RSQUARE:
            res.register_advancement()
            self.advance()
        else:
            elements.append(res.register(self.expr()))
            if res.error: return res

            while self.currTok.type == TOK_COMMA:
                res.register_advancement()
                self.advance()

                elements.append(res.register(self.expr()))
                if res.error: return res

            if self.currTok.type != TOK_RSQUARE:
                return res.failure(InvalidSyntaxError(
                    self.currTok.pos_start, self.currTok.pos_end,
                    "Expected ',' or ']'"
                ))
        
        res.register_advancement()
        self.advance()

        return res.success(listNode(elements, pos_start, self.currTok.pos_end))


    def atom(self):
        res = ParseResult()
        token = self.currTok

        if token.type in (TOK_INT, TOK_FLOAT):
            #* Idea is to return correct response here
            res.register_advancement()
            self.advance() 
            return res.success(NumberNode(token))
        elif token.type == TOK_STRING:
            res.register_advancement()
            self.advance()
            return res.success(StringNode(token))
        elif token.type == TOK_IDENTIFIER:
            res.register_advancement()
            self.advance()
            return res.success(VarAccessNode(token))
        elif token.type == TOK_LBRACKET:
            res.register_advancement()
            self.advance()
            expr = res.register(self.expr())
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
        elif token.type == TOK_LSQUARE:
            list_expr = res.register(self.list_expr())
            if res.error: return res
            return res.success(list_expr)
        elif token.matches(TOK_KEYWORD, 'if'):
            if_expr = res.register(self.if_expr())
            if res.error: return res
            return res.success(if_expr)           
        elif token.matches(TOK_KEYWORD, 'for'):
            for_expr = res.register(self.for_expr())
            if res.error: return res
            return res.success(for_expr)
        elif token.matches(TOK_KEYWORD, 'while'):
            while_expr = res.register(self.while_expr())
            if res.error: return res
            return res.success(while_expr)
        elif token.matches(TOK_KEYWORD, 'func'):
            func_def = res.register(self.func_def())
            if res.error: return res
            return res.success(func_def)

        return res.failure(InvalidSyntaxError(
            token.pos_start,
            token.pos_end ,
            'Expected int, float, identifier,+, - or ( '
        ))

    #* Call function
    def call(self):
        res = ParseResult() 
        atom = res.register(self.atom())
        if res.error: return res

        if self.currTok.type == TOK_LBRACKET:
            res.register_advancement()
            self.advance()
            arg_nodes = []

            if self.currTok.type == TOK_RBRACKET:
                res.register_advancement()
                self.advance()
            else: 
                arg_nodes.append(res.register(self.expr()))
                
                if res.error:
                    return res.failure(InvalidSyntaxError(
						self.currTok.pos_start, self.currTok.pos_end,
						"Expected ')', 'oyleki', 'if', 'for', 'while', 'func', int, float, identifier, '+', '-', '(' or 'NOT'"
					))
                
                while self.currTok.type == TOK_COMMA: 
                    res.register_advancement()
                    self.advance()

                    arg_nodes.append(res.register(self.expr()))
                    if res.error: return res
                
                if self.currTok.type != TOK_RBRACKET:
                    return res.failure(InvalidSyntaxError(
						self.currTok.pos_start, self.currTok.pos_end,
						f"Expected ',' or ')'"
					))
                res.register_advancement()
                self.advance()

            return res.success(funcCallNode(atom, arg_nodes))
            
        return res.success(atom)

  

    #* Term returns two number nodes as it calls factor function
    def term(self):
        return self.binaryOP(self.factor, (TOK_MUL, TOK_DIV))  

    def power(self):
        return self.binaryOP(self.call, (TOK_POW, ), self.factor)

    #* Expression runs the code term and term runs the factor
    def expr(self): 
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
            value = res.register(self.expr())
            
            if res.error: return res
            return res.success(VarAssignNode(varName, value))
        
        node = res.register(self.binaryOP(self.comp_expr, ((TOK_KEYWORD, 've'), (TOK_KEYWORD, 'veya'))))

        if res.error:
            return res.failure(InvalidSyntaxError(
                self.currTok.pos_start, self.currTok.pos_end,
                "Expected 'oyleki', int, float, identifier, '+', '-' or '('"
            ))

        return res.success(node)