## Project_Poetry_Generator_Groundwork
## February 8, 2019
## A program that randomly generates poetry (the underlying basics/understanding)
## Sources:
## The basics behind random text prediction: https://www.hallada.net/2017/07/11/generating-random-poems-with-python.html
## Understanding 'defaultdict' container: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
## Understanding 'gutenberg' corpora: https://www.hackerrank.com/challenges/defaultdict-tutorial/problem
## Understanding 'keys()' method: https://www.tutorialspoint.com/python3/dictionary_keys.htm
## Understanding NLTK's 'syntax trees': http://www.nltk.org/book/ch08.html
## Understanding how tokenize w/out punctuation: https://stackoverflow.com/questions/15547409/how-to-get-rid-of-punctuation-using-nltk-tokenizer
##Pledge:
## I have neither given nor recieved any unauthorized aid.

## Import libraries
import nltk
import random

## Begin with 'corpus' (the text our generator will blend & shake up)
corpus = "The quick brown fox jumps over the lazy dog and the quick cat."

## Tokenize 'corpus' by word
from nltk.tokenize import word_tokenize as tokenizeWord
tokenizedCorpus = tokenizeWord(corpus)
print(tokenizedCorpus)

## Create bigrams (pair of two words that are in the order they appear in the corpus)
bigrams = [x for x in zip(tokenizedCorpus[:-1], tokenizedCorpus[1:])]
print(bigrams)


## Using bigrams, we can predict the next word given the first word by returning every second
## element where the first element matches the condition...
condition = "the"
nextWords = [bigram[1] for bigram in bigrams if bigram[0].lower() == condition]
## Displays all of the words that are shown to possibly follow the 'condition'
print(nextWords)

## Conditional frequency distriubtion (AKA: finding the word that occured the most often
## after a condition in the corpus)
## Import 'defaultdict', a container similar to the usual dictionary container, but instead
## it has a default value if that key hasn't been set yet.
from collections import defaultdict
cfd = defaultdict(lambda: defaultdict(lambda: 0))
for x in range(len(tokenizedCorpus) - 2):
	cfd[tokenizedCorpus[x].lower()][tokenizedCorpus[x+1].lower()]+= 1
## Print the results for what is most likely to follow what & in how many iterations
print({k: dict(v) for k, v in dict(cfd).items()})
## Discovering the most likely word (ex: to follow 'the')
print(max(cfd["the"])) ## Print results as "quick"
priUnderstanding how tokenize w/out punctuation: https://stackoverflow.com/questions/15547409/how-to-get-rid-of-punctuation-using-nltk-tokenizernt()
##

## Generating random text
## For the purpose of this example, we're going to use a text already included in NLTK.
## To do this, we need to open Terminal and download 'gutenberg' (a project dedicated to assemply
## of corpora). After doing so, the followering should work...
TEXT = nltk.corpus.gutenberg.words("austen-emma.txt")
## NLTK actually has the 'bigrams' function included in its library already, so we'll use that
bigrams = nltk.bigrams(TEXT)
## NLTK also has 'conditional frequency distribution' included too
cfd = nltk.ConditionalFreqDist(bigrams)
## We're gonna pick a random word to start our text generation with
randomWord = random.choice(TEXT)
## And now fifteen more words to come after that which our program deems as 'statistically likely'
## to follow the OG word
fifteenWords = []
for x in range(0, 15):
	print(randomWord)
	fifteenWords.append(randomWord)
	if (randomWord in cfd):
		## Re-assigning variable 'randomWord' to become a random following word f/ 'cfd'
		randomWord = random.choice(list(cfd[randomWord].keys()))
	else:
		break
print()
print(*fifteenWords)
print()

## Counting syllables
## Import libraries, including 'cmudict' (CMU Pronouncing Dictionary--helps w/ rhyming)
## Need to install/download 'cmudict'
import string
from nltk.corpus import cmudict
cmu = cmudict.dict()
## New method built to count syllables
def countSyllables(word):
	lowerWord = word.lower()
	if lowerWord in cmu:
		## If the word is in 'cmu' then return the number of syllables
		return max([len([y for y in x if y[-1] in string.digits]) for x in cmu[lowerWord]])
## Print the number of syllables associated w/ each word
print("poet:", countSyllables("poet"))
print("does:", countSyllables("does"))
print("caterwaul:", countSyllables("caterwaul"))
print()

## Syntax-aware generation with NLTK syntax trees












