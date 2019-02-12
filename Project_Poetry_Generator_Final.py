## Project_Poetry_Generator_Final
## February 11, 2019
## A program that randomly generates different forms of poetry
## Pledge:
## I have neither given nor recieved any unauthorized aid.

## Import libraries
import nltk
import random

## Importing my emo poetry as the corpus
poetry2019 = open("Eilidh's Work 2019.txt")

## Tokenize 
from nltk.tokenize import word_tokenize as word
tokenizedPoetry2019 = word(poetry2019.read())

## Create bigrams
bigrams = [x for x in zip(tokenizedPoetry2019[:-1], tokenizedPoetry2019[1:])]

## Using bigrams, filter the corpus through conditional frequency distribution
from collections import defaultdict
cfd = defaultdict(lambda: defaultdict(lambda: 0))
for x in range(len(tokenizedPoetry2019) - 2):
	cfd[tokenizedPoetry2019[x].lower()][tokenizedPoetry2019[x+1].lower()]+= 1




## ISSUE @28
## From this, generate random text w/ a seed word
randomWord = random.choice(poetry2019)
fifteenWords = []
for x in range(0, 15):
	fifteenWords.append(randomWord)
	if (randomWord in cfd):
		## Re-assign the variable 'randomWord' to become a random following word f/ 'cfd'
		randomWord = random.choice(list(cfd[randomWord].keys()))
	else:
		break
print()
print(*fifteenWords)