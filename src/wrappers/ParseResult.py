
#! Class for parsing the result w.r.t Error Handling
class ParseResult:
	def __init__(self):
		self.error = None
		self.node = None
		self.advance_count = 0
		
	def register_advancement(self):
		self.advance_count += 1

	def register(self, res):
		if isinstance(res, ParseResult):
			self.advance_count += res.advance_count
			if res.error: self.error = res.error
			return res.node
		return res

	def success(self, node):
		self.node = node
		return self

	def failure(self, error):
		if not self.error or self.advance_count == 0:
			self.error = error
		return self
