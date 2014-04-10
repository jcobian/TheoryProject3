class Transition:
	def __init__(self,startState,tapeSymbol,resultState,writeSymbol,direction):
		self.startState = startState
		self.tapeSymbol = tapeSymbol
		self.resultState = resultState
		self.writeSymbol = writeSymbol
		self.direction = direction
	#returns true if the given start state and tape symbol are the ones for this transition
	def isTransition(self,startState,tapeSymbol):
		if self.startState == startState and self.tapeSymbol == tapeSymbol:
			return True
		return False	
