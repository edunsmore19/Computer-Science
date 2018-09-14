## Homework_Ascending_or_Descending
## September 12, 2018
## Program that takes three floats as command-line arguments & presents either true if
## values are ascending or descending & false if they're not.

import sys

## Initialize variables
x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])
offWithHerHead = 0

## Variable print out
print("X = ", x)
print("Y = ", y)
print("Z = ", z)

##print(type(x))

## Sort numbers
if (x < y < z):
	print("\nTrue\n")
	offWithHerHead = 1

if (x > y > z):
	print("\nTrue\n")
	offWithHerHead = 1

if (offWithHerHead == 0):
	print("\nFalse\n")
