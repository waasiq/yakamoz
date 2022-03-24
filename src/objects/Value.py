
from errors.ErrHandler import RTError
from wrappers.RTResult import RTResult

class Value:
    def __init__(self):
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start = None, pos_end = None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context = None):
        self.context = context
        return self 

    #* Basic Arithmetic Operations
    def addedTo(self, other):
        return None, self.illegal_operation(other)

    def subtractedBy(self, other):
        return None, self.illegal_operation(other)
    
    def multipliedBy(self, other):
        return None , self.illegal_operation(other)

    def powerOf(self, other):
        return None , self.illegal_operation(other)

    def dividedBy(self, other):
        return None , self.illegal_operation(other)
    
    #* Comparison operators class
    def greater_than(self , other):
        return None, self.illegal_operation(other)

    def greater_than_EQ(self, other): 
        return None, self.illegal_operation(other)

    def lesser_than(self , other):
        return None, self.illegal_operation(other)

    def lesser_than_EQ(self, other): 
        return None , self.illegal_operation(other)

    def compares_to(self,other):
        return None, self.illegal_operation(other)

    def not_equal(self,other):
        return None , self.illegal_operation(other)

    def anded_by(self, other):
        return None , self.illegal_operation(other)

    def ored_by(self, other):
            return None, self.illegal_operation(other)

    def implement_not(self):
        return None, self.illegal_operation(None)

    def isTrue(self):
        return False
    
    def execute(self, args):
        return RTResult().failure(self.illegal_operation())

    def copy(self):
        raise Exception('No copy method defined')

    def illegal_operation(self, other=None):
        if not other: other = self
        return RTError(
			self.pos_start, other.pos_end,
			'Illegal operation',
			self.context
		)