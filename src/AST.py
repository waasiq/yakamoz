class NumberNode:
    def __init__(self, token):
        self.token = token

    def __repr__(self):
        return f'{self.token}'


class BinOPNode:
    def __init__(self, opToken ,leftN, rightN):
        self.opToken = opToken
        self.leftN = leftN
        self.rightN = rightN

    def __repr__(self):
        return f'{self.leftN}, {self.opToken}, {self.rightN}'