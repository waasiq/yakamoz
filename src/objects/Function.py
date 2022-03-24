from objects.Value import Value
from wrappers.RTResult import RTResult
from helpers.Context import Context
from objects.SymbolTable import SymbolTable 
from errors.ErrHandler import RTError


class Function(Value):
    def __init__(self, name, arg_names, body_node):
        super().__init__()
        self.name = name or '<anonymous>'
        self.arg_names = arg_names
        self.body_node = body_node

    def execute(self, args, intrprt):
        res = RTResult()
        
        new_context = Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
        
        if len(args) > len(self.arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"{len(args) - len(self.arg_names)} too many args passed into '{self.name}'",
				self.context
            ))

        if len(args) < len(self.arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"{len(self.arg_names) - len(args)} too few args passed into '{self.name}'",
				self.context
            ))

        for i in range(len(args)):
            arg_name  = self.arg_names[i]
            arg_value = args[i]
            arg_value.set_context(new_context)
            new_context.symbol_table.set(arg_name, arg_value)

        value = res.register(intrprt.visit(self.body_node, new_context))

        if res.error: return res
        return res.success(value)

    def copy(self):
        copy = Function(self.name, self.body_node, self.arg_names)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<function {self.name}>"