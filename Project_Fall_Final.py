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
		## Establish an inventory list to keep track of the player's stuff
		self.inventory = inventory

	## Allows the user to access their backpack
	def backpack(self, addToInventory):
		self.addToInventory = addToInventory
		inventory.append(addToInventory)
		self.inventory = inventory
		print("You now have the", addToInventory + ".")
		
## Initialize variables
name = ""
gold = 0
inventory = []
global roomOneCompleted
roomOneCompleted = False
global backpackTaken
backpackTaken = False
global backpackPretend
backpackPretend = ["Inside the backpack you have:"]
global dresserOpened
dresserOpened = False
global dresserPushed
dresserPushed = False
global knifeTaken
knifeTaken = False
global pendantTaken
pendantTaken = False
global matchesTaken
matchesTaken = False
global mapTaken
mapTaken = False
global coinsTaken
coinsTaken = False

## Welcome screen & query username
def welcomeScreen():
	print("\nYou wake up, disoriented and confused. You jolt up out of your makeshift bed and", 
	"your head immediately begins to swim.")
	name = input("You think: \u001b[7m Who am I? \u001b[0m \n")
	global player
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
	## Reminding program of globals
	global choice
	global thing
	global action
	global backpackTaken
	global backpackPretend
	backpackPretend = ["Inside the backpack you have:"]
	global dresserOpened
	global dresserPushed
	global knifeTaken
	global pendantTaken
	global matchesTaken
	global mapTaken
	global coinsTaken
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
			print("The wood is old and dry, and you can just barely peer through. You realize",
			"you are on the second floor of a building. Outside, you see a barren, decaying",
			"cityscape. The streets are empty of people and animals.")
			print("As you stare at the skeleton of what might have long ago been a skyscraper, you",
			"see movement out of the corner of your eye. There is a man stumbling out of an alley",
			"into the street. He moves slowly, dragging his bad leg behind him seemingly without",
			"care or any indication of pain. You watch him continue to amble down the street until",
			"he is only a couple of yards away from the building you're in. It's then that you notice",
			"the bluish-green tinge of his flesh and the several rotting, open wounds covering his",
			"body.")
			print("You realize: He's a zombie.")
			print("You retreat from the window.")
			## Prompt user to continue exploring the room
			choice = input()
			parse()
		elif (action == "open"):
			print("You realize that the window has no glass in it and that the wooden boards",
			"nailed into the frame are the only thing between you and the street two stories below.")
			print("You decide you no longer want to open the window.")
			choice = input()
			parse()
		elif (action == "push"):
			print("You realize that the window has no glass in it and that the wooden boards",
			"nailed into the frame are the only thing between you and the street two stories below.")
			print("You decide you no longer want to try pushing on the boards covering the window.")
			choice = input()
			parse()
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
			## You can't 'approach the backpack' if you've taken it, so T/F
			if (backpackTaken == False):
				print("\nYou approach the backpack.")
			else:
				print()
		## Valid story choices
		if (action == "look at"):
			## It can't be 'usable but empty' if it's got stuff in it, so T/F
			if (len(player.inventory) == 0):
				print("You look at the slightly worn backpack. It's a navy blue color and has your name,",
				player.name, "stitched into the back in uneven grey thread. It looks usable, but empty.")
				print("Maybe it would be a good idea to take it?")
			else:
				print("You look at the slightly worn backpack. It's a navy blue color and has your",
				"name,", player.name, "stitched into the back in unever grey thread.")
			choice = input()
			parse()
		elif (action == "take"):
			## You can't take the backpack more than once, so T/F
			if (backpackTaken == True):
				print("You have already taken the backpack.")
				print("Maybe you wanted to see what was inside it?")
			if (backpackTaken == False):
				print("You pick the backpack up off the ground and swing it onto one shoulder. It feels",
				"comfortable, and empty.")
				if (backpackTaken == False):
					## Add backpack to inventory
					player.backpack("backpack")
					## Backpack has now been taken, set variable to 'true'
					backpackTaken = True
			choice = input()
			parse()
		elif (action == "open"):
			## Allows user to access inventory once they have both taken the backpack & another
			## object (not the backpack)
			if (backpackTaken == True) and (len(player.inventory) != 0):
				for x in range(len(player.inventory)):
					backpackPretend.append("\u001b[7m")
					if (x != 0):
						backpackPretend.append(player.inventory[x])
						if (x != (len(player.inventory)-1)):
							backpackPretend.append("\u001b[0m and ")
						else:
							backpackPretend.append("\u001b[0m")
				print(*backpackPretend)
			else:
				print("You kneel down and unzip the backpack carefully. You peer inside and see that it",
				"is empty.")
				print("Maybe you could use it to carry things?")
			choice = input()
			parse()
		elif (action == "push"):
			## You can't 'nudge the backpack with your toe' if you're wearing it, so T/F
			if (backpackTaken == False):
				print("You nudge the backpack with your toe.")
				print("It shifts several inches.")
			else:
				print("You're wearing the backpack. \nHow do you expect it to be pushed?")
			choice = input()
			parse()
		elif (action == "feel"):
			## You can't 'kneel down' if you're wearing it, so T/F
			if (backpackTaken == False):
				print("You kneel down and run a hand over the tough navy canvas backpack. It feels,",
				"rough to the touch, but strong. You ghost your fingers over your name,", player.name,
				"stitched into the canvas. The thread is slightly worn and was probably once white but",
				"it's now turned a greyish color.")
				print("The backpack is empty right now, but you surmise it could carry a lot.")
			else:
				print("You reach awkwardly around and run a hand over the tough navy canvas backpack. It feels,",
				"rough to the touch, but strong. You ghost your fingers over your name,", player.name,
				"stitched into the canvas. The thread is slightly worn and was probably once white but",
				"it's now turned a greyish color.")
			choice = input()
			parse()

	elif (thing == "dresser"):
		unknownAction()
		if (action == "talk to") or (action == "give") or (action == "show") or (action == "take") or (action == "buy") or (action == "eat") or (action == "drink"):
			why()
		## Print approach line
		else:
			print("\nYou approach the dresser.")
		## Valid story choices
		if (action == "look at"):
			## The dresser can't be blocking the door if its been pushed, so T/F
			if (dresserPushed == False):
				print("The dresser is wellmade and looks heavy. You notice that the dresser is blocking",
				"the door. You probably won't be able to leave without moving it. You glance down at the",
				"ground and see white scratches on the wooden floor leading to the dresser.")
				print("The dresser also has several drawers... perhaps there's something inside?")
			else:
				print("The dresser is wellmade and looks heavy. You notice that the dresser has been pushed free of",
				"the door.")
				print("The dresser also has several drawers... perhaps there's something inside?")
			choice = input()
			parse()
		elif (action == "open"):
			## Add new items to noun list
			if (dresserOpened == False):
				nouns.append("knife")
				nouns.append("matches")
				nouns.append("pendant")
				nouns.append("map")
				nouns.append("coins")
			## Dresser has now been opened, change variable to 'true'
			dresserOpened = True
			## Make sure you only see the items that are still inside the dresser, so T/F
			if (knifeTaken == False):
				print("You pull on one of the dresser drawer's knobs. It opens smoothly and you see a",
				"\u001b[7m knife \u001b[0m. It looks like it's meant for hunting, and it has a sheath.",
				"It also looks sharp.")
			if (matchesTaken == False):
				print("You pull open another drawer. You see a set of \u001b[7m matches \u001b[0m.")
			if (pendantTaken == False):
				print(" You also see a \u001b[7m pendant \u001b[0m made of raw pyrite with strange symbols carved into it,",
				"hung from a leather cord.")
			if (mapTaken == False):
				print("You open the last drawer. Inside is a paper \u001b[7m map \u001b[0m.")
			if (coinsTaken == False):
				print("Also inside the last drawer is a stack of ten gold \u001b[7m coins \u001b[0m.")
			if (knifeTaken) and (matchesTaken) and (pendantTaken) and (mapTaken) and (coinsTaken):
				print("The contents of the dresser have been emptied. There is nothing inside the drawers.")
			choice = input()
			parse()
		elif (action == "push"):
			## You can only push the dresser once, so T/F
			if (dresserPushed == False):
				print("You walk to the side of the dresser and put your hands on the solid wood before",
				"steeling yourself and giving it a gigantic shove. The dresser scrapes heavily against",
				"the floor, but eventually you move it clear of the door.")
			else:
				print("You have already pushed the dresser as far as it will go.")
			## Dresser has now been pushed, change variable to 'true'
			dresserPushed = True
			choice = input()
			parse()
		elif (action == "feel"):
			print("You run your hand over the solid surface of the dresser. It feels expensive,",
			"if disused. The wood is smooth with no imperfections.")
			choice = input()
			parse()

	elif (thing == "door"):
		unknownAction()
		if (action == "talk to") or (action == "give") or (action == "show") or (action == "take") or (action == "push") or (action == "buy") or (action == "eat") or (action == "drink"):
			why()
		## Print approach line
		else:
			print("\nYou approach the door.")
		## Valid story choices
		if (action == "look at"):
			## If dresser has been moved, it cannot obstruct door, so T/F
			if (dresserPushed == False):
				print("The door is obstructed by the dresser. It looks as if you won't be able to",
				"open it with the dresser where it is.")
			print("It's made of wood and it looks fairly sturdy. It's also the only way out.")
			choice = input()
			parse()
		elif (action == "open"):
			if (dresserPushed == True):
				if (knifeTaken == True):
					if (mapTaken == True):
						## Redirect to 'roomTwo' and set 'roomOneCompleted' to True
						print("You open the door cautiously, and it creaks slightly. You're going",
						"to try and find others. You glance at the map. Maybe there are people hiding",
						"in the Trebond Mines? You don't know, but you decide that you'll try there",
						"first.")
						roomOneCompleted = True
						roomTwo()
					else:
						print("You could open the door and leave, but you don't know where you're",
						"going.")
						choice = input()
						parse()
				else:
					print("You could open the door and leave, but what if you're attacked? How will",
					"you protect yourself?")
					choice = input()
					parse()
			else:
				print("You can't open the door, it's being obstructed by the dresser.")
				choice = input()
				parse()
		elif (action == "feel"):
			print("You press a palm to the door. The wood feels slightly warm, but not alarmingly so.",
			"The wood is smooth and textured.")
			choice = input()
			parse()

	## Secondary object actions
	if (dresserOpened == True):
		if (thing == "knife"):
			unknownAction()
			if (action == "talk to") or (action == "give") or (action == "show") or (action == "buy") or (action == "eat") or (action == "drink"):
				why()
			## Print approach line
			else:
				if (knifeTaken == False):
					print("\nInside the dresser is a knife.")
			## Valid story choices
			if (action == "look at"):
				if (knifeTaken == False):
					print("You regard the knife carefully. It's a silver hunting knife with a black,",
					"metal handle. It hasn't been properly put away in its sheath, so you can see the",
					"edge of the blade peaking out. It looks deadly.")
					print("The sheath is plain brown leather devoid of patterns or decoration.")
				else:
					print("You regard the knife carefully. It's a silver hunting knife with a black,",
					"metal handle. It looks deadly.")
					print("The sheath is plain brown leather devoid of patterns or decoration.")
				choice = input()
				parse()
			elif (action == "push"):
				if (knifeTaken == False):
					print("You push the knife gingerly a few inches to the left. It's heavier than",
					"it looks.")
				else:
					print("Why would you want to do that?")
				choice = input()
				parse()
			elif (action == "feel"):
				print("You run your fingertips over the sheath. The leather doesn't feel dry or",
				"cracked. Instead, it feels smooth and a little soft.")
				print("You decide it's best that you don't feel the knife. Although the handle",
				"looks well crafted.")
				choice = input()
				parse()
			elif (action == "take"):
				if (backpackTaken == True):
					if (knifeTaken ==False):
						print("Carefully, you pick up the knife and its sheath. You slide the knife",
						"completely into the leather sheath before putting it in your backpack.")
						print("Something tells you that this knife is sharper than it looks and that",
						"you ought to handle it as such.")
					else:
						print("You have already taken the knife.")
					if (knifeTaken == False):
						player.backpack("knife")
						## Knife has now been taken, set variable to 'true'
						knifeTaken = True
					choice = input()
					parse()
				else:
					print("Unfortunately, you need something to carry the knife in. You cannot take it.")
					choice = input()
					parse()

		elif (thing == "pendant"):
			unknownAction()
			if (action == "talk to") or (action == "give") or (action == "show") or (action == "buy") or (action == "eat") or (action == "drink"):
				why()
			## Print approach line
			else:
				if (pendantTaken == False):
					print("\nInside the dresser is a pendant.")
			## Valid story choices
			if (action == "look at"):
				print("The pendant is made of shiny, metalic pyrite. It hangs from a plain leather",
				"chord that looks soft from wear. You peer closer at the pendant itself. There are",
				"strange symbols engraved into the surface of the pendant. Smooth and curved lines",
				"run across the surface, tangling and cutting into one another. You wonder what they",
				"might mean, if anything at all...?")
				choice = input()
				parse()
			elif (action == "push"):
				if (pendantTaken == False):
					print("You nudge the pendant to a couple of inches to the left.")
				else:
					print("Why would you want to do that?")
				choice = input()
				parse()
			elif (action == "feel"):
				print("The leather cord is soft and well worn. The pendant, however, is cold",
				"and you can feel the indentations of the strange symbols in the stone with",
				"the pads of your fingers.")
				choice = input()
				parse()
			elif (action == "take"):
				if (backpackTaken == True):
					if (pendantTaken == False):
						print("You grasp the pendant in your hand. It's cool to the touch and you",
						"observe it for a moment while it rest in the palm of your hand. What a",
						"strange object. You wonder who it belonged to.")
						print("You turn and put it into your backpack.")
					else:
						print("You have already taken the pendant.")
					if (pendantTaken == False):
						player.backpack("pendant")
						## Pendant has now been taken, set variable to 'true'
						pendantTaken = True
					choice = input()
					parse()
				else:
					print("Unfortunately, you need something to carry the pendant in. You cannot take it.")
					choice = input()
					parse()

		elif (thing == "matches"):
			unknownAction()
			if (action == "talk to") or (action == "give") or (action == "show") or (action == "buy") or (action == "eat") or (action == "drink"):
				why()
			## Print approach line
			else:
				if (matchesTaken == False):
					print("\nInside the dresser is a set of matches.")
			## Valid story choices
			if (action == "look at"):
				print("The matches are in a little, folded carboard packet like you might get",
				"from a particularly seedy hotel or bar. On the carboard packet there is a faded",
				"little picture of a man in a yellow raincoat standing in front of a lighthouse.",
				"The text above the picture reads: 'Jolly Sailor Matches'.")
				choice = input()
				parse()
			elif (action == "push"):
				if (matchesTaken == False):
					print("You use a finger to slide the packet of matches a litle to the left.")
				else:
					print("Why would you want to do that?")
				choice = input()
				parse()
			elif (action == "feel"):
				print("The carboard feels cheaply made.")
				print("You worry that you might rub the red off the top of the matches, so",
				"you choose not to touch them.")
				choice = input()
				parse()
			elif (action == "take"):
				if (backpackTaken == True):
					if (matchesTaken == False):
						print("You pick up the wee packet of matches. You twist around to unzip your",
						"backpack and stick them inside.")
					else:
						print("You have already taken the packet of matches.")
					if (matchesTaken == False):
						player.backpack("matches")
						## Matches have now been taken, set variable to 'true'
						matchesTaken = True
					choice = input()
					parse()
				else:
					print("Unfortunately, you need something to carry the matches in. You cannot take it.")
					choice = input()
					parse()

		elif (thing == "map"):
			unknownAction()
			if (action == "talk to") or (action == "give") or (action == "show") or (action == "buy") or (action == "eat") or (action == "drink"):
				why()
			## Print approach line
			else:
				if (mapTaken == False):
					print("\nInside the dresser is a map.")
			## Valid story choices
			if (action == "look at"):
				print("The map is in color and details the city as well as the surrounding",
				"hundred miles. You notice that there is a route marked out in red pen from",
				"the city center out into the hills to a place called 'The Trebond Mines'")
				print("You wonder whose map this was, and if they ever made it to the mines.",
				"You decide that you too will head for the hills and try and make it to the",
				"Trebond Mines.")
				choice = input()
				parse()
			elif (action == "push"):
				if (mapTaken == False):
					print("You push the map a little to the left.")
				else:
					print("Why would you want to do that?")
				choice = input()
				parse()
			elif (action == "feel"):
				print("The map is printed on slightly glossy paper. It's been folded many",
				"times and as a result you can trace the grooves in the paper.")
				choice = input()
				parse()
			elif (action == "take"):
				if (backpackTaken == True):
					if (mapTaken == False):
						print("You take the map out of the dresser and fold it carefully. You unzip",
						"your backpack and place it inside.")
					else:
						print("You have already taken the map.")
					if (mapTaken == False):
						player.backpack("map")
						## Map has now been taken, set variable to 'true'
						mapTaken = True
					choice = input()
					parse()
				else:
					print("Unfortunately, you need something to carry the map in. You cannot take it.")
					choice = input()
					parse()

		elif (thing == "coins"):
			unknownAction()
			if (action == "talk to") or (action == "give") or (action == "show") or (action == "buy") or (action == "eat") or (action == "drink"):
				why()
			## Print approach line
			else:
				if (coinsTaken == False):
					print("\nInside the dresser are ten gold coins.")
			## Valid story choices
			if (action == "look at"):
				print("You look at the pile of coins and decide that they are indeed real gold.",
				"Perhaps they could be used to purchase supplies or as bribes if you encounter",
				"any people.")
				choice = input()
				parse()
			elif (action == "push"):
				if (coinsTaken == False):
					print("You push the pile of coins to the left and they clatter and role all",
					"over the inside of the drawer.")
				else:
					print("Why would you want to do that?")
				choice = input()
				parse()
			elif (action == "feel"):
				print("You pick up a coin in your hand. It feels solid, a little heavy, and",
				"it's slightly cold.")
				if (coinsTaken == False):
					print("You put the coin back in the drawer.")
				else:
					print("You put the coin back in your backpack.")
				choice = input()
				parse()
			elif (action == "take"):
				if (backpackTaken == True):
					if (coinsTaken == False):
						print("You reach into the dresser with both hands and scoop out the coins.",
						"They clink together in your hands before you unceremoniously dump them",
						"with a clatter into your backpack.")
					else:
						print("You have already taken the coins.")
					if (coinsTaken == False):
						player.backpack("coins")
						## Coins have now been taken, set variable to 'true'
						coinsTaken = True
					choice = input()
					parse()
				else:
					print("Unfortunately, you need something to carry the coins in. You cannot take them.")
					choice = input()
					parse()

def roomTwo():
	print("\nThis is the end of your journey for now.")
	print("Play 'Part Two'* to learn what happens next!")
	print("\n\n\n***Developer's Note: 'Part Two' has yet to be created.")
	exit()

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
	#print("\n\n\nYou want to:", action)
	#print("With the:", thing)
	#print("With the person:", person)
	## TEMP CODE ENDS
	## Redirect to 'roomOneChoices' if 'roomOne' hasn't been completed yet
	if (roomOneCompleted == False):
		roomOneChoices()

## Error message for when the user inputs an action that is unknown
def unknownAction():
	if (action == "unknown"):
		print("\nYou don't know how to do that.")
		print("Try commands like: 'talk to', 'give to', 'show to', 'look at', 'take',",
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