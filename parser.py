import sys
import fileinput
class Parser:
	def __init__(self,tm=None,standardInput=sys.stdin):
		#the turing machine
		self.tm = tm
		#pseudo standard input, just a redirection here for what to read
		self.standardInput = standardInput
	def start(self):
		for line in fileinput.input():
			print line
		'''
		f = open(self.standardInput)
		for line in f:
			print line
		'''		
