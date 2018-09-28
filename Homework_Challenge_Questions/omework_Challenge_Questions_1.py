## Homework_Challenge_Questions_1
## September 27, 2018
## Generate a list of 10 random numbers between 0 and 100.
## Get them in order from largest to smallest, removing numbers
## divisible by 3.
## Sources: Did some reasearch on list commands

import random

list = []

lopMeOffTheEnd = 0

## Generate the 10 random numbers
for x in range(10):
	list += [random.randint(1, 101)]
## Test print
print(list)

## Delete numbers divisible by 3
for listPosition in range(10):
	if (list[listPosition] % 3 == 0):
		list[listPosition] = 103
		list.remove(103)
		list.append(103)
		lopMeOffTheEnd+= 1
lopMeOffTheEnd = 10 - lopMeOffTheEnd
del list[lopMeOffTheEnd:]

## Order from largest to smallest
sorted(list, key = int, reverse = True)

## Final product print
print(list)