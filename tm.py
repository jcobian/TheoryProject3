import sys
from transition import Transition
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

	#returns true if the given start state and current tape symbol exist in the transition rules
	#if its false when called with the current state and the current tape symbol, then this means you should implicitly to the reject state
	def doesTransitionExist(self,startState,tapeSymbol):
		for transition in self.transitionRules:
			if transition.isTransition(startState,tapeSymbol) == True:
				return True
		return False

	def checkForDeterminism(self):
		#make sure no two transitions have the same starting state and current tape symbol
		for transition in self.transitionRules:
			count = 0
			for secondTransition in self.transitionRules:
				if transition.startState == secondTransition.startState and transition.tapeSymbol == secondTransition.tapeSymbol:		
					count+=1
			#count will at least be one because you will loop on yourself
			if count >=2:
				print 'Error: Non Deterministic. Two or more transitions have the same starting state and current tape symbol'
				sys.exit()
			
			
	
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

		for transition in self.transitionRules:
			#make sure each state in transition rules are valid states
			if transition.startState not in self.states:
				print 'Error: a transition\'s start state is not a valid state'
				sys.exit()
			
			if transition.resultState not in self.states:
				print 'Error: a transition\'s result state is not a valid state'
				sys.exit()
			#make sure the tapeSymbol and writeSymbol are in tape alphabet
			if transition.tapeSymbol not in self.tapeAlphabet:
				print 'Error: a transition\'s tape symbol is not in the tape alphabet'
				sys.exit()
						
			if transition.writeSymbol not in self.tapeAlphabet:
				print 'Error: a transition\'s write symbol is not in the tape alphabet'
				sys.exit()
			#make sure direction is L or R
			if transition.direction != "L" and transition.direction != "R":
				print 'Error: a transition\'s direction is not L or R'
				sys.exit()
			#make sure no transitions from the accept or reject states
			if transition.startState == self.acceptState:
				print 'Error: a transition\'s start state is the accept state'
				sys.exit()
			if transition.startState == self.rejectState:
				print 'Error: a transition\'s start state is the reject state'
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
				transitionString = components[1]
				transitionString = transitionString.rstrip()
				transitionList = transitionString.split(",")
			
				if(len(transitionList) != 5):
					print 'Error, a transition is invalid'
					sys.exit()
	
				t_startState = transitionList[0]
				t_tapeSymbol = transitionList[1]
				t_resultState = transitionList[2]
				t_writeSymbol = transitionList[3]
				t_direction = transitionList[4]
				
				transition = Transition(t_startState,t_tapeSymbol,t_resultState,t_writeSymbol,t_direction)
				self.transitionRules.append(transition)				
			
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
