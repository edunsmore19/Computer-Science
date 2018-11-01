## Class_Work_Deck_And_Card
## October 31, 2018
## Making a card & deck class to function like playing cards.

cardList = []


## Create class 'Card'
class Card:
	def __init__ (self, rank, suit):
		self.rank = rank
		self.suit = suit
		self.name = (rank + suit)

## Create class 'Deck'
class Deck:
	def __init__ (self):
		self.cardList = cardList

## Begin the creation of new cards
## Create a for loop to cycle through all possible suits for cards
for x in range(0, 4):
	if (x == 0):
		suit = " of Spades"
	if (x == 1):
		print()
		suit = " of Clubs"
	if (x == 2):
		print()
		suit = " of Hearts"
	if (x == 3):
		print()
		suit = " of Diamonds"
	## Create a for loop to cycle through all possible ranks for cards
	for i in range(2, 15):
		createCard = Card(str(i), str(suit))
		if (i == 11):
			createCard = Card("Jack", str(suit))
		if (i == 12):
			createCard = Card("Queen", str(suit))
		if (i == 13):
			createCard = Card("King", str(suit))
		if (i == 14):
			createCard = Card("Ace", str(suit))
		## Add new card to a list, contained in Deck
		cardList.append(createCard.name)
		print("This is the Deck now:", len(cardList))

