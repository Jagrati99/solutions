class string:
	def __init__(self):
		self.s=""
	def getString(self):
		self.s=input()
	def printString(self):
		print(self.s.upper())

obj1=string()
obj1.getString()
obj1.printString()

