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

### If that doesn't work for you, you can use this code:
##########
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
##########
## as a way to bypass this error. I don't understand how any of those things work or what any of
## those things do, but... it allowed my program to execute, so, oh well.

## Tokenization
## Sentence tokenization
from nltk.tokenize import sent_tokenize as sent
exampleText = "Last weekend I delivered a letter to the city council. I complained about my terrible neighbors and their terrible children. I signed it: Sincerely, Brenda."
tokenized_text = sent(exampleText)
print("This is the example text tokenized:")
print(tokenized_text)
print()
print(tokenized_text[0])

print("\n\n\n\n")


## Word tokenization
from nltk.tokenize import word_tokenize as word
tokenized_word = word(exampleText)
print("This is the example text tokenized:")
print(tokenized_word)

print("\n\n\n\n")



## Frequency Distribution (utilizing matplotlib)
from nltk.probability import FreqDist
fdist = FreqDist(tokenized_word)
print("The frequency distribution:")
print(fdist)
print("\n\n\n\n\n")
## Convert the info to a more sense-making thing, explaining the 2 most common words & number of
## times they occur
print("The top two most common distributions:")
print(fdist.most_common(2))
print("\n\n\n\n\n")
## Creating a frequency distribution plot
import matplotlib.pyplot as plt
######
#fdist.plot(30, cumulative = False)
#plt.show()
######

## Stopwords, basic
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
#print("Stop words in English:")
#print(stop_words)


print("\n\n\n\n\n\n")
imTokenized = tokenized_word
## Jumping back in…
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
## In order to utilize ‘stopwords’ you must use text that has been tokenized by word
## (refer to above tutorials for answers on how to do that), so for that we’re going
## to use the text we’ve already tokenied: ‘imTokenized’.
## Create a new list for the filtered sentences (sentences w/out stop words)
filtered_words = []
## Use a ‘for’ loop to remove the stop words
for x in imTokenized:
	if x not in stop_words:
		filtered_words.append(x)
## Then print
print("Original:", imTokenized)
print("Filtered:", filtered_words)




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
print("\n\n\n\nFiltered Sentence:", *filtered_word)

print("\n\n\n\n\n\n\n")
print(tokenized_word)

print("\n\n\n\n\n\n\n\n")
## Lexicon Normaliation
## Cuts down on another kind of noise that reduces devitionally related forms of a word to a 
## common root word
## Stemming (reducing words to their root word/chops off derivational affixes)
from nltk.stem import PorterStemmer

ps = PorterStemmer()
## Example text:
someText = "She wanted to cancel the trip. She canceled by calling on the phone and telling the man on the other end about wanting to do so."
## Filter words
tokenized_word = word(someText)
## Create a new list
stemmed_words = []

for x in tokenized_word:
	stemmed_words.append(ps.stem(x))
print("Tokenized Sentence:", tokenized_word)
print("Stemmed Sentence:", stemmed_words)

#############################
## Sentiment Gathering
review = open('Amazon Headphones Review.txt')
## Tokenize by word
tokenizedReview = word(review.read())
## Create a new list for filtering stop words
filtered_words = []

for x in tokenizedReview:
	if x not in stop_words:
		filtered_words.append(x)
## Create a new list for stemming
stemmed_words = []

for x in filtered_words:
	stemmed_words.append(ps.stem(x))
print("\n\n\n\nFiltered Review:\n", *stemmed_words)

## Search for "good-geared words"
goodTally = 0
badTally = 0
unknownTally = 0
for x in range(len(stemmed_words)):
	if (stemmed_words[x] == "good") or (stemmed_words[x] == "nice") or (stemmed_words[x] == "best") or (stemmed_words[x] == "reliabl"):
		goodTally+= 1
	elif (stemmed_words[x] == "bad") or (stemmed_words[x] == "cheap") or (stemmed_words[x] == "terribl"):
		badTally+= 1
	else:
		unknownTally+= 1
## Print
print("\nGood-Sentiment words:", goodTally)
print("Bad-Sentiment words:", badTally)
print("Unknown-Sentiment words:", unknownTally)

