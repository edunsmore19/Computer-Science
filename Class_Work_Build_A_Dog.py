## Class_Work_Build_A_Dog
## October 25, 2018
## Utilizing classes & methods to build a dog.

## You want the class to be flexible, not printing things our or querrying
## user input from within the class.
class Dog:
	## Constructor & things in parentheses are arguments
	def __init__(self, energy, name):
		self.energy = energy
		self.hunger = 5
		self.weight = 30
		self.happiness = 5
		## When the 'dog' constructor is called
		self.name = name

	## Methods (basically just functions, but the difference is that a function
	## isn't in a class V. a method that is in a class.)
	## The 'eat' method is accesing self && because it's part of the 'Dog' class
	## only a DOG can eat. So you have to reference it as myDog.eat()
	def eat(self):
		status = ""
		if (self.hunger > 0):
			self.weight+= 1
			self.hunger-= 1
			self.energy+= 1
			self.happiness+= 1

			status = self.name + " just ate."

			if (self.weight > 40):
				self.happiness-= 3
				status+= "\nFYI, this dog is unhappy because its getting to big."
		else:
			status = "Nope, not eating. Not hungry."
		return status

	## Can exercise dog
	def exercise(self):
		status = ""
		if (self.weight > 20):
			self.weight-= 2
			self.hunger+= 1
			self.energy-= 1
			self.happiness+= 1

			status = self.name + " was just exercised."

		else:
			status = "This dog is too thin. It cannot be exercised."

	## Returns a string that conveys the general stats of the dog
	def stats(self):
		## This returns all of these variables & their value by printing them
		return "\n\nName:" + self.name + "\nHunger:" + str(self.hunger) + "\nEnergy:" + str(self.energy) + "\nHappiness:" + str(self.happiness) + "\nWeight:" + str(self.weight)


## Dog has been created, and his name will be 'Tim', and then passed up to the 
## constructor & 'name' will store 'Tim'--thereafter 'Tim' is stored in the 
## 'name' variable throughout the class. Conclusion: 'Tim' is used whenever
## the 'name' argument is called
myDog = Dog(3, "Tim")
## This creates another dog, & the variable '8' refrences the energy argument,
## Setting the energy variable for the dog.
mySecondDog = Dog(8, "Annabelle")

## Prints the dog stats
print(myDog.stats())

## Gets your dog to eat
print(myDog.eat())
print(myDog.eat())
print(myDog.eat())
print(myDog.eat())
print(myDog.exercise())
print(myDog.eat())
print(myDog.eat())
print(myDog.stats())