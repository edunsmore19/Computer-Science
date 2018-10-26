## Class_Work_Bank_Account
## October 26, 2018
## We build a simulation bank account (you know... for funsies.)

class Bank:
	def __init__(self, accountHolder, accountType):
		self.balance = 0
		self.pinNumber = 3475
		self.accountNumber = 758294061
		self.accountStatus = True
		self.accountType = accountType
		self.accountHolder = accountHolder
		self.seccurityQuestions = []

	#def deposit()

myAccount = Bank("Eilidh", "unknown")
print("\nWelcome,", myAccount.accountHolder)
print("What kind of account would you like to open?")
accountTypeChoice = input("You may open a: \n1) Checking Account \n2) Savings Account \nPlease type 1 or 2\n")
if (accountTypeChoice == 1):
	myAccount = Bank("Amanda", "Checking Account")
elif (accountTypeChoice == 2):
	myAccount = Bank("Eilidh", "Savings Account")
print(myAccount.accountHolder + ", you have chosen to open a", myAccount.accountType)


