
#* AST Node Classes

#* Basic Number Node class
class NumberNode:
    def __init__(self, token):
        self.token = token
        self.pos_start = self.token.pos_start
        self.pos_end = self.token.pos_end

    def __repr__(self):
        return f'{self.token}'

#* Binary Operation Node is something like this:
#*             +
#*          /   \
#*       LNode   RNODE
class BinOPNode:
    def __init__(self, opToken ,leftN, rightN):
        self.opToken = opToken
        self.leftN = leftN #* These can be numbernodes or opnodes
        self.rightN = rightN

        self.pos_start = self.leftN.pos_start
        self.pos_end = self.rightN.pos_end

    def __repr__(self):
        return f'({self.leftN}, {self.opToken}, {self.rightN})'

#* Unary Operation Node , unary operation: ++ , -- 
#* It will contain the opTOKEN eg: +,- and node beside it, will look something like 
#* this in the AST TREE:
#*             +
#*          /
#*       +
#*     / 
#*   2 

class UnaryOPNode:
    def __init__(self, opToken, node):
        self.opToken = opToken
        self.node = node

        self.pos_start = self.opToken.pos_start
        self.pos_end = self.node.pos_end

    def __repr__(self):
        return f'({self.opToken} , {self.node})'


#* IF, FOR, WHILE Nodes below this
class forNode:
    def __init__(self, var_name, start_val, end_val, step_value, body_node):
        self.var_name       = var_name
        self.start_val      = start_val        
        self.end_val        = end_val
        self.step_value     = step_value
        self.body_node      = body_node

        self.pos_start      = self.var_name.pos_start
        self.pos_end        = self.body_node.pos_end

class ifNode:
      def __init__(self, cases, else_case):
        self.cases = cases
        self.else_case = else_case

        self.pos_start = self.cases[0][0].pos_start
        self.pos_end = (self.else_case or self.cases[len(self.cases) - 1][0]).pos_end

#* Variable Assignment and Access Nodes
class VarAssignNode:
    def __init__(self, var_name_token, value_node):
        self.var_name_token = var_name_token
        self.value_node     = value_node

        self.pos_start  = self.var_name_token.pos_start
        self.pos_end    = self.value_node.pos_end

class VarAccessNode:
    def __init__(self, var_name_token):
        self.var_name_token      = var_name_token
        self.pos_start           = self.var_name_token.pos_start
        self.pos_end             = self.var_name_token.pos_end