from helpers.Numbers import Number
from helpers.RTResult import RTResult
from Tokens import *

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
        
    
    def visit_BinOPNode(self, node, context):
        res = RTResult()

        left = res.register(self.visit(node.leftN, context))
        if res.error: return res
        right = res.register(self.visit(node.rightN, context))
        if res.error: return res

        tokType = node.opToken.type
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
            
            
        if error: return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_UnaryOPNode(self, node, context):
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.error: return res

        if node.opToken.type == TOK_SUB:
            number,error = number.multipliedBy(Number(-1)) 

        if error: return res.failure(error)
        else:
            return res.success(number.set_pos(node.pos_start, node.pos_end))