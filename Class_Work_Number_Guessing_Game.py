## Class_Work_Number_Guessing_Game
## September 17, 2018
## User gueses secret number, and program returns whether it was too high
## or low until they get the number.

import random

## Initialize variables
theNumber = random.randint(0, 101)

## User query
print(theNumber) ## to delete
guess = int(import("Guess a number"))
if (guess == theNumber):
	"Congrats, you got it."