import os
import subprocess
import recordSpeech as RS
import commandGenerator as CG
import os
	
	
class Jarvis:
	program = ".\\espeak.exe \""
	name = ""
	def __init__(self):
		text = " Hello user. I am Jarvis. May I know your name? "
		print ('\n' + text)
		self.speak(text)
		self.setName()
		
	def setName(self):
		try:
			text = RS.listen()
			self.name = text
		except:
			text = "I could not hear anything. Assigning default name as Shivani"
			print(text)
			self.speak(text)
			self.name = "Shivani"
		text = " Welcome " + str(self.name)
		print(text)
		self.speak(text)
		
	
	def speak(self,text):
		say =  self.program + text + '"'
		os.system(say)
	
	def listen(self):
		text = " What can I do for you ?"
		print("\n" + text)
		self.speak(text)
		try:
			text = RS.listen()
			if "bye" in text:
				text = " " + self.name + ". Please visit again. GoodBye"
				print ( text )
				self.speak(text)
				return
			else:
				print(" you said: " + text)
				self.speak(" I heard " + text)
				text = CG.generateCommand(text)
				self.speak(text)
				#print (" Tagged as: ", tokens)
				self.listen()				
		except:
			text  = " I did not hear clearly. Please Try again. Speak goodbye to stop my execution."
			print(text)
			self.speak(text)
			self.listen()
		
	
if __name__=='__main__':
	
	j = Jarvis() 
	j.listen()
	