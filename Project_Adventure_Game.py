## Project_Adventure_Game
## September 17, 2018
## User engages in an adventure-style game requiring the user to make 
## choices that change the story.
## Honor Code: I have neither given nor recieved any unauthorized aid.

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
		whatIsYourName()
	elif (choice == "n"):
		readBetter()
		print("\nA shame. \nGoodbye.\n")
		exit()
	else:
		error()
		start()

## User's name
def whatIsYourName():
	global characterName
	characterName = input("\nWhat is your name?\n")
	readBetter()
	character()

## Character customization
def character():
	print("\nWelcome,",characterName + ".")
	print("What kind of witch would you like to play as?")
	print("You may be a 1)'fire witch', 2)'water witch', 3)'swamp witch', or a 4)'practical witch'.")
	global witchType
	witchType = input("Choose which kind of witch you'd like to play as. (1, 2, 3, or 4)\n")
	if (witchType == "1" or witchType == "2" or witchType == "3" or witchType == "4"):
		witchType = int(witchType)
		readBetter()
		print("\n\n\n\nExcellent.")
		readBetter()
		soWeFindOurSelvesAlone()
	else:
		error()
		character()

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
	## Initialize 'loveOMeter' as a global @ 40%
	global loveOMeter
	loveOMeter = 40
	print("Currently, your 'Successful Valentine's Day' meter is at", loveOMeter, "%.")
	print("Make correct choices in order to raise it.")
	print("But beware of incorrect choices, which will lower it.")
	print("Do your best to rescue your Valentine's day.")
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
		error()
		soWeFindOurSelvesAlone()

## Captured by townspeople, AKA: GAME OVER
def capturedByTownspeople():
	print("\nLooks like you've attracted the attention of the townspeople!")
	print("They surround & capture you.")
	print("You're thrown in jail.")
	print("\nYour wife is not pleased.")
	print("\nShe says she's never letting you plan another romantic getaway.")
	## 'loveOMeter' presents at zero, saying you've lost
	global loveOMeter
	loveOMeter = 0
	print("Your 'Successful Valentine's Day' meter is at", loveOMeter, "%")
	print("\n\n\nGAME OVER")
	choice = input("\nWould you like to play again (y/n)\n")
	choice = choice.lower()
	if (choice == "y"):
		print()
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
		error()
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
	## 'loveOMeter' presents at zero, saying you've lost
	global loveOMeter
	loveOMeter = 0
	print("Your 'Successful Valentine's Day' meter is at", loveOMeter, "%")
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
	global witchKind
	if (witchType == 1):
		witchKind = "fire witch"
	elif (witchType == 2):
		witchKind = "water witch"
	elif (witchType == 3):
		witchKind = "swamp witch"
	else:
		witchKind = "practical witch"

## User chooses to use their powers to distract the sheriff
def powersToDistract():
	powers()
	print("You, being a, " + witchKind + ", have more options than a mere human.")
	if (witchType == 1):
		action = """cause the sheriff’s coffee to evaporate. He attempts to take a sip,
but becomes confused. He gets up to make some more coffee."""
	elif (witchType == 2):
		action = """cause the sheriff’s book to catch fire. He throws it away
from himself, jumps to his feet, and attempts to stomp it out."""
	elif (witchType == 3):
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
		error()
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
		error()
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
		error()
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
	print("\nYour 'Successful Valentine's Day' meter plumets.")
	print("\nThe sheriff immediately notices you and signals to the townspeople.")
	capturedByTownspeople()

## User decides to use their powers to destroy the lock
def powersToUnlock():
	print("You concentrate on the lock and pray for something to happen.")
	powers()
	if (witchType == 1):
		action = """Water starts to gather on, and around the metal of the lock. 
The lock begins to rust before your eyes--it eventually disintigrates."""
	elif (witchType == 2):
		action = "Flames errupt from your hands! The lock melts under your barrage."
	elif (witchType == 3):
		action = """The metal of the lock creaks and moans. It twists itself
unexpectedly into the shape of an oragami crane."""
	else:
		action = """You look down at the lock and notice that the key is still in it.
You take a hold of it, and turn it."""
	print(action, "You push the door gently inwards, and it creaks open.")
	print("""and as a bonus, your wife looks mildly impressed. You're glad you did not make a fool
of yourself by trying to pick the lock, and instead did the cool, impressive thing.""")
	## Assign 'loveOMeter' a 25 point increase
	global loveOMeter
	loveOMeter += 25
	print("\n(Your 'Successful Valentine's Day' meter has increased to", loveOMeter, "%)\n")
	readBetter()
	youEscape()

## The user escapes
def youEscape():
	print("You grab your wife's hand & the two of you begin to run.")
	print("'It's not truly a romantic getaway if one of us isn't kidnapped.' You say.")
	print("She cracks a smile. 'Regadless,' she says, 'You're not planning our next vacation.'")
	print("""\nYou run, hand in hand, for the door--but unfortunetly, all of this cute dialogue
has captured the sheriff's attention.""")
	print("'Stop right there.' Shouts the sheriff. 'The power of Christ compells you!'")
	print("Your wife and you exchange a glance.")
	print("\nQuick! Say something witty!")
	print("1) Erm...")
	print("2) *eye roll* Isn't that vampires? Get your supernatural creatures straight.")
	print("3) Hah! I love garlic sauce on my pasta!")
	choice = input("Choose your action. (Type either '1', '2', or '3').\n")
	if (choice == "1"):
		readBetter()
		print("Alack!\nYou could not think of anything!")
		print("Thankfully, your blunder goes mostly unnoticed.")
	elif (choice == "2"):
		readBetter()
		print("A fantastic comeback!")
		print("Both the sheriff and your wife seem mighty impressed.")
		## Assign 'loveOMeter' a 10 point increase
		## Remind program that we are using a global variable in this function
		global loveOMeter
		loveOMeter+=10
		print("\n(Your 'Successful Valentine's Day' meter has increased to", loveOMeter, "%)")
	elif (choice == "3"):
		readBetter()
		print("You've said something that vaguely relates, but in the worst possible way!")
		print("Oh dear.")
		## Assign 'loveOMeter' a 10 point decrease
		loveOMeter-=10
		print("\n(Your 'Successful Valentine's Day' meter has decreased to", loveOMeter, "%)")
	else:
		error()
		youEscape()
	readBetter()
	fightTheSheriff()

## User must choose how to incapacitate the sheriff
def fightTheSheriff():	
	print("Witty repartee now aside, you must decide how to incapacitate the sheriff.")
	print("You have three options.")
	print("1) Convince him to let you by.")
	print("2) Hand to hand combat.")
	print("3) Let your wife figure it out.")
	choice = input("Choose your action. (Type either '1', '2', or '3').\n")
	if (choice == "1"):
		readBetter()
		print("The sheriff isn't too into listening.")
		print("Before you can even open your mouth, he yells out to his fellow townspeople.")
		capturedByTownspeople()
	elif (choice == "2"):
		readBetter()
		print("You've read a lot of books that include fighty bits.")
		print("It can't be that much different in real life... can it?")
		print("\nIt turns out, it's not.")
		print("You just have to be willing to hurt & get hurt back.")
		print("\nWhile efficient, your wife does not believe in violence.")
		print("\nEspecially not while she's on holiday.")
		## Assign 'loveOMeter' a 5 point decrease
		## Remind program that we are using a global variable in this function
		global loveOMeter
		loveOMeter -= 5
		print("\n(Your 'Successful Valentine's Day' meter has decreased to", loveOMeter, "%)")
		readBetter()
		soNowWeFindOurselvesTogether()
	elif (choice == "3"):
		readBetter()
		print("Your wife appreciates you letting her have the narrative spotlight for once.")
		print("You watch her eyes flash bright blue, and she makes a sharp cutting motion with her arm.")
		print("The sheriff collapses in a sudden deep slumber.")
		## Assign 'loveOMeter' a 10 point increase
		loveOMeter += 10
		print("\n(Your 'Successful Valentine's Day' meter has increased to", loveOMeter, "%)")
		soNowWeFindOurselvesTogether()
	else:
		error()
		fightTheSheriff()
	readBetter()

## User must now choose an action in the town square
def soNowWeFindOurselvesTogether():
	print("Your wife and you emerge from the town jail.")
	print("You can see the townspeople gathering flamable material in the distance.\n")
	print("You look around for some sort of getaway method.")
	print("1) An old jalopy practically rusted to the sidewalk.")
	print("2) A pair of broomsticks rested haphazardly against the side of a building.")
	print("3) A firey stallion tied to a post, munching out of a feedbag.")
	choice = input("Choose your action. (Type either '1', '2', or '3').\n")
	readBetter()
	if (choice == "1"):
		print("Your wife glares at the rustbucket-death-trap before reluctantly climbing inside.")
		print("""You try to think of a cool joke about how old the car is and how great your
Valentine's Day is going, but you come up blank.""")
		## Assign 'loveOMeter' a 15 point decrease for style
		## Remind program that we are using a global variable in this function
		global loveOMeter
		loveOMeter -= 15
		print("\n(Your 'Successful Valentine's Day' meter has decreased to", loveOMeter, "%)")
		print("""\nHowever, by some miracle the old thing has the key in the ignition and
manages to cough and hack its way into life.""")
		print("It crawls slowly away from the town.")
		print("'It's been one helluva day.' You say.")
		print("Your wife agrees.")
		print("\nShe also insists that you do not plan your next vacation.")
		youWin()
	elif (choice == "2"):
		print("The broomstick thing is a harmful stereotype.")
		print("\nAlso, brooms cannot fly, or move in any sort of way unassisted.")
		print("Your wife and you get into a loud argument.")
		readBetter()
		capturedByTownspeople()
	elif (choice == "3"):
		print("Salutations for style, your wife looks mad impressed.")
		print("""She loves horses--even more so when they're your mode of escape from terrible
villagers seeking to burn you at the stake.""")
		## Assign 'loveOMeter' a 15 point increase for style
		loveOMeter += 15
		print("\n(Your 'Successful Valentine's Day' meter has increased to", loveOMeter, "%)")
		print("\n'Did you plan this??' She asks.")
		print("'Oh yes.' You absolutely lie and then thank whatever higher powers are out there.")
		print("""\nYou help your wife onto the horse (who seems a bit surprised, but not upset at
this new development in its life, and besides, he's a fan of witches).""")
		print("You untie the horse from the post, unclip the feed bag, and then climb on yourself.")
		print("You ride happily ever after into the sunset.")
		youWin()
	else:
		error()
		soNowWeFindOurselvesTogether()
	readBetter()

## User reacher the end of the game, YOU WIN
def youWin():
	readBetter()
	print("\n\n\n\n")
	print(characterName + ",", witchKind + ",", "congratulations.")
	print("\nYOU WIN!\n")
	print("\n(Your 'Successful Valentine's Day' meter is at", loveOMeter, "%")
	if (loveOMeter == 100):
		choice = input("\nWould you like to play again (y/n)\n")
		choice = choice.lower()
		if (choice == "y"):
			readBetter()
			start()
		elif(choice == "n"):
			readBetter()
			exit()
		else:
			error()
			youWin()
	else:
		choice = input("""\nWould you like to play again to try and fill your 'Successful
Valentine's Day' meter all the way to the top? (y/n)\n""")
		choice = choice.lower()
		if (choice == "y"):
			readBetter()
			start()
		elif(choice == "n"):
			readBetter()
			exit()
		else:
			error()
			youWin()

## Error message for when user types the wrong thing
def error():
	readBetter()
	print("\nDo what you're told. \nTry again with the proper command.\n")
	readBetter()

## Big line to help user read
def readBetter():
	print("----------------------------------------------------")

## Run
title()
