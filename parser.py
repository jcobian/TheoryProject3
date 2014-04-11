import sys
class Parser:
	def __init__(self,tm=None):
		#the turing machine
		self.tm = tm
		#reads lines from standard input and places in list
		self.lines = sys.stdin.readlines()

		self.max_transitions = 1000
		#true if the TMaccepts
		self.accept = False
		#current Index of the tape to read
		self.currentTapeIndex = 0
		#list that contains the tape
		self.tapeInputList = list()
	def start(self):
		try:
			numTapes = int(self.lines[0].rstrip())
		except:
			print 'Error, first line in stdin must be an int'
			sys.exit()
		#for each tape input
		for x in range (1,numTapes+1):
			#reset variables to initial state
			self.accept = False
			self.currentTapeIndex = 0
			self.tapeInputList = list()
			#num of transitions applied 
			num_transitions = 0
			
			#grab the line
			line = self.lines[x].rstrip()
			#populate the tape
			self.tapeInputList = line.split(",")
			#set current tape to be the first symbol in tape
			currentTapeSymbol = self.tapeInputList[self.currentTapeIndex]
			#print initial information
			self.printInfo()	
			while num_transitions<self.max_transitions:
				#perform a transition and get the next direction and the symbol to write
				direction,writeSymbol = self.tm.performTransition(currentTapeSymbol)
				#write the symbol to the tape	
				self.tapeInputList[self.currentTapeIndex] = writeSymbol
				
				if(direction == "L"):
					if(self.currentTapeIndex==0):
						print 'Error: moving left when at the head of the tape'
						break	
					else:		
						self.currentTapeIndex-=1
					
				elif(direction == "R"):
					self.currentTapeIndex+=1
			
				#if index is outside the bounds of the tape list, append an empty char	
				if(self.currentTapeIndex >= len(self.tapeInputList)):
					self.tapeInputList.append(' ')

				#set the new current symbol
				currentTapeSymbol = self.tapeInputList[self.currentTapeIndex]
				#print the information about the tape and TM
				self.printInfo()
				
				if(self.tm.isInAcceptState()):
					self.accept = True
					break
				elif(self.tm.isInRejectState()):
					break;
				num_transitions+=1
		
			if(self.accept == True):
				print 'ACCEPT'
			else:
				print 'REJECT'
			self.tm.reset()
			#print a new line b/w tapes unless you're on the last tape
			if(x<numTapes):
				print ''
	#prints information to stdout about the tape and current state of TM
	def printInfo(self):
		self.output = '('
		self.output += self.getBeginningTapeInfo()
		self.output += ')'
		self.output += self.tm.currentState
		self.output+='('
		self.output+= self.getEndingTapeInfo()
		self.output+=')'
		print self.output
		
	#returns true if there are non empty characters AFTER (but not including) index
	def areMoreLettersToPrint(self,index):
		for x in range(index+1,len(self.tapeInputList)):
			if x != ' ':
				return True
		return False

	#prints tape from current index until rightmost non blank character
	def getEndingTapeInfo(self):
		output = ''
		for x in range(self.currentTapeIndex,len(self.tapeInputList)):
			if self.tapeInputList[x] == ' ':
				if self.areMoreLettersToPrint(x) == False:
					break
			output+=self.tapeInputList[x]+','
		output = output.rstrip(',')
		return output
	#prints tape from begining to the head (current tape index) but not including head
	def getBeginningTapeInfo(self):
		output = ''
		for x in range(0,self.currentTapeIndex):
			output+=self.tapeInputList[x] + ','
		output = output.rstrip(',')
		return output
				
