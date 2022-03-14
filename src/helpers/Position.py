
#* Position class returns the position of the element and advances 
#* Using the positiong in Error Handling as of now

class Position:
    '''
        col -> column Number
        fn -> File Number
        ftxt -> File text 
        line -> Line Number
        indx -> Index
    '''

    def __init__(self, indx, line , col, fn, ftxt):
        self.indx = indx
        self.line = line
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, currChar = None):
        self.indx += 1 
        self.col += 1

        if currChar == '\n':
            self.line += 1
            self.col = 0
        return self
    
    def copy(self):
        return Position(self.indx, self.line , self.col, self.fn, self.ftxt)
