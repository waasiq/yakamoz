from errors.ErrHandler import RTError

class Number:
    def __init__(self, value):
        self.value = value
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
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None

    def subtractedBy(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
    
    def multipliedBy(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None

    def powerOf(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None

    def dividedBy(self, other):
        if isinstance(other, Number):
            if (other.value == 0):
                return None, RTError(
                    other.pos_start , other.pos_end,
                    'Division by Zero',
                    self.context
                )
            return Number(self.value / other.value).set_context(self.context), None
    
    #* Comparison operators class
    def greater_than(self , other):
        if isinstance(other, Number):
            if self.value > other.value:
                return Number(1).set_context(self.context), None
        return Number(0).set_context(self.context), None

    def greater_than_EQ(self, other): 
        if isinstance(other, Number):
            if self.value >= other.value:
                return Number(1).set_context(self.context), None
        return Number(0).set_context(self.context), None

    def lesser_than(self , other):
        if isinstance(other, Number):
            if self.value < other.value:
                return Number(1).set_context(self.context), None
        return Number(0).set_context(self.context) , None

    def lesser_than_EQ(self, other): 
        if isinstance(other, Number):
            if self.value <= other.value:
                return Number(1).set_context(self.context), None
        return Number(0).set_context(self.context) , None

    def compares_to(self,other):
        if isinstance(other, Number):
            if self.value ==  other.value:
                return Number(1).set_context(self.context), None
        return Number(0).set_context(self.context) , None

    def not_equal(self,other):
        if isinstance(other, Number):
            if self.value !=  other.value:
                return Number(1).set_context(self.context), None
        return Number(0).set_context(self.context) , None

    def anded_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value and other.value)).set_context(self.context), None

    def ored_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value or other.value)).set_context(self.context), None

    def implement_not(self):
        return Number(1 if self.value == 0 else 0).set_context(self.context), None

    def isTrue(self):
        return self.value != 0
    
    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy
	
    def __repr__(self):
        return str(self.value)