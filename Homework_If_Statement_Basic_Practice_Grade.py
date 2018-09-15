## Homework_If_Statement_Basic_Practice_Grade
## September 15, 2018
## Program that accepts a float between 0 and 5 from the command 
## argument & then determines their grade in the class using the scale.

import sys

## Initialize variables
input = eval(sys.argv[1])
letterGrade = " "
sign = " "

## Determine if 'input' is between 0 & 5
## Assign variables 'sign' and 'letterGrade'
if (0 <= input <= 5):
	if (4.5 <= input):
		letterGrade = "A"
		if (4.85 <= input):
			sign = "+"
		elif (input < 4.7):
			sign = "-"
	elif (3.5 <= input <= 4.5):
		letterGrade = "B"
		if (4.2 <= input):
			sign = "+"
		elif (input < 3.85):
			sign = "-"
	elif (2.5 <= input <= 3.5):
		letterGrade = "C"
		if (3.2 <= input):
			sign = "+"
		elif (input < 2.85):
			sign = "-"
	else:
		letterGrade = "D"
		if (2 <= input):
			sign = "+"
		elif (input < 1.5):
			sign = "-"
	## Print grade
	print("Your grade is:", letterGrade + sign)
	
else:
	print("Number is not in range.\nUse a number from zero to five.")