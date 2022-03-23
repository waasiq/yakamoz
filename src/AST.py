
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
    def __init__(self, var_name_node, start_val_node, end_val_node, step_value_node, body_node):
        self.var_name_node       = var_name_node
        self.start_val_node      = start_val_node        
        self.end_val_node        = end_val_node
        self.step_value_node     = step_value_node
        self.body_node           = body_node

        self.pos_start      = self.var_name_node.pos_start
        self.pos_end        = self.body_node.pos_end

class whileNode:
        def __init__(self, condition_node, body_node):
            self.condition_node       = condition_node
            self.body_node            = body_node

            self.pos_start      = self.condition_node.pos_start
            self.pos_end        = self.body_node.pos_end

class ifNode:
      def __init__(self, cases, else_case):
        self.cases = cases
        self.else_case = else_case

        self.pos_start = self.cases[0][0].pos_start
        self.pos_end = (self.else_case or self.cases[len(self.cases) - 1][0]).pos_end


#* Function nodes below this
class funcDefNode:
    def __init__(self, func_name_token, arg_name_tokens ,  body_node):
        self.func_name_token = func_name_token
        self.arg_name_tokens = arg_name_tokens
        self.body_node       = body_node

        if self.func_name_token:
            self.pos_start = self.func_name_token.pos_start
        elif len(arg_name_tokens) > 0: 
            self.pos_start = self.arg_name_tokens[0].pos_start
        else:
            self.pos_start = self.body_node.pos_start

        self.pos_end = self.body_node.pos_end

class funcCallNode:
    def __init__(self, node_to_call , arg_nodes):
        self.node_to_call = node_to_call
        self.arg_nodes    = arg_nodes

        self.pos_start = self.node_to_call.pos_start

        if len(arg_nodes) > 0:
            self.pos_end = self.arg_nodes[len(arg_nodes)  - 1].pos_end
        else:
            self.pos_end = self.node_to_call.pos_end

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