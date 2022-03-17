class Number:
    def __init__(self, value):
        self.value = value
        self.set_pos()

    def set_pos(self, pos_start = None, pos_end = None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def addedTo(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)

    def subtractedBy(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
    
    def multipliedBy(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value)

    def dividedBy(self, other):
        if isinstance(other, Number):
            return Number(self.value / other.value) 
    
    def __repr__(self):
        return str(self.value)