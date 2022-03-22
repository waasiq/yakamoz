from errors.ErrHandler import RTError
from objects.Numbers import Number
from wrappers.RTResult import RTResult
from Tokens import *


#* Implementation of visitor pattern in the Interpreter class
#* The python implementation of ast also implements the same approach 
#* https://docs.python.org/2.7/library/ast.html#module-ast

class Interpreter:
    def visit(self,node,context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_node)
        return method(node, context)

    def no_visit_node(self,node, context):
        raise Exception(f'No visit_{type(node).__name__} method defined')
    
    def visit_NumberNode(self,node, context):
        return RTResult().success(            
            Number(node.token.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )
        
    def visit_VarAccessNode(self, node, context):
        res = RTResult()
        #* value = name of the token
        var_name = node.var_name_token.value 
        value = context.symbol_table.get(var_name)

        if value is None:
            return res.failure(RTError(
                node.pos_start, node.pos_end,
                f"{var_name} is not defined",
                context
            ))
        
        value = value.copy().set_pos(node.pos_start, node.pos_end)
        return res.success(value)

    def visit_VarAssignNode(self, node , context):
        res = RTResult()
        var_name = node.var_name_token.value
        value = res.register(self.visit(node.value_node, context))

        if res.error: return res

        context.symbol_table.set(var_name, value)
        return res.success(value)

    def visit_BinOPNode(self, node, context):
        res = RTResult()
    
        left = res.register(self.visit(node.leftN, context))
        
        #* Check if left is none and give error
        if left is None: 
            return res.failure(RTError(
                node.pos_start, node.pos_end,
                f"variable {node.leftN.var_name_token.value } not defined",
                context
            ))
                
        if res.error: return res

        right = res.register(self.visit(node.rightN, context))
        if res.error: return res

        #* Check if right is none and give error
        if right is None: 
            return res.failure(RTError(
                node.pos_start, node.pos_end,
                f"variable  { node.rightN.var_name_token.value } not defined",
                context
            ))
                
        tokType = node.opToken.type
        error = None
        if (tokType == TOK_ADD):
            result, error = left.addedTo(right)
        elif(tokType == TOK_DIV):
            result, error = left.dividedBy(right)  
        elif(tokType == TOK_MUL):
            result, error = left.multipliedBy(right)
        elif(tokType == TOK_SUB):
            result, error = left.subtractedBy(right)
        elif(tokType == TOK_POW):
            result, error = left.powerOf(right)
        elif(tokType == TOK_GT):
            result, error = left.greater_than(right)
        elif(tokType == TOK_GTE):
            result, error = left.greater_than_EQ(right)    
        elif(tokType == TOK_LT):
            result, error = left.lesser_than(right)
        elif(tokType == TOK_LTE):
            result, error = left.lesser_than_EQ(right)
        elif(tokType == TOK_DEQUAL):
            result, error = left.compares_to(right)
        elif(tokType == TOK_NTEQUAL):
            result, error = left.not_equal(right)
        elif(node.opToken.matches(TOK_KEYWORD, 've')):
            result, error = left.anded_by(right)
        elif(node.opToken.matches(TOK_KEYWORD, 'veya')):
            result, error = left.ored_by(right)

        if error: return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_ifNode(self, node, context):
        res = RTResult()
        
        for condition, expr in node.cases:
            condition_val = res.register(self.visit(condition, context))
            if res.error: return res

            if condition_val.isTrue():
                expr_val = res.register(self.visit(expr, context))
                if res.error: return res
                return res.success(expr_val)

        if node.else_case: 
                else_val = res.register(self.visit(node.else_case, context))
                if res.error: return res
                return res.success(else_val)

        return res.success(None)

    def visit_forNode(self, node, context):
        res = RTResult()


        start_value = res.register(self.visit(node.start_val, context))
        if res.error: return res

        end_value = res.register(self.visit(node.end_val, context))
        if res.error: return res

        if node.step_value:
            step_value = res.register(self.visit(node.step_value, context))
            if res.error: return res
        else: 
            step_value = Number(1)

        i = start_value.value
        
        
        if step_value.value >= 0:
            condition = lambda: i < end_value.value
        else:
            condition = lambda: i > end_value.value
        
        while condition():
            context.symbol_table.set(node.var_name.value, Number(i))
            i += step_value.value

            res.register(self.visit(node.body_node, context))
            if res.error: return res

        return res.success(None)

       

    def visit_UnaryOPNode(self, node, context):
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.error: return res
        
        error = None
        if node.opToken.type == TOK_SUB:
            number,error = number.multipliedBy(Number(-1)) 
        elif node.opToken.matches(TOK_KEYWORD, 'yoket'):
            number, error = number.implement_not()

        if error: return res.failure(error)
        else:
            return res.success(number.set_pos(node.pos_start, node.pos_end))