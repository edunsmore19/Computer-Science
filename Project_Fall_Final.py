## Project_Fall_Final
## November 2, 2018
## Honor Code: I have neither given nor recieved any unauthorized aid.
## Sources:
## Learning to edit text colors
## http://www.lihaoyi.com/post/BuildyourownCommandLinewithANSIescapecodes.html#colors
## A text based game in which the user can decide how to move forward utilizing a litany of
## commands.

class Player:
	def __init__(self, name):
		self.name = name
		self.gold = gold
		## Establish an inventory list to keep track of the player's stuff
		self.inventory = inventory

	## Allows the user to spend gold
	def spendGold(self):
		status = ""
		## If the user has enough money, allow them to purchase
		if (self.gold - cost > 0):
			self.gold-= cost
			print("You have just purchased", item + ("."))
		## If the user doesn't have enough money, do not allow them to purchase
		elif (self.gold - cost < 0):
			print("You don't have enough money to purchase", item + ("."))

	## Allows the user to gain gold
	def gainGold(self):
		self.gold+= boon
		print("You have just added,", boon + ("to your account."))
		print("You now have", self.gold, "gold.")

	## Actions
	#def actions(self):
		

## Initialize variables
name = ""
gold = 0
inventory = ["knife", "matches", "book", "map"]
cost = 0
boon = 0


## Welcome screen & query username
def welcomeScreen():
	print("\nYou wake up, disoriented and confused. You jolt up out of your makeshift bed and " + 
	"your head immediately begins to swim.")
	name = input("You think: \u001b[7m Who am I? \u001b[0m \n")
	player = Player(name)
	print("\nAh yes, your name is", player.name + ".")
	global choice
	choice = input("You look around the dark room. Watery sunlight filters in from between the " + 
	"wooden slats nailed to the \u001b[7m window. \u001b[0m The only \u001b[7m door \u001b[0m is " +
	"barricaded with a \u001b[7m dresser. \u001b[0m By your head is your \u001b[7m backpack. \u001b[0m\n")
	## Creates a list of interactive nouns
	global nouns
	nouns = ["window", "door", "dresser", "backpack"]
	## Redirect to parse to figure out what the user is actually asking to do
	parse()

## Cut up & parse meaning from user input
def parse():
	global choice
	choice = choice.lower
	## Figure out the action
	if (choice.find("talk to") != (-1)):
		global actions
		action = "talk to"
	## Figure out the noun
	print(len(nouns))
	for x in range(len(nouns)):
		if (choice.find(nouns[x]) != (-1)):
			global thing
			thing = nouns[x]
	## TEMP CODE
	print("You want to:", action)
	print("With the:", thing)
	## TEMP CODE ENDS


## Begin program
welcomeScreen()