## Class_Work_Continuously_Compounding
## September 14, 2018
## Program that calculates & writes the amount of money you'd have if you
## invested it and it had continuously compounded interest.

import sys
import math

## Initialize variables
principal = eval(sys.argv[1])
rate = eval(sys.argv[2])
time = eval(sys.argv[3])
moneyTotal = 0

## Compute equation
moneyTotal = principal * (math.e ** (rate * time))
moneyTotal = round(moneyTotal * 100) / 100
print("Your money after", time, "years is:    ", moneyTotal)