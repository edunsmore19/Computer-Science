## Project_Adventure_Game
## September 17, 2018
## User engages in an adventure-style game requiring the user to make 
## choices that change the story.
## Honor Code: I have neither given nor recieved any unauthorized aid.

## Initialize variables

## 'title' clears terminal & presents title
def title():
	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("Welcome to WITCHY BUISNESS.")
	readBetter()
	start()

## 'start' begins with asking the user if they want to play
def start():
	choice = input("Are you ready to play? \nType 'y' or 'n'\n")
	choice = choice.lower()
	if (choice == "y"):
		readBetter()
		character()
	elif (choice == "n"):
		readBetter()
		print("\nA shame. \nGoodbye.\n")
		exit()
	else:
		readBetter()
		error()
		readBetter()
		start()

## Character customization
def character():
	characterName = input("\nWhat is your name?\n")
	readBetter()
	print("\nWelcome,",characterName + ".")
	print("What kind of witch would you like to play as?")
	print("You may be a 'fire witch', 'water witch', 'swamp witch', or a 'practical witch'.")
	witchType = input("Type the kind of witch you'd like to play as.\n")
	witchType = witchType.lower()
	if (witchType.startswith('f') + witchType.startswith('w') + witchType.startswith('s') + witchType.startswith('p') == False):
		error()
	## Add the term 'witch' to the end of type if user didn't already add it
	if (witchType.endswith('h') == False):
		witchType = witchType + " witch"
	readBetter()
	print("\n\n\n\nExcellent.")
	readBetter()
	soWeFindOurSelvesAlone()

## Begin w/ small story & first movement query
def soWeFindOurSelvesAlone():
	print("""\nIt is Valentine's Day, and you booked what you thought would be a
lovely vacation for you and your wife in a small country town.""")
	print("""Little did you know, this particular small country town still practices
witch burning.""")
	print("""And after a small miracle performed by your lovely wife in the town
square, the town sheriff showed up.""")
	print("And the mob formed.")
	print("You escaped... barely.")
	print("Your wife was not so lucky.")
	print("And so you seek to bust your wife out of jail.")
	print("And somehow salvage your romantic vacation.")
	print("\nHopes are not high.")
	choice = input("\nWould you like to approach the jail? (y/n)\n")
	choice = choice.lower()
	if (choice == "y"):
		readBetter()
		approachJail()
	elif (choice == "n"):
		readBetter()
		dontApproachJail();
	else:
		readBetter()
		error()
		readBetter()
		soWeFindOurSelvesAlone()

## Captured by townspeople, AKA: GAME OVER
def capturedByTownspeople():
	print("\nYou've attracted the attention of the townspeople!")
	print("They surround & capture you.")
	print("You're thrown in jail.")
	print("\nYour wife is not pleased.")
	print("\nShe says she's never letting you plan another romantic getaway.")
	print("\n\n\nGAME OVER")
	choice = input("\nWould you like to play again (y/n)\n")
	choice = choice.lower()
	if (choice == "y"):
		start()
	elif(choice == "n"):
		exit()
	else:
		error()
		capturedByTownspeople()

def dontApproachJail():
	print("\n\n\n\n\n\nYou decide not to approach the jail.")
	print("This turns out to be a mistake. Much like this vacation.")
	capturedByTownspeople()

def approachJail():
	print("You approach the jail.")
	print("You notice that the entrance is not locked.")
	print("You peer in, and see the Sheriff sitting in the corner.")
	print("""He is holding a cup of coffee, leaning back in his chair, and 
reading a bad YA novel.""")
	print("You need to distract him somehow.")
	print("You have three options.")
	print("""1) Inform him that you are a witch & that he is, in fact, ruining 
your holiday.""")
	print("2) Use your powers to create some sort of diversion.")
	print("3) Attempt to signal your wife through covert means.")
	choice = input("Choose your action. (Type either '1', '2', or '3').")
	if (choice == "1"):
		readBetter()
		tryToTalkItOut()
	elif (choice == "2"):
		readBetter()
		powersToDistract()
	elif (choice == "3"):
		readBetter()
		covertMeans()
	else:
		readBetter()
		error()
		readBetter()
		approachJail()

def tryToTalkItOut():
	print("You stride confidently into the jail.")
	print("'Sheriff,' you say, 'I am a witch and it is Valentine's day.'")
	print("The sheriff pauses mid-sip and stares at you.")
	print("'You have ruined our vacation--' You begin.")
	print("\nYou are promplty arrested.")
	print("You're thrown in jail.")
	print("\nYour wife is not pleased.")
	print("\nShe says she's never letting you plan another romantic getaway.")
	print("\n\n\nGAME OVER")
	choice = input("\nWould you like to play again (y/n)\n")
	choice = choice.lower()
	if (choice == "y"):
		start()
	elif(choice == "n"):
		exit()
	else:
		error()
		tryToTalkItOut()

def powersToDistract():
	print("You, being a ______________, have more options than a mere human.") #insert variable depicting witchType

	print("Using your powers, you", _____________) #insert variable for thing
	print("You have successfully distracted him.")

def covertMeans():
	print("You cup your hands around you mouth and make a bird noise.")
	print("The sheriff seems nonplussed.")
	print("You wait for a signal from your wife.")
	print("\nNothing happens.")
	print("\nYou decide to try something else.")
	print("""1) Inform him that you are a witch & that he is, in fact, ruining 
your holiday.""")
	print("2) Use your powers to create some sort of diversion.")
	choice = input("\nChoose your action. (Type either '1' or '2')")
	choice = choice.lower()
	if (choice == "1"):
		readBetter()
		tryToTalkItOut()
	elif (choice == "2"):
		readBetter()
		powersToDistract()
	else:
		readBetter()
		error()
		readBetter()
		covertMeans()

def successfullyDistractedTheSheriff():
	pass

## Error message for when user types the wrong thing
def error():
	print("\nDo what you're told. \nTry again with the proper command.\n")

## Big line to help user read
def readBetter():
	print("----------------------------------------------------")

## Run
title()

## Test print lines
##print("Ready to play choice:", start.choice())
##print("Character name choice:", characterName.character())
##print("Type of witch choice:", witchType.character())
##print("Did you approach the jail:", soWeFindOurSelvesAlone.choice())
##print("READOUT COMPLETE")
