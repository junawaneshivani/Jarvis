from nltk import pos_tag
from datetime import datetime
from os import system
import subprocess

startVerbList = ['open','opened','start']
closeVerbList = ['close','closed','stop']
nounList = ['notepad','browser','chrome','editor','texteditor','note']
subNounList = ['google','facebook','twitter','fb']


def posTagger(text):
	text = text.split()
	return pos_tag(text)
	
def generateCommand(text):
	text = text.lower()
	text = text.split()
	if text[0] in startVerbList:
		text.remove(text[0])
		text = openSomething(text)
	elif text[0] in closeVerbList:
		text.remove(text[0])
		text = closeSometing(text)
	else:
		text = ' You did not gave a valid command. Please try again.'
		print (text)
	return text			
	
def openSomething(text):
	#print ("in open")
	#print (text)
	if len(text)==1 or text[0] in nounList or text[0] in subNounList:
		text = text[0]
		if text in ['browser','browsers']:
			text = "chrome"
		elif text in ['editor','texteditor','note']:
			text = 'notepad'
		elif text in ['fb','face','facebook']:
			text = 'facebook'
		if text in nounList:
			x = system('start ' + text + " >nul")
			if (x==0):
				text = " Successfully opened " + text
				print(text)
			else:
				text = " Cannot open " + text
				print(text)
		elif text in subNounList:
			x = system('start chrome -new "www.' + text + '.com" >nul')
			if (x==0):
				text = " Successfully opened " + text
				print(text)
			else:
				text = " Cannot open " + text
				print(text)
	else:
		text = ' You did not gave a valid command. Please try again.'
		print(text)
	return text
	
def closeSometing(text):
	#print (" in close")
	if len(text)==1 or text[0] in nounList or text[0] in subNounList:
		text = text[0]
		if text in ['browser','browsers']:
			text = "chrome"
		elif text in ['editor','texteditor','note']:
			text = 'notepad'
		elif text in ['fb','face','facebook']:
			text = 'facebook'
		if text in nounList:
			x = system('Taskkill /IM '+text+'.exe /F > nul')
			if (x==0):
				text = " Successfully closed " + text
				print(text)
			else:
				text = " Cannot close " + text
				print(text)
		elif text in subNounList:
			text = 'chrome'
			x = system('Taskkill /IM '+text+'.exe /F > nul')
			if (x==0):
				text = " Successfully closed " + text
				print(text)
			else:
				text = " Cannot close " + text
				print(text)
	else:
		text = ' You did not gave a valid command. Please try again.'
		print(text)
	return text
	