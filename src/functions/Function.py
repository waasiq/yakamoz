
from functions.BaseFunc import BaseFunction
from wrappers.RTResult import RTResult

class Function(BaseFunction):
    def __init__(self, name, arg_names, body_node):
        super().__init__(name)
        self.arg_names = arg_names
        self.body_node = body_node

    def execute(self, args, intrprt, res):        
        new_context = self.generate_new_context()
        
        res.register(self.check_and_populate_args(self.arg_names, args, new_context, res))
        if res.error: return res

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