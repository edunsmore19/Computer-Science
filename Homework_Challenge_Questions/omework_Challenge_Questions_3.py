## Homework_Challenge_Questions_3
## September 27, 2018
## Generate 30 numbers from 1 to 30, randomly (?) and then print
## only the values that the digit sum equals 5.
## Sources: did some research on adding integers from two
## different lists

import random

list = []
firstList = []
secondList = []
finalList = []
stringList = []

## Generate the 30 random numbers 1-30
for x in range(29):
	list += [random.randint(1, 31)]

## Check to see if number is two digit & separate
for listPosition in range(len(list)):
	if (list[listPosition] >= 10):
		list[listPosition] = str(list[listPosition])
		firstList.append(list[listPosition][0])
		secondList.append(list[listPosition][1])
## Convert back to ints
for listPosition in range(len(firstList)):
	firstList[listPosition] = int(firstList[listPosition])
	secondList[listPosition] = int(secondList[listPosition])

## Add together & put back in original finalList
for listPosition in range(len(firstList)):
	finalList = [sum(i) for i in zip(firstList, secondList)]

## Check for it equaling 5
for listPosition in range(len(finalList)):
	if (finalList[listPosition] == 5):
		## add two strings together to equal string list
		stringList = [str(firstList[listPosition]) + str(secondList[listPosition]) for listPosition in range(len(firstList))]
		print(stringList[listPosition])

## Test print
print(5)