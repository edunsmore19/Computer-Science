## Homework_Challenge_Questions_2
## September 27, 2018
## Generate a list of 100 3-digit numbers, exctract the first 
## digit from each number, arrange in ascending order.
## Sources: Did some research on printing list positions

import random

list = []

## Generate the 100 random 3 digit numbers
for x in range(100):
	list += [random.randint(100, 1001)]
## Test print
print(list)

## Take the first digit from each number
for listPosition in range(len(list)):
	list[listPosition] = str(list[listPosition])
	list[listPosition] = (list[listPosition][0])

## Final print
print(list)