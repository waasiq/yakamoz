from helpers.Numbers import Number
from Tokens import *

class Interpreter:
    def visit(self,node):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_node)
        return method(node)

    def no_visit_node(self,node):
        raise Exception(f'No visit_{type(node).__name__} method defined')
    
    def visit_NumberNode(self,node):
        return Number(node.token.value).set_pos(node.pos_start, node.pos_end)
        
    
    def visit_BinOPNode(self, node):
        left = self.visit(node.leftN)
        right = self.visit(node.rightN)

        tokType = node.opToken.type
        if (tokType == TOK_ADD):
            result = left.addedTo(right)
        elif(tokType == TOK_DIV):
            result = left.dividedBy(right)  
        elif(tokType == TOK_MUL):
            result = left.multipliedBy(right)
        elif(tokType == TOK_SUB):
            result = left.subtractedBy(right)
            
        return result.set_pos(node.pos_start, node.pos_end)

    def visit_UnaryOPNode(self, node):
        number = self.visit(node.node)

        if node.opToken.type == TOK_SUB:
            number = number.multipliedBy(Number(-1))

        return number.set_pos(node.pos_start, node.pos_end)