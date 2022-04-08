import Errors.strArrows as sArrow

#* Error Handling Classes  
class Error:
    def __init__(self, pos_start, pos_end,err_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.err_name = err_name
        self.details = details
    
    def toStr(self):
        result = f'{self.err_name}: {self.details}'
        result += '\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.line + 1}'       
        result += '\n\n' + sArrow.strArrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end,'Illegal Char', details)

class ExpectedCharError(Error):
	def __init__(self, pos_start, pos_end, details):
		super().__init__(pos_start, pos_end, 'Expected Character', details)

class InvalidSyntaxError(Error):
        def __init__(self, pos_start, pos_end, details = ''):
            super().__init__(pos_start, pos_end, 'Invalid Syntax', details)

class RTError(Error):
    def __init__(self, pos_start, pos_end, details, context):
        super().__init__(pos_start, pos_end, 'Runtime Error', details)
        self.context = context

    def trace_back(self):
        result = ''
        pos = self.pos_start
        ctx = self.context

        while ctx:
            result = f'File {pos.fn}, line {str(pos.line + 1)}, in {ctx.displayName}\n' + result
            pos = ctx.parent_entry_pos
            ctx = ctx.parent
            
        return 'Traceback (most recent call last):\n' + result

    def toStr(self):    
        result = self.trace_back()
        result += f'{self.err_name}: {self.details}'
        result += '\n\n' + sArrow.strArrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
        return result