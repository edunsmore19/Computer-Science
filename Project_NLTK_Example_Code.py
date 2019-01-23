## Project_NLTK_Example_Code
## January 22, 2019
## Example code using NLTK, to be used to framiliarize myself & explain the uses of the library
## in the book.

## Installing NLTK sourse:
# http://ling-blogs.bu.edu/lx390f16/2016/09/07/installing-nltk-on-mac-os-x/

## Learning about NLTK sourse:
# https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk

## Importing NLTK
import nltk

## If you get certificate errors, then check out this stack overflow entry
# https://stackoverflow.com/questions/41348621/ssl-error-downloading-nltk-data/42890688#42890688
## I ended up installing certificates by finding this: /Applications/Python 3.7/Install Certificates.command
## and then double clicking it to run & install it

## If that doesn't work for you, you can use this code:
#########
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#########
## as a way to bypass this error. I don't understand how any of those things work or what any of
## those things do, but... it allowed my program to execute, so, oh well.

## Tokenization
## Sentence tokenization
from nltk.tokenize import sent_tokenize as sent
exampleText = "I love birds and mice. I love blankets. I love kittens."
tokenized_text = sent(exampleText)
print(tokenized_text)
## Word tokenization
from nltk.tokenize import word_tokenize as word
tokenized_word = word(exampleText)
print(tokenized_word)

## Frequency Distribution (utilizing matplotlib)
from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print(fdist)
## Convert the info to a more sense-making thing, explaining the 2 most common words & number of
## times they occur
print(fdist.most_common(2))
## Creating a frequency distribution plot
import matplotlib.pyplot as plt
######
#fdist.plot(30, cumulative = False)
#plt.show()
######

## Stopwords
## Stopwords are text noise (ex: is, am, this, a, an, the), you can use NLTK to remove stopwords
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
## These are all of the stopwords nltk includes in the english language
######
# print(stop_words)
######
## Here's how to remove them from your text:
## Utilize an already tokenized set of sentences broken down into words to do this we're going
## to learn how to access text from the web & from disk
## Reading local files, make sure .txt file is saved in the file you're already accessing
#
flowerHead = open('Flower Head.txt')
print(flowerHead)
## Tokenize 'Flower Head' into words
tokenized_word = word(flowerHead.read())
## Create a new list for filtered sentences
filtered_word = []

for x in tokenized_word:
	if x not in stop_words:
		filtered_word.append(x)
print("Tokenized Sentences:", tokenized_word)
print("Filtered Sentence:", filtered_word)

## Lexicon Normaliation
## Cuts down on another kind of noise that reduces devitionally related forms of a word to a 
## common root word
## Stemming (reducing words to their root word/chops off derivational affixes)
from nltk.stem import PorterStemmer

ps = PorterStemmer()
## Example text:
someText = "She wanted to cancel the trip. She canceled by calling on the phone."
## Filter words
tokenized_word = word(someText)
## Create a new list
stemmed_words = []

for x in tokenized_word:
	stemmed_words.append(ps.stem(x))
print("Filtered Sentence:", tokenized_word)
print("Stemmed Sentence:", stemmed_words)

## Part of Speech Tagging




