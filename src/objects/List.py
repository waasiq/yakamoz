
from errors.ErrHandler import RTError
from objects.Value   import Value
from objects.Numbers import Number

class List(Value):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def addedTo(self, other):
        new_list = self.copy()
        new_list.elements.append(other)
        return new_list, None

    def multed_by(self, other):
        if isinstance(other, List):
            new_list = self.copy()
            new_list.elements.extend(other.elements)
            return new_list, None
        else:
            return None, Value.illegal_operation(self, other)
    
    def dividedBy(self, other):
        if isinstance(other, Number):
            try:
                return self.elements[other.value], None
            except: 
                return None, RTError(
                    self.pos_start, self.pos_end,
                    'Element at this index could not be retrieved from list because index is out of bounds',
                    self.context
                )
        else: 
            return None, Value.illegal_operation(self, other)

    def compares_to(self,other):
        return self == other

    def copy(self):
        copy = List(self.elements[:])
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy
    
    def __repr__(self):
        return f'[{", ".join([str(x) for x in self.elements])}]'