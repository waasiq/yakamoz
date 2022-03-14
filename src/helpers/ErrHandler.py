import helpers.strArrows as sArrow

#* Error Handling Classes  
class Error:
    def __init__(self, pos_start, pos_end,err_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.err_name = err_name
        self.details = details
    
    def toStr(self):
        result = f'{self.err_name}: {self.details}'
        result += f'File {self.pos_start.fn}, line {self.pos_start.line + 1}'
        result += '\n\n' + sArrow.strArrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
        return result

class IllegalChar(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end,'Illegal Char', details)

class InvalidSyntax(Error):
        def __init__(self, pos_start, pos_end, details = ''):
            super().__init__(pos_start, pos_end, 'Invalid Syntax', details)
