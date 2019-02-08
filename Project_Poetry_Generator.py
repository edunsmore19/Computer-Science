## Project_Poetry_Generator
## February 8, 2019
## A program that randomly generates poetry
## Sources:
## The basics behind random text prediction: https://www.hallada.net/2017/07/11/generating-random-poems-with-python.html
## Pledge:
## I have neither given nor recieved any unauthorized aid.

## Import libraries
import nltk

## Begin with 'corpus' (the text our generator will blend & shake up)
corpus = "The quick brown fox jumps over the lazy dog"

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
