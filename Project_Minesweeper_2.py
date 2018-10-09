## Project_Minesweeper_2
## October 2, 2018
## I have neither given nor recieve any unauthorized aid.
## User provices the width and height for the board as well as
## the number of bombs that will be randomly placed and then 
## the program determines how many bombs surround each space.

import sys
import random

## Initialize variables
global width
width = int(sys.argv[1])
global height
height = int(sys.argv[2])
bombs = int(sys.argv[3])

board = [[0]*width for x in range(height)]
gameBoard = [[0]*width for x in range(height)]
fauxBoard = [[0]*width for x in range(height)]
bombLocation = []
conquerAndKill = []

## Welcome user, explain game
def title():
	print("\n\nWelcome to MineSweeper!")
	print("To select a tile, enter the row and collumn number.")
	print("Here is your board.\n\n")
	printGameBoard()

## Generates & prints game board
def printGameBoard():
	## Print blank board
	for x in range(height):
		print(*gameBoard[x])
	print()
	realBoard()

## Generates the real board w/ bombs and numbers
def realBoard():
	## Generate bombs
	for x in range(bombs):
		bombLocation.append(random.randint(0, (width * height - 1)))

	## Put bombs on the board
	for x in range(len(bombLocation)):
		## Bombs
		rToL = bombLocation[x] / width
		rToL = int(rToL)
		uToD = bombLocation[x] % width
		board[rToL][uToD] = "*"
		fauxBoard[rToL][uToD] = "*"
		## Numbers
		## Next to bombs
		if (uToD != 0):
			if (board[rToL][uToD-1] != "*"):
				board[rToL][uToD-1]+= 1
				fauxBoard[rToL][uToD-1]+= 1
		if (uToD != (width-1)):
			if (board[rToL][uToD+1] != "*"):
				board[rToL][uToD+1]+= 1
				fauxBoard[rToL][uToD+1]+= 1
		## Above/below bombs
		if (rToL != 0):
			if (board[rToL-1][uToD] != "*"):
				board[rToL-1][uToD] += 1
				fauxBoard[rToL-1][uToD] += 1
		if (rToL != (height-1)):
			if (board[rToL+1][uToD] != "*"):
				board[rToL+1][uToD] += 1
				fauxBoard[rToL+1][uToD] += 1
		## Left corners
		if (rToL != (height-1)) and (uToD != 0):
			if (board[rToL+1][uToD-1] != "*"):
				board[rToL+1][uToD-1] += 1
				fauxBoard[rToL+1][uToD-1] += 1
		if (rToL != 0) and (uToD != 0):
			if (board[rToL-1][uToD-1] != "*"):
				board[rToL-1][uToD-1] += 1
				fauxBoard[rToL-1][uToD-1] += 1
		## Right corners
		if (rToL != 0) and (uToD != (width-1)):
			if (board[rToL-1][uToD+1] != "*"):
				board[rToL-1][uToD+1] += 1
				fauxBoard[rToL-1][uToD+1] += 1
		if (rToL != (height-1)) and (uToD != (width-1)):
			if (board[rToL+1][uToD+1] != "*"):
				board[rToL+1][uToD+1] += 1
				fauxBoard[rToL+1][uToD+1] += 1
	flagOrClear()

## Comand that prompts the user to either flag or clear a space
def flagOrClear():
	print("Type the row and then collumn of the tile you would like to either clear or flag.")
	print("Collumns and rows begin at zero.")

	## Row choice
	while True:
		try:
			global row
			row = int(input("Type your row choice:\n"))
			break
		except ValueError:
			error()
			flagOrClear()
	if (0 <= row <= width-1):
		print("Row:", row)
	else:
		error()
		flagOrClear()

	## Collumn choice
	while True:
		try:
			global collumn
			collumn = int(input("Type your collumn choice:\n"))
			break
		except ValueError:
			error()
			flagOrClear()
	if (0 <= collumn <= height-1):
		print("Collumn:", collumn)
	else:
		error()
		flagOrClear()

	## Choose to flag or clear space
	print("You have chosen row:", row, "and collumn:", collumn)
	choice = input("Would you like to flag or clear that tile?\nType 'f' or 'c'\n")
	choice = choice.lower()
	if (choice == "f") and ((gameBoard[row][collumn] == 0) or (gameBoard[row][collumn] == "F")):
		print("You've chosed to flag", row, ",", collumn)
		gameBoard[row][collumn] = "F"
		for x in range(height):
			print(*gameBoard[x])
		print()
		flagOrClear()
	elif (choice == "c") and ((gameBoard[row][collumn] != "*") or (gameBoard[row][collumn] == "F")):
		print("You've chosen to clear", row, ",", collumn)
		play()
	else:
		error()
		flagOrClear()

## Command to overwrite gameBoard to reflect the users' choices
def play():
	## If player chooses/hits a mine
	if (board[row][collumn] == "*"):
		print("\n\nYou've hit a mine!")
		print("GAME OVER\n")
		exit()
	else:
		## Checks for numbered tiles and presents them on user's board
		if ((board[row][collumn] != 0) and (board[row][collumn] != "*")):
			if (gameBoard[row][collumn] != "."):
				print("\nThis is a numbered tile\n")
				gameBoard[row][collumn] = board[row][collumn]
			else:
				print("\nYou've already cleared this tile.")
				print("Would you like to guess again?\n\n")
				## Reprint user's board game
				for x in range(height):
					print(*gameBoard[x])
				print()
				## Redirect to choose tile
				flagOrClear()
			## Print user's game board
			for x in range(height):
				print(*gameBoard[x])
			print()
			## Redirect to choose tile
			flagOrClear()
		## Checks for 0 tiles and overwrites them as '.'
		elif (board[row][collumn] == 0):
			gameBoard[row][collumn] = "."
			## Print the user's game board
			for x in range(height):
				print(*gameBoard[x])
			print()

			## Redirect to choose zeroFilter() to try and suss zeros
			zeroFilter()

## Command to filter through the tiles, looking for zeros
def zeroFilter():
	## Checks for all blank adjacent tiles
	## Check left
	if (collumn != 0):
		if ((board[row][collumn-1] == 0) and (gameBoard[row][collumn-1] != ".")):
			conquerAndKill.append(row)
			conquerAndKill.append((collumn-1))
			gameBoard[row][collumn-1] = "."
		elif (gameBoard[row][collumn-1] == "."):
			print("You've already cleared this tile.")
		else: 
			gameBoard[row][collumn-1] = board[row][collumn-1]
	## Check right
	if (collumn != (width-1)):
		if ((board[row][collumn+1] == 0)  and (gameBoard[row][collumn+1] != ".")):
			conquerAndKill.append(row)
			conquerAndKill.append((collumn+1))
			gameBoard[row][collumn+1] = "."
		elif (gameBoard[row][collumn+1] == "."):
			print("You've already cleared this tile.")
		else:
			gameBoard[row][collumn+1] = board[row][collumn+1]
	## Check above
	if (row != 0):
		if ((board[row-1][collumn] == 0)  and (gameBoard[row-1][collumn] != ".")):
			conquerAndKill.append((row-1))
			conquerAndKill.append(collumn)
			gameBoard[row-1][collumn] = "."
		elif (gameBoard[row-1][collumn] == "."):
			print("You've already cleared this tile.")
		else: 
			gameBoard[row-1][collumn] = board[row-1][collumn]
	## Check below
	if (row != (height-1)):
		if ((board[row+1][collumn] == 0)  and (gameBoard[row+1][collumn] != ".")):
			conquerAndKill.append((row+1))
			conquerAndKill.append(collumn)
			gameBoard[row+1][collumn] = "."
		elif (gameBoard[row+1][collumn] == "."):
			print("You've already cleared this tile.")
		else:
			gameBoard[row+1][collumn] = board[row+1][collumn]
	## Check left upper corner
	if ((collumn != (height-1)) and (row != 0)):
		if ((board[row-1][collumn-1] == 0)  and (gameBoard[row-1][collumn-1] != ".")):
			conquerAndKill.append((row-1))
			conquerAndKill.append(collumn-1)
			gameBoard[row-1][collumn-1] = "."
		elif (gameBoard[row-1][collumn-1] == "."):
			print("You've already cleared this tile.")
		else:
			gameBoard[row-1][collumn-1] = board[row-1][collumn-1]
	## Check left lower corner
	if ((collumn != 0) and (row != (width-1))):
		if ((board[row+1][collumn-1] == 0)  and (gameBoard[row+1][collumn-1] != ".")):
			conquerAndKill.append((row+1))
			conquerAndKill.append(collumn-1)
			gameBoard[row+1][collumn-1] = "."
		elif (gameBoard[row+1][collumn-1] == "."):
			print("You've already cleared this tile.")
		else:
			gameBoard[row+1][collumn-1] = board[row+1][collumn-1]
	## Check right upper corner
	if ((row != 0) and (collumn != (width-1))):
		if ((board[row-1][collumn+1] == 0)  and (gameBoard[row-1][collumn+1] != ".")):
			conquerAndKill.append((row-1))
			conquerAndKill.append(collumn+1)
			gameBoard[row-1][collumn+1] = "."
		elif (gameBoard[row-1][collumn+1] == "."):
			print("You've already cleared this tile.")
		else:
			gameBoard[row-1][collumn+1] = board[row-1][collumn+1]
	## Check right lower corner
	if ((row != (height-1)) and (collumn != (width-1))):
		if ((board[row+1][collumn+1] == 0)  and (gameBoard[row+1][collumn+1] != ".")):
			conquerAndKill.append((row+1))
			conquerAndKill.append(collumn+1)
			gameBoard[row+1][collumn+1] = "."
		elif (gameBoard[row+1][collumn+1] == "."):
			print("You've already cleared this tile.")
		else:
			gameBoard[row+1][collumn+1] = board[row+1][collumn+1]

	conqueredAndKilled()

## 'conquerAndKill' subroutine
def conqueredAndKilled():
	## Go through 'conquerAndKill' list, separate pairs
	if (conquerAndKill != []):
		global horizontal
		horizontal = conquerAndKill[0]
		global vertical
		vertical = conquerAndKill[1]
		del conquerAndKill[0:2]
		test()
	else:
		## Print user's game board
		for x in range(height):
			print(*gameBoard[x])
		flagOrClear()
		print()

	## Check to see if board has been cleared
	## Generate cleared comparison board
	for a in range(width):
		for b in range(height):
			if (fauxBoard[a][b] == 0):
				fauxBoard[a][b] = "."
			elif (fauxBoard[a][b] == "*"):
				fauxBoard[a][b] = 0

	## Comparing 'fauxBoard' with 'gameBoard'
	if (fauxBoard == gameBoard):
		youWin()


## Command to filter through the tiles, looking for zeros
def test():
	## Checks for all blank adjacent tiles
	## Check left
	if (vertical != 0):
		if ((board[horizontal][vertical-1] == 0) and (gameBoard[horizontal][vertical-1] != ".")):
			conquerAndKill.append(horizontal)
			conquerAndKill.append((vertical-1))
			gameBoard[horizontal][vertical-1] = "."
		elif ((board[horizontal][vertical-1] != 0) and (board[horizontal][vertical-1] != "*")): 
			gameBoard[horizontal][vertical-1] = board[horizontal][vertical-1]
	## Check right
	if (vertical != (width-1)):
		if ((board[horizontal][vertical+1] == 0)  and (gameBoard[horizontal][vertical+1] != ".")):
			conquerAndKill.append(horizontal)
			conquerAndKill.append((vertical+1))
			gameBoard[horizontal][vertical+1] = "."
		elif ((board[horizontal][vertical+1] != 0) and (board[horizontal][vertical+1] != "*")): 
			gameBoard[horizontal][vertical+1] = board[horizontal][vertical+1]
	## Check above
	if (horizontal != 0):
		if ((board[horizontal-1][vertical] == 0)  and (gameBoard[horizontal-1][vertical] != ".")):
			conquerAndKill.append((horizontal-1))
			conquerAndKill.append(vertical)
			gameBoard[horizontal-1][vertical] = "."
		elif ((board[horizontal-1][vertical] != 0) and (board[horizontal-1][vertical] != "*")): 
			gameBoard[horizontal-1][vertical] = board[horizontal-1][vertical]
	## Check below
	if (horizontal != (height-1)):
		if ((board[horizontal+1][vertical] == 0)  and (gameBoard[horizontal+1][vertical] != ".")):
			conquerAndKill.append((horizontal+1))
			conquerAndKill.append(vertical)
			gameBoard[horizontal+1][vertical] = "."
		elif ((board[horizontal+1][vertical] != 0) and (board[horizontal+1][vertical] != "*")): 
			gameBoard[horizontal+1][vertical] = board[horizontal+1][vertical]
	## Check left upper corner
	if ((vertical != (height-1)) and (horizontal != 0)):
		if ((board[horizontal-1][vertical-1] == 0)  and (gameBoard[horizontal-1][vertical-1] != ".")):
			conquerAndKill.append((horizontal-1))
			conquerAndKill.append(vertical-1)
			gameBoard[horizontal-1][vertical-1] = "."
		elif ((board[horizontal-1][vertical-1] != 0) and (board[horizontal-1][vertical-1] != "*")):  
			gameBoard[horizontal-1][vertical-1] = board[horizontal-1][vertical-1]
	## Check left lower corner
	if ((vertical != 0) and (horizontal != (width-1))):
		if ((board[horizontal+1][vertical-1] == 0)  and (gameBoard[horizontal+1][vertical-1] != ".")):
			conquerAndKill.append((horizontal+1))
			conquerAndKill.append(vertical-1)
			gameBoard[horizontal+1][vertical-1] = "."
		elif ((board[horizontal+1][vertical-1] != 0) and (board[horizontal+1][vertical-1] != "*")): 
			gameBoard[horizontal+1][vertical-1] = board[horizontal+1][vertical-1]
	## Check right upper corner
	if ((horizontal != 0) and (vertical != (width-1))):
		if ((board[horizontal-1][vertical+1] == 0)  and (gameBoard[horizontal-1][vertical+1] != ".")):
			conquerAndKill.append((horizontal-1))
			conquerAndKill.append(vertical+1)
			gameBoard[horizontal-1][vertical+1] = "."
		elif ((board[horizontal-1][vertical+1] != 0) and (board[horizontal-1][vertical+1] != "*")): 
			gameBoard[horizontal-1][vertical+1] = board[horizontal-1][vertical+1]
	## Check right lower corner
	if ((horizontal != (height-1)) and (vertical != (width-1))):
		if ((board[horizontal+1][vertical+1] == 0)  and (gameBoard[horizontal+1][vertical+1] != ".")):
			conquerAndKill.append((horizontal+1))
			conquerAndKill.append(vertical+1)
			gameBoard[horizontal+1][vertical+1] = "."
		elif ((board[horizontal+1][vertical+1] != 0) and (board[horizontal+1][vertical+1] != "*")): 
			gameBoard[horizontal+1][vertical+1] = board[horizontal+1][vertical+1]

	## Redirect to check 'conquerAndKill' list for more coordinates
	conqueredAndKilled()

## Command to generate the YOU WIN screen
def youWin():
	print("\n\n\n\n\nYOU WIN!\n")
	## Fix 'fauxBoard' to reflect bomb again
	for a in range(width):
		for b in range(height):
			if (fauxBoard[a][b] == 0):
				fauxBoard[a][b] = "*"
	for x in range(height):
		print(*fauxBoard[x])
	print()
	exit()

## Command to print the final board when player loses/wins
def printFinalBoard():
	## Print board with bombs and numbers
	for x in range(height):
		print(*board[x])

## Error message
def error():
	print("\nBamboozled again!")
	print("Looks like you didn't input a valid character.")
	print("When selecting a row, you may choose between 0 and", width-1)
	print("When selecting a collumn, you may choose between 0 and", height-1)
	print("When choosing whether to flag or clear a tile, you may choose between 'f' and 'c'.")
	print("Now you'll have to start all over again.\n")

## Run
title()