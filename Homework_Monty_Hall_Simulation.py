## Homework_Monty_Hall_Simulation
## January 8, 2018
## Create a Monty Hall simulation

## Thoughts: It's always better to switch your door. When you first choose your door, 
## you have a 1/3 chance of selecting the one with a car behind it. After a door holding
## a penny is revealed, it is then eliminated. If you switch your choice, you have a 1/2
## chance of selecting the car, but if you stay with your original choice, your likelihood
## of choosing the car remains at a 1/3 chance.

import random
car = 0

probability = 0

iChoose = 0
montyChooses = 0
iChooseTwice = 0

## If you do not switch
for x in range(0, 1000):
	car = random.choice([1, 2, 3])
	print(car)

	iChoose = random.choice([1, 2, 3])
	print(iChoose)

	if (iChoose == car):
		print("You Win!")
		probability+= 1
	else:
		print("Oh no... a goat!")

print("The probability of you winning: ", probability/1000)

car = 0
door1 = 1
door2 = 2
door3 = 3

probability = 0

iChoose = 0
montyChooses = 0

## If you DO switch
for x in range(0, 1000):
	iChooseTwice = 0
	print()
	car = random.choice([1, 2, 3])
	print("Car is behind: ", car)

	iChoose = random.choice([1, 2, 3])
	print("I choose: ", iChoose)

	if (door1 == car):
		if (iChoose == 2):
			montyChooses = 3
			print("Door ", montyChooses, " has a goat behind it.")
			print("You switch your choice.")
		else:
			montyChooses = 2
			print("Door ", montyChooses, " has a goat behind it.")
			print("You switch your choice.")
	elif (door2 == car):
		if (iChoose == 1):
			montyChooses = 3
			print("Door ", montyChooses, " has a goat behind it.")
			print("You switch your choice.")
		else:
			montyChooses = 1
			print("Door ", montyChooses, " has a goat behind it.")
			print("You switch your choice.")
	else:
		if (iChoose == 1):
			montyChooses = 2
			print("Door ", montyChooses, " has a goat behind it.")
			print("You switch your choice.")
		else:
			montyChooses = 1
			print("Door ", montyChooses, " has a goat behind it.")
			print("You switch your choice.")
#
	iChooseTwice = 6 - montyChooses - iChoose
	print("I choose again:", iChooseTwice)

	if (iChooseTwice == car):
		print("You Win!")
		probability+= 1
	else:
		print("Oh no... a goat!")

print("The probability of you winning: ", probability/1000)


## So, turns out its actually a 2/3 chance of guessing correctly if you change your door.
## You have a 1/3 chance of choosing the car in the first simulation, but in the second
## simulation, you have a 2/3 chance of choosing a door without the car, so when Monty
## opens a door to reveal a goat, switching your door makes it more likely that you 
## then choose a car (as you likely chose a goat). There is a 2/6 probability of losing
## when you switch (and thats only if you choose the car correctly on the first go).


