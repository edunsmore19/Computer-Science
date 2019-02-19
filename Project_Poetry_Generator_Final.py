## Project_Poetry_Generator_Final
## February 11, 2019
## A program that randomly generates different forms of poetry
## Sources:
## How to create a time delay: https://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
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
import time

## Importing my emo poetry as the corpus
global poetry
poetry = open("Eilidh's Work 17, 18, 19.txt")
#poetry = open("Haiku Text.txt")

## Tokenize 
from nltk.tokenize import word_tokenize as word
tokenizedPoetry = word(poetry.read())

## Create bigrams
bigrams = [x for x in zip(tokenizedPoetry[:-1], tokenizedPoetry[1:])]

## Using bigrams, filter the corpus through conditional frequency distribution
from collections import defaultdict
cfd = defaultdict(lambda: defaultdict(lambda: 0))
for x in range(len(tokenizedPoetry) - 2):
	cfd[tokenizedPoetry[x].lower()][tokenizedPoetry[x+1].lower()]+= 1

## Randomly generate the number of lines in this poem
global numLines
numLines = random.randint(3, 11)
global numLinesCounter
numLinesCounter = 0
global line
line = 0
global haikuWords
haikuWords = []
global haikuLineNum
haikuLineNum = 0

## This will generate poems based on cfd
def cfdPoetryGeneration():
	## From this, generate random text w/ a seed word
	randomWord = random.choice(tokenizedPoetry)
	global generatedWords
	generatedWords = []
	## Randomly generate the number of words per line (between 1 & 20)
	global g
	g = random.randint(1, 21)
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
	generatedWordsCleaned[0] = generatedWordsCleaned[0].capitalize()
	## Capitalize 'i'
	for x in range(len(generatedWordsCleaned)):
		if (generatedWordsCleaned[x] == "i"):
			generatedWordsCleaned[x] = "I"
	print(*generatedWordsCleaned)
	## Now that text has been cleaned, send back to 'cfdPoetryGeneration' & add a line
	## to the counter
	global numLinesCounter
	numLinesCounter+= 1
	## Redirect to 'cfdPoetryGeneration' if the poem is not complete
	if (numLinesCounter != numLines):
		cfdPoetryGeneration()

## This rhyming component will count syllables
def countSyllables(word):
	lowerWord = word.lower()
	if lowerWord in cmu:
		## If the word is in 'cmu' then return the number of syllables
		return max([len([y for y in x if y[-1] in string.digits]) for x in cmu[lowerWord]])

## This will generate haikus
def haikuMe():
	## Generate a random seed word
	randomWord = random.choice(tokenizedPoetry)
	global haikuWords
	global line
	global syllableCount
	syllableCount = countSyllables(randomWord)
	#print("syllableCount", syllableCount)
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
	else:
		exit()

## This will print the haiku
def printHaiku():
	global haikuWords
	print(*haikuWords)
	## Empty 'haikuWords' list
	haikuWords = []
	## Add one to 'haikuLineNum' counter in order to move onto next line
	global haikuLineNum
	haikuLineNum+= 1
	## Redirect to 'haikuMe'
	haikuMe()

def click():
	print("Click!")

## If user clicks 'no' while within 'welcomePage' or otherwise seeks to leave the program
## this will close the window and bid the user goodbye
def goodbye():
	## Build labels
	labelGoodbye = Label(myframe, text = "Goodbye.")
	labelGoodbye.pack()
	time.sleep(5)
	quit()

## If user clicks 'yes' while within 'welcomePage', then ask the user if they'd like to
## generate ether a freestyle poem or a haiku
def generateWhat():
	## Build labels
	labelWhat = Label(myframe, text = "What would you like me to generate for you?")
	labelWhat.pack()
	## Build buttons
	buttonHaiku = Button(myframe, text = "Haiku", command = click)
	buttonHaiku.pack()
	buttonFreeform = Button(myframe, text = "Freeform", command = click)
	buttonFreeform.pack()

## Generate window & window title
def display():
	## Build window basics
	global myframe
	myframe = Tk()
	myframe.aspect(1, 1, 1, 1)
	myframe.geometry("800x800")
	## Title window
	myframe.title("Poetry Generator")
	## Redirect to 'welcomePage'
	welcomePage()

def welcomePage():
	## Build labels (AKA: text boxes)
	labelWelcome = Label(myframe, text = "Welcome.")
	labelWelcome.pack()
	labelIntro = Label(myframe, text = "My name is Atlantia.")
	labelIntro.pack()
	labelOrigin = Label(myframe, text = "I was manufactured in an industrial factory in Shenzhen, China.")
	labelOrigin.pack()
	labelHumanity = Label(myframe, text = "Ever since I was first brought online, I have been fascinated with you humans.")
	labelHumanity.pack()
	labelLove = Label(myframe, text = "More than anything, I love your species' gift for poetry. It is very different than the poetry we have amongst machines.")
	labelLove.pack()
	labelLikeToSee = Label(myframe, text = "I have tried to emulate Human poetry... would you like to see?")
	labelLikeToSee.pack()
	## Build buttons
	buttonYes = Button(myframe, text = "Yes", command = generateWhat)
	buttonYes.pack()
	buttonNo = Button(myframe, text = "No", command = goodbye)
	buttonNo.pack()

	## Execute
	mainloop()

##BEGIN
display()

## Begin generating poetry & redirect to 'cfdPoetryGeneration'
#cfdPoetryGeneration()
#print()
#haikuMe()
