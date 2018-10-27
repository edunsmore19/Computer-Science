## Class_Work_Bank_Account
## October 26, 2018
## We build a simulation bank account (you know... for funsies.)

class Bank:
	def __init__(self, accountHolder, accountType):
		self.username = "edunsmore19"
		self.password = "Debate1#"
		self.balance = 0
		self.pinNumber = 3475
		self.accountNumber = 758294061
		self.accountStatus = True
		self.accountType = accountType
		self.accountHolder = accountHolder
		self.seccurityQuestions = []

	#def deposit()
## Set up 'myAccount'
myAccount = Bank("Eilidh", "unknown")

## Initiate login sequence w/ username & password
def login():
	print("\nWelcome.")
	print("\nPlease login.")
	usernameChoice = input("\nPlease type your username. \n(Note: it is case sensitive.)\n")
	passwordChoice = input("\nPlease type your password. \n(Note: it is case sensitive.)\n")
	if (usernameChoice == myAccount.username) and (passwordChoice == myAccount.password):
		print("\nWelcome,", myAccount.accountHolder)
		createBankAccount()
	elif (usernameChoice == myAccount.username) and (passwordChoice != myAccount.password):
		readBetter()
		print("Password incorrect.")
		print("Please try again.")
		readBetter()
		login()
	else:
		readBetter()
		print("There is no record of that user.")
		print("Please try again.")
		readBetter()
		login()

## Ask user what kind of bank account they would like to create
def createBankAccount():
	print("What kind of account would you like to open?")
	accountTypeChoice = input("You may open a: \n1) Checking Account \n2) Savings Account \nPlease type 1 or 2\n")
	if (accountTypeChoice == "1"):
		myAccount = Bank("Eilidh", "Checking Account")
	elif (accountTypeChoice == "2"):
		myAccount = Bank("Eilidh", "Savings Account")
	print("\n" + myAccount.accountHolder + ", you have chosen to open a", myAccount.accountType)
	print("Your PIN number is:", myAccount.)




## Line and spacing protocols
def readBetter():
	print("-----------------------------------------------------")

## Run program
login()