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

	## Allows the user to access their backpack
	def backpack(self, addToInventory):
		self.addToInventory = addToInventory
		inventory.append(addToInventory)
		self.inventory = inventory
		
## Initialize variables
name = ""
gold = 0
inventory = []
cost = 0
boon = 0
roomOneCompleted = False

## Welcome screen & query username
def welcomeScreen():
	print("\nYou wake up, disoriented and confused. You jolt up out of your makeshift bed and " + 
	"your head immediately begins to swim.")
	name = input("You think: \u001b[7m Who am I? \u001b[0m \n")
	player = Player(name)
	print("\nAh yes, your name is", player.name + ".")
	## Redirect to 'roomOne'
	roomOne()

def roomOne():
	global choice
	choice = input("\nYou look around the dark room. Watery sunlight filters in from between the " + 
	"wooden slats nailed to the \u001b[7m window. \u001b[0m The only \u001b[7m door \u001b[0m is " +
	"barricaded with a \u001b[7m dresser. \u001b[0m By your head is your \u001b[7m backpack. \u001b[0m\n")
	## Creates a list of interactive nouns
	global nouns
	nouns = ["window", "door", "dresser", "backpack"]
	## Creates a list of interactive characters
	global characters
	characters = []
	## Redirect to parse to figure out what the user is actually asking to do
	parse()

## Outcomes for choices made in 'roomOne'
def roomOneChoices():
	if (thing == "window"):
		if (action == "talk to") or (action == "give") or (action == "show") or (action == "take")
		or (action == "buy") or (action == "eat") or (action == "drink") or (action == "drop")
		or (action == "turn"):
			print("\nWhy would you want to do that?")
			## Prompt user to input new commands that make more sence
			global choice
			choice = input()
			parse()
		elif (action == "look at"):
		elif (action == "open"):
		elif (action == "push"):
		elif (action == "feel"):
		elif (action == "unknown"):



	#elif (thing == "door")
	#elif (thing == "dresser")
	#elif (thing == "backpack")
	#elif (thing == "unknown")

## Cut up & parse meaning from user input
def parse():
	global choice
	choice = choice.lower()
	## Figure out the action
	global action
	if (choice.find("talk to") != (-1)):
		action = "talk to"
	elif (choice.find("give") != (-1)):
		action = "give"
	elif (choice.find("show") != (-1)):
		action = "show"
	elif (choice.find("look at") != (-1)):
		action = "look at"
	elif (choice.find("take") != (-1)):
		action = "take"
	elif (choice.find("drop") != (-1)):
		action = "drop"
	elif (choice.find("open") != (-1)):
		action = "open"
	elif (choice.find("push") != (-1)):
		action = "push"
	elif (choice.find("turn") != (-1)):
		action = "turn"
	elif (choice.find("feel") != (-1)):
		action = "feel"
	elif (choice.find("eat") != (-1)):
		action = "eat"
	elif (choice.find("drink") != (-1)):
		action = "drink"
	else:
		action = "unknown"
	## Figure out the noun
	foundANoun = False
	for x in range(len(nouns)):
		if (choice.find(nouns[x]) != (-1)):
			global thing
			thing = nouns[x]
			foundANoun = True
		elif (choice.find(nouns[x]) == (-1)) and (foundANoun == False):
			thing = "unknown"
	## Figure out if any characters are being referenced
	foundAPerson = False
	for x in range(len(characters)):
		if (choice.find(characters[x]) != (-1)):
			global person
			person = characters[x]
			foundAPerson = True
		elif (choice.find(characters[x]) == (-1)) and (foundAPerson == False) :
			person = "unknown"
	if (len(characters) == 0):
		person = "none"


	## TEMP CODE
	print("\n\n\nYou want to:", action)
	print("With the:", thing)
	print("With the person:", person)
	## TEMP CODE ENDS

	## Redirect to 'roomOneChoices' if 'roomOne' hasn't been completed yet
	if (roomOneCompleted == False):
		roomOneChoices()


## Begin program
welcomeScreen()