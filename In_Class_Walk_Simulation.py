## In_Class_Walk_Simulation
## January 9, 2019
## Making the computer take a randomly generated walk and then calculating the number of
## blocks it is now away from its starting point (home).

import random
import matplotlib.pyplot as plt

howManyTrials = 1000
howManyBlocks = 22
home = [0, 0]
xWalk = 0
yWalk = 0
currentLocation = [0, 0]
distance = 0
walkHome = 0
getBus = 0

for x in range(0, howManyTrials):
	print()
	## Refresh variables
	xWalk = 0
	yWalk = 0
	currentLocation = [0, 0]
	distance = 0
	## Take the computer for a walk
	for y in range(0, howManyBlocks):
		## Begin simulation
		xWalk, yWalk = random.choice([(-1, 0), (1, 0), (0, -1), (0, 1)])
		## Update 'currentLocation'
		print("xWalk: ", xWalk)
		print("yWalk: ", yWalk)
		currentLocation[0] += xWalk
		currentLocation[1] += yWalk
		print("Your current location is: ", currentLocation)


		## Calculate distance
		if (currentLocation[0] <= 0):
			if (currentLocation[1] <= 0):
				distance = (-1 * currentLocation[0]) + (-1 * currentLocation[1])
			else:
				distance = (-1 * currentLocation[0]) + currentLocation[1]
		else:
				if (currentLocation[1] <= 0):
					distance = currentLocation[0] + (-1 * currentLocation[1])
				else:
					distance = currentLocation[0] + currentLocation[1]

		print("You are", distance, "blocks away from your home.")

		## Can the computer walk home?
		if (distance <= 4):
			print("You can walk home.")
			walkHome+= 1
		else:
			print("You cannot walk home.")
			getBus+= 1
print()
print("You can walk home:", str((walkHome/220)), "percent of the time")
print("You have to get the bus:", str((getBus/220)), "percent of the time")
		