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
	global thing
	global action
	## Prints error message if there is no known 'thing' being interacted with
	unknownThing()
	if (thing == "window"):
		## Prints error message if there is no known 'action' being done
		unknownAction()
		if (action == "talk to") or (action == "give") or (action == "show") or (action == "take") or (action == "buy") or (action == "eat") or (action == "drink"):
			why()
		## Print approach line
		else:
			print("\nYou approach the boarded up window.")
		## Valid story choices
		if (action == "look at"):
			print("The wood is old and dry, and you can just barely peer through. You realize " +
			"you are on the second floor of a building. Outside, you see a barren, decaying " +
			"cityscape. The streets are empty of people and animals.")
			print("As you stare at the skeleton of what might have long ago been a skyscraper, you " +
			"see movement out of the corner of your eye. There is a man stumbling out of an alley " +
			"into the street. He moves slowly, dragging his bad leg behind him seemingly without " +
			"care or any indication of pain. You watch him continue to amble down the street until " +
			"he is only a couple of yards away from the building you're in. It's then that you notice " +
			"the bluish-green tinge of his flesh and the several rotting, open wounds covering his " +
			"body.")
			print("You realize: He's a zombie.")
			print("You retreat from the window.")
			## Prompt user to continue exploring the room
			choice = input()
			parse()
		elif (action == "open"):
			print("You realize that the window has no glass in it and that the wooden boards " +
			"nailed into frame are the only thing between you and the street two stories below.")
			print("You decide you no longer want to open the window.")
			choice = input()
			parse()
		elif (action == "push"):
			print("You realize that the window has no glass in it and that the wooden boards " +
			"nailed into frame are the only thing between you and the street two stories below.")
			print("You decide you no longer want to try pushing on the boards covering the window.")
		elif (action == "feel"):
			print("You run your hand over the dry, old wood covering the window.")
			print("You discover the wood has splinters.")
			choice = input()
			parse()

	elif (thing == "backpack"):
		unknownAction()
		if (action == "talk to") or (action == "give") or (action == "show") or (action == "buy") or (action == "eat") or (action == "drink"):
			why()
		## Print approach line
		else:
			print("\nYou approach the backpack.")
		## Valid story choices
		if (action == "look at"):
			print("You look at the slightly worn backpack. It's a navy blue color and has your name, " +
			player.name + " stitched into the back in uneven grey thread. It looks usable, but empty.")
			print("Maybe it woulf be a good idea to take it?")
		elif (action == "take"):
			print("You pick the backpack up off the ground and swing it onto one shoulder. It feels " +
			"comfortable, and empty.")
		elif (action == "open"):
			print("You kneel down and unzip the backpack carefully. You peer inside and see that it " +
			"is empty.")
			print("Maybe you could use it to carry things?")
		elif (action == "push"):
			print("You nudge the backpack with your toe.")
			print("It shifts several inches.")
		elif (action == "feel"):
			print("You kneel down and run a hand over the tough navy canvas backpack. It feels, " +
			"rough to the touch, but strong. You ghost your fingers over your name, " + player.name +
			" stitched into the canvas. The thread is slightly worn and was probably once white but " +
			"it's now turned a greyish color.")
			print("The backpack is empty right now, but it could carry a lot you surmise.")







	#elif (thing == "dresser"):

#	elif (thing == "door"):
#		unknownAction()
#		if (action == "talk to") or (action == "give") or (action == "show") or (action == "take") or (action == "buy") or (action == "eat") or (action == "drink"):
#			why()
#		## Print approach line
#	else:
#		print("\nYou approach ")

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
	elif (choice.find("open") != (-1)):
		action = "open"
	elif (choice.find("push") != (-1)):
		action = "push"
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

## Error message for when the user inputs an action that is unknown
def unknownAction():
	if (action == "unknown"):
		print("\nYou don't know how to do that.")
		print("Try commands like: 'talk to', 'give to', 'show to', 'look at', 'take', " +
		"'open', 'push', 'feel', 'buy', 'eat', or 'drink'.")
		global choice
		choice = input()
		parse()

## Error message for when the user inputs a thing that is unknown
def unknownThing():
	if (thing == "unknown"):
		print("\nYou don't see or can't interact with that object.")
		print("Try an object that is highlighted in the room description.")
		global choice
		choice = input()
		parse()

## Error message for when the user inputs a person that is unknown
def unknownPerson():
	if (thing == "unknown"):
		print("\nWho is that person?")
		print("Try someone whose name is highlighted.")
		global choice
		choice = input()
		parse()
## Error message for when the user is trying to do weird things
def why():
	print("\nWhy would you want to do that?")
	## Prompt user to input new commands that make more sense
	global choice
	choice = input()
	parse()

## Begin program
welcomeScreen()