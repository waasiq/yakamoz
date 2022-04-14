
from Funcs.BaseFunc import BaseFunction
from Objects.Numbers import Number

class Function(BaseFunction):
    def __init__(self, name, arg_names, body_node, should_auto_return):
        super().__init__(name)
        self.arg_names          = arg_names
        self.body_node          = body_node
        self.should_auto_return = should_auto_return

    def execute(self, args, intrprt, res):        
        new_context = self.generate_new_context()
        
        res.register(self.check_and_populate_args(self.arg_names, args, new_context, res))
        if res.error: return res

        value = res.register(intrprt.visit(self.body_node, new_context))
        if res.should_return() and res.func_return_value == None: return res
        
        ret_value = (value if self.should_auto_return else None) or res.func_return_value or Number.null
        return res.success(ret_value)

    def copy(self):
        copy = Function(self.name, self.body_node, self.arg_names, self.should_auto_return)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<function {self.name}>"