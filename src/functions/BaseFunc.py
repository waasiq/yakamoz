
from functions.Function     import *
from helpers.Context        import *
from objects.SymbolTable    import *
from objects.Value          import *

class BaseFunction(Value):
    def __init__(self, name):
        super().__init__() 
        self.name = name or '<anonymous>'
    
    def generate_new_context(self):
        new_context = Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
        return new_context

    def check_args(self, arg_names, args, res):
        if len(args) > len(arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"Too many args passed into '{self.name}', arguments passed: {len(args) - len(arg_names)}",
				self.context
            ))

        if len(args) < len(arg_names):
            print('Inside second loop')
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"{len(arg_names) - len(args)} too few args passed into '{self.name}'",
				self.context
            ))
        
        return res.success(None)

    def populate_args(self, arg_names, args, exec_cntx):
        for i in range(len(args)):
            arg_name       = arg_names[i]
            arg_value      = args[i]
            arg_value.set_context(exec_cntx)
            exec_cntx.symbol_table.set(arg_name, arg_value)
    
    def check_and_populate_args(self, arg_names, args, exec_cntx , res):
        res.register(self.check_args(arg_names, args, res))
        if res.error: return res
        
        self.populate_args(arg_names, args, exec_cntx)
        return res.success(None)