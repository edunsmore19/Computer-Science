## Homework_Challenge_Questions_3
## September 27, 2018
## Generate 30 numbers from 1 to 30, randomly (?) and then print
## only the values that the digit sum equals 5.
## Sources:

import random

list = []
firstList = []
secondList = []
finalList = []

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
##for listPosition in range(len(firstList)):
finalList += firstList[listPosition] + secondList[listPosition]

## Add 5 to the list, bc it equals 5
finalList.append(5)

## Test print
print(finalList)