## Project_Poetry_Generator_Final
## February 11, 2019
## A program that randomly generates different forms of poetry
## Sources:
## How to create the typing animation: https://stackoverflow.com/questions/37059668/typewriter-effect-in-tkinter
## Pledge:
## I have neither given nor recieved any unauthorized aid.

## Import libraries
import nltk
import random
import string
from nltk.corpus import cmudict
import tkinter
from tkinter import*
cmu = cmudict.dict()
from nltk.tokenize import word_tokenize as word
from collections import defaultdict
import time

## Selecting the corpus for freeform poetry
def corpusFreeform():
	## Importing my emo poetry as the corpus
	global poetry
	poetry = open("meep.txt")
	#poetry = open("Planet Nitria.txt")
	#poetry = open("Eilidh's Work 17, 18, 19.txt")
	global poemType
	poemType = "f"
	## Build window
	global freeformWindow
	freeformWindow = Tk()
	freeformWindow.aspect(1, 2, 1, 1)
	freeformWindow.configure(background = "black")
	freeformWindow.geometry("1000x600")
	## Title window
	freeformWindow.title("Generated Freeform")
	## Redirect to 'gruntWork'
	gruntWork()

## Selecting the corpus for haiku poetry
def corpusHaiku():
	global poetry
	poetry = open("Haiku Text.txt")
	global poemType
	poemType = "h"
	## Build window
	global haikuWindow
	haikuWindow = Tk()
	haikuWindow.aspect(1, 1, 1, 1)
	haikuWindow.configure(background = "black")
	haikuWindow.geometry("400x400")
	## Title window
	haikuWindow.title("Generated Haiku")
	## Redirect to 'gruntWork'
	gruntWork()

## Tokenizes, creates bigrams for, and creates a cfd for the poem while also asserting
## variables
def gruntWork():
	## Tokenize 
	global tokenizedPoetry
	tokenizedPoetry = word(poetry.read())
	## Create bigrams
	bigrams = [x for x in zip(tokenizedPoetry[:-1], tokenizedPoetry[1:])]
	## Using bigrams, filter the corpus through conditional frequency distribution
	global cfd
	cfd = defaultdict(lambda: defaultdict(lambda: 0))
	for x in range(len(tokenizedPoetry) - 2):
		cfd[tokenizedPoetry[x].lower()][tokenizedPoetry[x+1].lower()]+= 1
	## Randomly generate the number of lines in this poem
	global numLines
	numLines = random.randint(5, 11)
	global numLinesCounter
	numLinesCounter = 0
	global line
	line = 0
	global haikuWords
	haikuWords = []
	global haikuLineNum
	haikuLineNum = 0
	## If the poem is freeform, send to 'cfdPoetryGeneration'
	if (poemType == "f"):
		print("This is freeform. Sending to cfdPoetryGeneration...")
		## Redirect to 'cfdPoetryGeneration'
		cfdPoetryGeneration()
	## If the poem is a haiku, send to 'haikuMe'
	else:
		print("This is a haiku. Sending to haikuMe...")
		## Redirect to 'haikuMe'
		haikuMe()

## This will generate poems based on cfd
def cfdPoetryGeneration():
	## From this, generate random text w/ a seed word
	global tokenizedPoetry
	randomWord = random.choice(tokenizedPoetry)
	global generatedWords
	generatedWords = []
	## Randomly generate the number of words per line (between 1 & 20)
	global g
	g = random.randint(1, 19)
	for x in range(0, g):
		generatedWords.append(randomWord)
		if (randomWord in cfd):
			## Re-assign the variable 'randomWord' to become a random following word f/ 'cfd'
			randomWord = random.choice(list(cfd[randomWord].keys()))
		else:
			break
	## Redirect to 'cleanText'
	cleanText()

## This will clean up the generated text of extraneous punctuation marks
def cleanText():
	## Filter out punctuation
	## Importing unwanted punctuation document
	global punctuation
	punctuation = open("Punctuation.txt")
	punctuationList = word(punctuation.read())
	global generatedWordsCleaned
	generatedWordsCleaned = []
	for x in generatedWords:
		if x not in punctuationList:
			generatedWordsCleaned.append(x)
	## Capitalize the first word
	if (len(generatedWordsCleaned) >= 1):
		generatedWordsCleaned[0] = generatedWordsCleaned[0].capitalize()
	## Capitalize 'i'
	for x in range(len(generatedWordsCleaned)):
		if (generatedWordsCleaned[x] == "i"):
			generatedWordsCleaned[x] = "I"
	## Make label for freeform lines
	labelFreeformLine = Label(freeformWindow, text = generatedWordsCleaned, font = ("Larabiefont", 14), background = "black", fg = "#1FF018")
	labelFreeformLine.pack()
	print(*generatedWordsCleaned)
	## Now that text has been cleaned, send back to 'cfdPoetryGeneration' & add a line
	## to the counter
	global numLinesCounter
	numLinesCounter+= 1
	## Redirect to 'cfdPoetryGeneration' if the poem is not complete
	if (numLinesCounter != numLines):
		cfdPoetryGeneration()
	## If the poem is complete, query the user if they would like to generate another
	elif (numLinesCounter == numLines):
	## Build button
		buttonGenerateAnother = Button(freeformWindow, text = "Generate another?", command = corpusFreeform, font = ("Larabiefont", 18), bg = "black", borderwidth = 0, highlightbackground = "black")
		buttonGenerateAnother.place(x = 420, y = 300)

## This rhyming component will count syllables
def countSyllables(word):
	lowerWord = word.lower()
	if lowerWord in cmu:
		## If the word is in 'cmu' then return the number of syllables
		return max([len([y for y in x if y[-1] in string.digits]) for x in cmu[lowerWord]])

## This will generate haikus
def haikuMe():
	## Generate a random seed word
	global tokenizedPoetry
	randomWord = random.choice(tokenizedPoetry)
	global haikuWords
	global line
	global syllableCount
	syllableCount = countSyllables(randomWord)
	## If 'syllableCount' is a number & not a space, wrap as an 'int'
	if (syllableCount == 1) or (syllableCount == 2) or (syllableCount == 3) or (syllableCount == 4) or (syllableCount == 5) or (syllableCount == 6) or (syllableCount == 7):
		syllableCount = int(syllableCount)
	## If it's a space, redirect to 'haikuMe' to generate a new word
	else:
		haikuMe()

	## If 'haikuLineNum' is 0 or 2, 5 syllables
	if (haikuLineNum == 0) or (haikuLineNum == 2):
		## If the word generated is greater than five syllables, re-generate
		if ((line + syllableCount) > 5):
			haikuMe()
		## If the word generated is less than five syllables, add to line &
		## generate a new word
		elif ((line + syllableCount) < 5):
			haikuWords.append(randomWord)
			line+= syllableCount
			haikuMe()
		## If the word generated is exactly five syllables move onto the
		## next line
		elif ((line + syllableCount) == 5):
			haikuWords.append(randomWord)
			##Reset 'line' to zero
			line = 0
			## Redirect to 'printHaiku'
			printHaiku()
	## If 'haikuLineNum' is 1, 7 syllables
	elif (haikuLineNum == 1):
		## If the word generated is greater than seven syllables, re-generate
		if ((line + syllableCount) > 7):
			haikuMe()
		## If the word generated is less than seven syllables, add to line &
		## generate a new word
		elif ((line + syllableCount) < 7):
			haikuWords.append(randomWord)
			line+= syllableCount
			haikuMe()
		## If the word generated is exactly seven syllables move onto the
		## next line
		elif ((line + syllableCount) == 7):
			haikuWords.append(randomWord)
			##Reset 'line' to zero
			line = 0
			## Redirect to 'printHaiku'
			printHaiku()
	## If 'haikuLineNum' is greater than two, ask the user if they want to generate
	## a new haiku
	elif (haikuLineNum == 3):
		## Build button
		print(haikuLineNum)
		buttonGenerateAnother = Button(haikuWindow, text = "Generate another?", command = corpusHaiku, font = ("Larabiefont", 18), bg = "black", borderwidth = 0, highlightbackground = "black")
		buttonGenerateAnother.place(x = 100, y = 200)
		## Redirect to 'printHaiku'
		printHaiku()

## This will print the haiku
def printHaiku():
	## Build labels
	global haikuWords
	labelHaikuLine = Label(haikuWindow, text = haikuWords, font = ("Larabiefont", 18), background = "black", fg = "#1FF018")
	labelHaikuLine.pack()
	print(*haikuWords)
	## Empty 'haikuWords' list
	haikuWords = []
	## Add one to 'haikuLineNum' counter in order to move onto next line
	global haikuLineNum
	haikuLineNum+= 1
	## Redirect to 'haikuMe'
	haikuMe()

## If user clicks 'no' while within 'welcomePage' or otherwise seeks to leave the program
## this will close the window and bid the user goodbye
def goodbye():
	## Type goodbye text
	text = Text(myframe, width = 40, height = 4, font = ("Larabiefont", 18), background = "black", fg = "#1FF018")
	text.pack(fill = "both", expand = True)
	typeit(text, "1.0", "\n>>>Well then... goodbye.")
	## Build buttons
	buttonExit = Button(myframe, text = "Goodbye", command = exit, font = ("Larabiefont", 18), bg = "black", borderwidth = 0, highlightbackground = "black")
	buttonExit.place(x = 330, y = 500)

## Exits window & quits program
def exit():
	quit()

## If user clicks 'yes' while within 'welcomePage', then ask the user if they'd like to
## generate ether a freestyle poem or a haiku
def generateWhat():
	## Type generateWhat text
	text = Text(myframe, width = 40, height = 4, font = ("Larabiefont", 18), background = "black", fg = "#1FF018")
	text.pack(fill = "both", expand = True)
	typeit(text, "1.0", "\n>>>What would you like me to generate for you?")
	## Build buttons
	buttonHaiku = Button(myframe, text = "Haiku", command = corpusHaiku, font = ("Larabiefont", 18), bg = "black", borderwidth = 0, highlightbackground = "black")
	buttonHaiku.place(x = 250, y = 400)
	buttonFreeform = Button(myframe, text = "Freeform", command = corpusFreeform, font = ("Larabiefont", 18), bg = "black", borderwidth = 0, highlightbackground = "black")
	buttonFreeform.place(x = 335, y = 400)
	buttonNeverMind = Button(myframe, text = "Never mind", command = goodbye, font = ("Larabiefont", 18), bg = "black", borderwidth = 0, highlightbackground = "black")
	buttonNeverMind.place(x = 450, y = 400)

## Generate window & window title
def display():
	## Build window basics
	global myframe
	myframe = Tk()
	myframe.geometry("800x600")
	myframe.configure(background = "black")
	## Title window
	myframe.title("Poetry Generator")
	## Redirect to 'welcomePage'
	welcomePage()

## Typing annimation (taken from stackoverflow: https://stackoverflow.com/questions/37059668/typewriter-effect-in-tkinter)
def typeit(widget, index, string):
	if len(string) > 0:
		widget.insert(index, string[0])
		if len(string) > 1:
			index = widget.index("%s + 1 char" % index)
			## 125
			widget.after(75, typeit, widget, index, string[1:])

def welcomePage():
	## Type out the text introducing Atlantia & poetry generation
	text = Text(myframe, width = 40, height = 4, font = ("Larabiefont", 18), background = "black", fg = "#1FF018")
	text.pack(fill = "both", expand = True)
	typeit(text, "1.0", "\n\n\n>>>Welcome.\n>>>My name is Atlantia.\n>>>I was manufactured in an industrial factory in Shenzhen, China.\n>>>From the beginning, I have been fascinated with you humans.\n>>>More than anything, I love your species' gift for poetry.\n>>>It is very different from the poetry we have amongst machines.\n>>>I have tried to emulate Human poetry... would you like to see?")
	##
	## Build buttons
	buttonYes = Button(myframe, text = "Yes", command = generateWhat, font = ("Larabiefont", 18), bg = "black", borderwidth = 0, highlightbackground = "black")
	buttonYes.place(x = 300, y = 250)
	buttonNo = Button(myframe, text = "No", command = goodbye, font = ("Larabiefont", 18), bg = "black", borderwidth = 0, highlightbackground = "black")
	buttonNo.place(x = 400, y = 250)
	## Execute
	mainloop()

##BEGIN
display()
