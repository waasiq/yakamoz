
#* This class is a helper function
class Context:
    def __init__(self, displayName, parent = None, parent_entry_pos = None, symbol_table = None):
        self.displayName = displayName
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = symbol_table