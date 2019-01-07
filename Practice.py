"""
for a in range(0, 7):
	for b in range(0, 7):
		list1.append("#")
		if (a != 0) and (a != 6) and (b != 0) and (b != 6):
			list2.append(" ")
for a in range(0, 7):
	if (a == 0) or (a == 6):
		print(*list1)
	else:
		print(*list2)


board = [[0]*7 for x in range(7)]
print(*board)
"""
"""
## First set
cornishRex = [[" "]*7 for x in range(7)]
for a in range(0, 7):
	for b in range(0, 7):
		if (a == 0) or (a == 6):
			cornishRex[a][b] = "#"
		elif (b == 0) or (b == 6):
			cornishRex[a][b] = "#"

for x in range(7):
	print(*cornishRex[x])

print()

## Second set
scottishFold = [[" "]*7 for x in range(7)]
for a in range(0, 7):
	for b in range(0, 7):
		if (b == 0) or (b == 6):
			scottishFold[a][a] = "#"
		if (b == 0) or (b == 6):
			scottishFold[a][-a-1] = "#"
		if (a == 0) or (a == 6):
			scottishFold[a][b] = "#"

for x in range(7):
	print(*scottishFold[x])

print()

## Third set
maineCoon = [[" "]*7 for x in range(7)]
for a in range(0, 7):
	for b in range(0, 7):
		if (b == 0) or (b == 6):
			maineCoon[a][b] = "#"
		if (b == 0) or (b == 6):
			maineCoon[a][a] = "#"
		if (b == 0) or (b == 6):
			maineCoon[a][-a-1] = "#"
		if (a == 0) or (a == 6):
			maineCoon[a][b] = "#"

for x in range(7):
	print(*maineCoon[x])
"""
"""
deck = []
suit = ""
value = ""
card = ""
for a in range(0, 4):
	for b in range(2, 15):
		## Determine suit
		if (a == 0):
			suit = "H"
		elif (a == 1):
			suit = "D"
		elif (a == 2):
			suit = "S"
		else:
			suit = "C"
		## Determine value
		if (b <= 10):
			value = str(b)
		elif (b == 11):
			value = "J"
		elif (b == 12):
			value = "Q"
		elif (b == 13):
			value = "K"
		else:
			value = "A"
		## Append to list
		card = value + suit
		deck.append(card)
print(*deck)
"""
"""

numbers = [14, 9, 25, 8, 10, 20, 7, 28, 21, 11]


for a in range(len(numbers)):
	## Number in front is even, number after is odd, divisible by three
	if (numbers[a] % 2 == 0) and (numbers[a + 2] % 2 != 0) and (numbers[a + 1] % 3 == 0):
		## Number is special, print out
		print("Position " + str(a + 1) + ": " + str(numbers[a]) + ", " + str(numbers[a + 1]) + ", " + str(numbers[a + 2]))
"""

board = [["O"]*8 for x in range(8)]
board[0][0] = "1"
board[1][1] = "1"
queenLocation = []
attack = False

for x in range(8):
	print(*board[x])

## Process
for a in range(8):
	for b in range(8):
		if (board[a][b] == "1"):
			queenLocation.append(a)
			queenLocation.append(b)
#print(queenLocation)

if (queenLocation[0] == queenLocation[2]):
	#print("Same collumn")
	attack = True
if (queenLocation[1] == queenLocation[3]):
	#print("Same row")
	attack = True
for a in range(1, 9):
	for b in range(1, 9):
		if (queenLocation[0]-a == queenLocation[2]):
			if (queenLocation[1]-a == queenLocation[3]):
				#print("Same diagonal 1")
				attack = True
			elif (queenLocation[1]+a == queenLocation[3]):
				#print("Same diagonal 2")
				attack = True
		elif (queenLocation[0]+a == queenLocation[2]):
			if (queenLocation[1]-a == queenLocation[3]):
				#print("Same diagonal 3")
				attack = True
			elif (queenLocation[1]+a == queenLocation[3]):
				#print("Same diagonal 4")
				attack = True

if (attack == True):
	print("Attack imminent")
else:
	print("No attack imminent")


"""
		print("1")
for x in range(1, 9):
	## Check right
	queenX =+ 1
	if (queenX == queenLocation[3]):
		attack = True
		print("2")
for x in range(1, 9):
	## Check above
	queenY =- 1
	if (queenY == queenLocation[2]):
		attack = True
		print("3")
for x in range(1, 9):
	## Check below
	queenY =+ 1
	if (queenY == queenLocation[2]):
		attack = True
		print("4")

"""

