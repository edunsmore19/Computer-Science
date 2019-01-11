## Homework_Monte_Carlo_Walk_Simulation
## January 10, 2019
## Response discussing the Monte Carlo simulation and a dart
## program.

## Response:
## The longest walk you can take where you'll be within walking
## distance of home at least 50% of the time is 22 blocks. By
## randomly generating the direction of the computer (N, E, W, S)
## and having the computer run the simulation 10000 times with X
## number of blocks and printing amount of blocks the computer
## is away from home. If the distance is less than or equal to
## four, the number of random walks that end with a walk home can
## made into a percent (walksHome/numberOfWalks). The longest
## walk with a greater than 50% chance of walking home is 22.

## Monte Carlo simulations are a technique used to understand the
## impact of risk and uncertainty in prediction and forecasting
## models. They're used in finance, supply chain, engineering,
## and science. (AKA: It's a probability simulation.)
## They work by building models of possible results by subsituting
## a range of values for any factor that has inherent uncertainty.
## (In the case above: the distance from home due to randomly
## generated block directions.) It then calculates the results
## many times, each time using a different set of random values.

## Dart program
import random, math

global x, y
x, y = 0, 0
numberOfDarts = 100000
landedInCircle = 0
whatDoYouGet = 0

def throwDart():
	global x, y
	x = random.uniform(-1.0, 1.0)
	y = random.uniform(-1.0, 1.0)
	print(x, y)
	
for a in range(0, numberOfDarts + 1):
	print("Trial:", a)
	throwDart()

	## Landed in circle?
	if (x**2 + y**2 <= 1.0):
		landedInCircle+= 1

## Calculate 'whatDoYouGet'
whatDoYouGet = (landedInCircle * 4) / numberOfDarts
print(whatDoYouGet)
print(math.pi)

## Answer:
## You get Pi!
