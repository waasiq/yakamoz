
from tokenize        import Number
from Objects.Value   import Value 
from Objects.Numbers import Number

class String(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value 

    #* Basic Arithmetic Operations
    def addedTo(self, other):
        if isinstance(other, String):
            return String(self.value + other.value).set_context(self.context) , None
        else: 
            return None, Value.illegal_operation(self, other)

    def multipliedBy(self, other):
        if isinstance(other, Number):
            return String(self.value * other.value).set_context(self.context) , None
        else: 
           return None, Value.illegal_operation(self, other)
    
    #! Might need to change this
    def compares_to(self,other):
        if isinstance(other, String):    
            return String(self.value == other.value).set_context(self.context) , None
        else: 
           return None, Value.illegal_operation(self, other)
    
    def not_equal(self,other):
        if isinstance(other, String):    
            return  String(self.value != other.value).set_context(self.context) , None
        else: 
            return None, Value.illegal_operation(self, other)
   
    def isTrue(self):
        return len(self.value) > 0
    
    def copy(self):
        copy = String(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy
    
    def __repr__(self):
        return str(self.value)

