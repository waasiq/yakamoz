from helpers.ErrHandler import RTError
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

    def addedTo(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None

    def subtractedBy(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
    
    def multipliedBy(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None

    def dividedBy(self, other):
        if isinstance(other, Number):
            if (other.value == 0):
                return None, RTError(
                    other.pos_start , other.pos_end,
                    'Division by Zero',
                    self.context
                )
            return Number(self.value / other.value).set_context(self.context), None
    
    def __repr__(self):
        return str(self.value)