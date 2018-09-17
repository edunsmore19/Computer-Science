## Class_Work_Adventure_Demo
## September 17, 2018
## Demo on a choose-your-own adventure style game

def start():
	response = input("Greetings! You are looking for treasure. Your map", 
		"says that the treature can be found notherly--However, your friend",
		"says that he heard someone talking about treasure in the south.",
		"Do you 1) trust your friend, or 2) trust the map?")
	if response == "1":
		friend()
	elif response == "2":
		map()
	else:
		print("You must type 1 or 2. Please try again.")
		start()
def map():
	pass
def friend():
	pass
start()