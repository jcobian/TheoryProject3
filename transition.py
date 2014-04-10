class Transition:
	def __init__(self,startState,tapeSymbol,resultState,writeSymbol,direction):
		self.startState = startState
		self.tapeSymbol = tapeSymbol
		self.resultState = resultState
		self.writeSymbol = writeSymbol
		self.direction = direction
	
