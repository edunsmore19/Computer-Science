## In_Class_Monte_Carlo_Simulation
## January 11, 2019
## Monte Carlo simulation figuring out the average calories consumed at a series of holiday
## parties.

import random, math
import matplotlib.pyplot as plt

global totalCalories
totalCalories = 0

trials = 1000

results = []

## Calculate the number of parties you're going to
def parties():
	global numParties
	numParties = random.randint(0, 9)
	print("Number of parties:", numParties)
	## Redirect to 'servings'
	servings()

## Calculate the number of servings
def servings():
	for x in range(0, numParties):
		global numServings
		numServings = random.randint(1, 31)
		print("Number of servings:", numServings)
		## Redirect to 'calories'
		calories()

## Calculate the number of calories per serving
def calories():
	for x in range(0, numServings):
		global numCalories
		numCalories = random.randint(50, 501)
		print("Number of calories per serving:", numCalories)

		## Add to total
		global totalCalories
		totalCalories+= numCalories

		## Plot on graph
		results.append(totalCalories)

for i in range(len(results)):
	display[results[i]] += 1

r = [x for x in range(0, 1000)]
plt.plot(r, display, 'r--')


## Run simulation
#for x in range(0, trials):
#	parties()

#print("\n\nNumber of calories total:", totalCalories)




## Append the 'result' of the function to the 'results list'
## use this display function:

#display = [0 for i in range(11)]
#for i in range(len(results)):
#	display[results[i]] += 1
#
#r = [x for x in range(5, 16)]
#d = [x for x in range(5, 16)]
