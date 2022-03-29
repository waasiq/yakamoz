from errors.ErrHandler import RTError
from objects.Value import Value

class Number(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    #* Basic Arithmetic Operations
    def addedTo(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None
        else: 
            return None, Value.illegal_operation(self,other)

    def subtractedBy(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
        else: 
            return None, Value.illegal_operation(self,other)
    
    def multipliedBy(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None
        else: 
            return None, Value.illegal_operation(self,other)

    def powerOf(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None
        else: 
            return None, Value.illegal_operation(self,other)
    
    def dividedBy(self, other):
        if isinstance(other, Number):
            if (other.value == 0):
                return None, RTError(
                    other.pos_start , other.pos_end,
                    'Division by Zero',
                    self.context
                )
            return Number(self.value / other.value).set_context(self.context), None
        else: 
            return None, Value.illegal_operation(self,other)
    
    #* Comparison operators class
    def greater_than(self , other):
        if isinstance(other, Number):
            if self.value > other.value:
                return Number(1).set_context(self.context), None
            return Number(0).set_context(self.context), None
        else: 
            return None, Value.illegal_operation(self,other)
    
    def greater_than_EQ(self, other): 
        if isinstance(other, Number):
            if self.value >= other.value:
                return Number(1).set_context(self.context), None
            return Number(0).set_context(self.context), None
        else: 
            return None, Value.illegal_operation(self,other)

    def lesser_than(self , other):
        if isinstance(other, Number):
            if self.value < other.value:
                return Number(1).set_context(self.context), None
            return Number(0).set_context(self.context) , None
        else: 
            return None, Value.illegal_operation(self,other)
    
    def lesser_than_EQ(self, other): 
        if isinstance(other, Number):
            if self.value <= other.value:
                return Number(1).set_context(self.context), None
            return Number(0).set_context(self.context) , None
        else: 
            return None, Value.illegal_operation(self,other)
    
    def compares_to(self,other):
        if isinstance(other, Number):
            if self.value ==  other.value:
                return Number(1).set_context(self.context), None
            return Number(0).set_context(self.context) , None
        else: 
            return None, Value.illegal_operation(self,other)
   
    def not_equal(self,other):
        if isinstance(other, Number):
            if self.value !=  other.value:
                return Number(1).set_context(self.context), None
            return Number(0).set_context(self.context) , None
        else: 
            return None, Value.illegal_operation(self,other)

    def anded_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value and other.value)).set_context(self.context), None
        else: 
            return None, Value.illegal_operation(self,other)

    def ored_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value or other.value)).set_context(self.context), None
        else: 
            return None, Value.illegal_operation(self,other)

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

Number.null = Number(0)
Number.false = Number(0)
Number.true = Number(1)