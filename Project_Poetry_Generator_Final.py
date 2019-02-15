## Project_Poetry_Generator_Final
## February 11, 2019
## A program that randomly generates different forms of poetry
## Pledge:
## I have neither given nor recieved any unauthorized aid.

## Import libraries
import nltk
import random

## Importing my emo poetry as the corpus
global poetry
poetry = open("Eilidh's Work 17, 18, 19.txt")

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
numLines = random.randint(1, 11)
global numLinesCounter
numLinesCounter = 0

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

## Begin generating poetry & redirect to 'cfdPoetryGeneration'
cfdPoetryGeneration()



