import sys

class TuringMachine:
	def __init__(self,inputFile):

		#initialize data structures
		self.states = list()
		self.inputAlphabet = list()
		self.tapeAlphabet = list()
		self.transitionRules = list()
		self.startState = ''
		self.acceptState = ''
		self.rejectState = ''

		#read input file and fill in data structures
		self.readInput(inputFile)
		
		#check to make sure the TM is valid
		self.checkForValidTM()
		
		#check to make sure the TM is determinisitc
		self.checkForDeterminism()

	def checkForDeterminism(self):
		pass

	def checkForValidTM(self):
		#blank character cannot be in input alphabet
		if ' ' in self.inputAlphabet:
			print 'Error: empty string is in input alphabet'
			sys.exit()
		#input alphabet must be subset of tape alphabet
		if set(self.inputAlphabet) < set(self.tapeAlphabet) == False:
			print 'Error: Tape Alphabet is not subset of Input Alphabet'
			sys.exit()
		#tape alphabet must include empty string
		if ' ' not in self.tapeAlphabet:
			print 'Error: Tape Alphabet does not include empty string'
			sys.exit()
		#start state should be valid state
		if self.startState not in self.states:
			print 'Error: start state is not in states'
			sys.exit()
		 #accept and reject state should be valid states and different
		if self.acceptState not in self.states:
			print 'Error: accept state is not in states'
			sys.exit()
				
		if self.rejectState not in self.states:
			print 'Error: reject state is not in states'
			sys.exit()
		if self.acceptState == self.rejectState:
			print 'Error: accept and reject states must be different'
			sys.exit()
	
	#read input file and populate the data structures
	def readInput(self,inputFile):
		f = open(inputFile)
		for line in f:
			line = line.rstrip()
			components = line.split(":")
			type = components[0]
			if(type == "Q"):
				statesString = components[1]
				statesString = statesString.rstrip()
				statesList = statesString.split(",")
				for state in statesList:
					self.states.append(state)
				
			elif(type == "A"):
				inputAlphabetString = components[1]
				inputAlphabetString = inputAlphabetString.rstrip()
				inputAlphabetList = inputAlphabetString.split(",")
				for letter in inputAlphabetList:
					self.inputAlphabet.append(letter)
				
			elif(type == "Z"):
				tapeAlphabetString = components[1]
				tapeAlphabetString = tapeAlphabetString.rstrip()
				tapeAlphabetList = tapeAlphabetString.split(",")
				for letter in tapeAlphabetList:
					self.tapeAlphabet.append(letter)
			
			elif(type == "T"):
				pass	
			elif(type == "S"):
				self.startState = components[1].rstrip()	
			elif(type == "F"):
				finalStates = components[1]
				finalStates = finalStates.rstrip()
				finalStatesList = finalStates.split(",")
				self.acceptState = finalStatesList[0]
				self.rejectState = finalStatesList[1]
		
		f.close()	
		
if __name__ == '__main__':
	tm = TuringMachine(sys.argv[1])
