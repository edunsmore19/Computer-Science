## Side_Project_Toad_Simulator
## November 18, 2018
## Take care of your pet toad.

class Toad:
	def __init__(self, name, kind):
		self.name = name
		self.kind = kind
		self.happiness = 5
		self.food = 3
		self.water = 3

def welcome():
	print("\nWelcome to \u001b[7m Toad Simulator \u001b[0m.")
	choice = input("Would you like to play? (Type: 'y' or 'n')\n")
	choice = choice.lower()
	if (choice == "y"):
		toadName()
	elif (choice == "n"):
		print("Okay then. Goodbye.")
		exit()
	else:
		error()
		welcome()


def toadName():
	print("\nYou have entered the \u001b[7m Toad Customization Screen \u001b[0m.")
	global name
	name = input("Toad's Name:\n")
	myToad = Toad(name, "unknown")
	toadKind()

def toadKind():
	print("\nWhat kind of toad would you like?")
	global kind
	kind = input("1) Athletic \n2) Clever \n3) Artistic \n4) Slimy\n")
	if (kind == "1"):
		kind = "athletic"
		myToad = Toad(name, kind)
	elif (kind == "2"):
		kind = "clever"
		myToad = Toad(name, kind)
	elif (kind == "3"):
		kind = "artistic"
		myToad = Toad(name, kind)
	elif (kind =="4"):
		kind = "slimy"
		myToad = Toad(name, kind)
	else:
		error()
		toadKind()





def error():
	print("\nLooks like you typed something that don't make no sense.")
	print("plz try again. \nuWu\n")

## Begin program
welcome()