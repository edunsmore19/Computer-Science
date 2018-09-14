## Homework_What_Week_Was_Date
## September 12, 2018
## Program that accepts a date as an input and writes the day of the week
## on which the date falls.

import sys

## Initialize variables
month = int(sys.argv[1])
day = int(sys.argv[2])
year = int(sys.argv[3])

## Compute date
y = year - (14 - month)//12
##y = round(y)
x = y + int(y/4 - y/100 + y/400)
##x = int(x)
m = month + int(12*((14-month)//12)) - 2
##m = round(m)
d = ((day + x + (31*m)//12)) % 7
##d = round(d)

## Output
print(y, x, m, d)
if d == 0:
	print("This date took place on a Sunday")
if d == 1:
	print("This date took place on a Monday")
if d == 2:
	print("This date took place on a Tuesday")
if d == 3:
	print("This date took place on a Wednesday")
if d == 4:
	print("This date took place on a Thursday")
if d == 5:
	print("This date took place on a Friday")
if d == 6:
	print("This date took place on a Saturday")