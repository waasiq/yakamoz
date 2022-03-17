
#* AST Node Classes
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

class UnaryOPNode:
    def __init__(self, opToken, node):
        self.opToken = opToken
        self.node = node

        self.pos_start = self.opToken.pos_start
        self.pos_end = self.node.pos_end

    def __repr__(self):
        return f'({self.opToken} , {self.node})'

