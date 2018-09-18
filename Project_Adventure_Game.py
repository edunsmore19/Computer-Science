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
	global characterName
	characterName = input("\nWhat is your name?\n")
	readBetter()
	print("\nWelcome,",characterName + ".")
	print("What kind of witch would you like to play as?")
	print("You may be a 'fire witch', 'water witch', 'swamp witch', or a 'practical witch'.")
	global witchType
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

## User makes the choice not to approach the jail, GAME OVER
def dontApproachJail():
	print("\n\n\n\n\n\nYou decide not to approach the jail.")
	print("This turns out to be a mistake. Much like this vacation.")
	capturedByTownspeople()

## User chooses to approach jail
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
	choice = input("Choose your action. (Type either '1', '2', or '3').\n")
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

## User chooses to try and talk it out with the sheriff, GAME OVER
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

## User's powers break down
def powers():
	global power
	if (witchType == "water witch"):
		power = 1
	elif (witchType == "fire witch"):
		power = 2
	elif (witchType == "swamp witch"):
		power = 3
	else:
		power = 4

## User chooses to use their powers to distract the sheriff
def powersToDistract():
	print("You, being a, " + witchType + ", have more options than a mere human.")
	powers()
	if (power == 1):
		action = """cause the sheriff’s coffee to evaporate. He attempts to take a sip,
but becomes confused. He gets up to make some more coffee."""
	elif (power == 2):
		action = """cause the sheriff’s book to catch fire. He throws it away
from himself, jumps to his feet, and attempts to stomp it out."""
	elif (power == 3):
		action = """cause a neglected potted fern in the corner to grow rapidly.
The fern reaches out and taps the sheriff gently, but insistently on the shoulder.
The sheriff, terrified, tries to strangle the fern.\nThe fern fights valiantly—and
to the death."""
	else:
		action = """cause his book to become incredibly engrossing. He’s never read
something with such vigor before."""
	print("Using your powers, you", action)
	print("You have successfully distracted him.")
	readBetter()
	successfullyDistractedTheSheriff()

## The user chooses to use covert means, this redirects them to choices 1 & 2
def covertMeans():
	print("You cup your hands around you mouth and make a bird noise.")
	print("The sheriff seems nonplussed.")
	print("You wait for a signal from your wife.")
	print("\nNothing happens.")
	print("\nYou decide to try something else.")
	print("""1) Inform him that you are a witch & that he is, in fact, ruining 
your holiday.""")
	print("2) Use your powers to create some sort of diversion.")
	choice = input("\nChoose your action. (Type either '1' or '2')\n")
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

## The user has distracted the sheriff & is asked if they'd like to sneak past
def successfullyDistractedTheSheriff():
	choice = input("Would like to enter the jail and sneak past? (y/n)\n")
	choice = choice.lower()
	if (choice == "y"):
		readBetter()
		sneakPast()
	elif(choice == "n"):
		readBetter()
		print("The sheriff turns and sees you loitering in the entrance way!")
		print("He signals his fellow townspeople!")
		capturedByTownspeople()
	else:
		readBetter()
		error()
		readBetter()
		successfullyDistractedTheSheriff()

## The user sneaks past & is asked how they would like to destroy the lock
def sneakPast():
	print("You quietly creep past the occupied sheriff.")
	print("You come to the cell where your, frankly, peeved wife is being held.")
	print("She gestures (meaningfully) towards the cell lock.")
	print("You have three options.")
	print("1) Attempt to impress your wife and regain her favor by picking the lock.")
	print("2) Use your powers to... well, you're not sure what. But something.")
	print("3) Ask the distracted shreiff to open the door.")
	choice = input("Choose your action. (Type either '1', '2', or '3').\n")
	if (choice == "1"):
		readBetter()
		pickTheLock()
	elif (choice == "2"):
		readBetter()
		powersToUnlock()
	elif (choice == "3"):
		readBetter()
		askPolitely()
	else:
		readBetter()
		error()
		readBetter()
		sneakPast()

## The user decides to ask the sheriff politely, GAME OVER
def askPolitely():
	print("You spin around, and walk over to the sheriff.")
	print("He seems just as shocked as your wife.")
	print("'Would you mind unlocking this cell?' You ask, politely.")
	print("\nThis does not work.")
	print("He arrests you and signals to the townspeople.")
	capturedByTownspeople()

## The user decides to try to pick the lock, GAME OVER
def pickTheLock():
	print("You do not know how to pick locks.")
	print("\nYour wife no longer remembers why she married you.")
	print("\nThe sheriff immediately notices you and signals to the townspeople.")
	capturedByTownspeople()

## User decides to use their powers to destroy the lock
def powersToUnlock():
	print("You concentrate on the lock and pray for something to happen.")
	powers()
	if (power == 1):
		action = """Water starts to gather on, and around the metal of the lock. 
The lock begins to rust before your eyes--it eventually disintigrates."""
	elif (power == 2):
		action = """Flames errupt from your hands! The lock melts under your barrage,
and as a bonus, your wife looks mildly impressed. You're glad you did not make a fool
of yourself by trying to pick the lock, and instead did the cool, impressive thing."""
	elif (power == 3):
		action = """The metal of the lock creaks and moans. It twists itself
unexpectedly into the shape of an oragami crane."""
	else:
		action = """You look down at the lock and notice that the key is still in it.
You take a hold of it, and turn it."""
	print(action, "You push the door gently inwards, and it creaks open.")
	youWin()

## The user wins, end screen, YOU WIN
def youWin():
	print("You grab your wife's hand & the two of you begin to run.")
	print("'It's not truly a romantic getaway if one of us isn't kidnapped.' You say.")
	print("She cracks a smile. 'Regadless,' she says, 'You're not planning our next vacation.'")
	print("\n\n\n\n")
	readBetter
	print(characterName + ",", witchType + ",", "congratulations.")
	print("\nYOU WIN!\n")
	choice = input("\nWould you like to play again (y/n)\n")
	choice = choice.lower()
	if (choice == "y"):
		start()
	elif(choice == "n"):
		exit()
	else:
		error()
		capturedByTownspeople()

## Error message for when user types the wrong thing
def error():
	print("\nDo what you're told. \nTry again with the proper command.\n")

## Big line to help user read
def readBetter():
	print("----------------------------------------------------")

## Run
title()
