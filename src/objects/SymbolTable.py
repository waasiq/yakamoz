
#! Symbol table class holds the value of the variables respectively in a dict

class SymbolTable:
    def __init__(self):
        self.symbols = {}
        #* Parent is empty but later on this will store the values of the parent function later on
        self.parent = None  

    def get(self,name):
        value = self.symbols.get(name, None) 
        if value == None and self.parent: 
            return self.parent.get(name) 
        return value

    def set(self,name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]
         