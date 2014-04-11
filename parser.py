import sys
class Parser:
	def __init__(self,tm=None):
		#the turing machine
		self.tm = tm
		self.lines = sys.stdin.readlines()
		self.max_transitions = 1000
		self.accept = False
	def start(self):
		numTapes = int(self.lines[0].rstrip())
		for x in range (1,numTapes+1):
			line = self.lines[x].rstrip()
			tapeInputList = line.split(",")
			num_transitions = 0
			currentTapeIndex = 0
			currentTapeSymbol = tapeInputList[currentTapeIndex]
			while num_transitions<self.max_transitions:
				direction = self.tm.performTransition(currentTapeSymbol)	
				if(direction == "L"):
					if(currentTapeIndex==0):
						print 'Error: moving left when at the head of the tape'
						break
					else:		
						currentTapeIndex-=1
				elif(direction == "R"):
					currentTapeIndex+=1
				
				if(currentTapeIndex >= len(tapeInputList)):
					currentTapeSymbol = ' '
				else:
					currentTapeSymbol = tapeInputList[currentTapeIndex]
				
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
			
		
