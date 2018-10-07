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
bombLocation = []

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
		## Numbers
		## Next to bombs
		if (uToD != 0):
			if (board[rToL][uToD-1] != "*"):
				board[rToL][uToD-1]+= 1
		if (uToD != (width-1)):
			if (board[rToL][uToD+1] != "*"):
				board[rToL][uToD+1]+= 1
		## Above/below bombs
		if (rToL != 0):
			if (board[rToL-1][uToD] != "*"):
				board[rToL-1][uToD] += 1
		if (rToL != (height-1)):
			if (board[rToL+1][uToD] != "*"):
				board[rToL+1][uToD] += 1
		## Left corners
		if (rToL != (height-1)) and (uToD != 0):
			if (board[rToL+1][uToD-1] != "*"):
				board[rToL+1][uToD-1] += 1
		if (rToL != 0) and (uToD != 0):
			if (board[rToL-1][uToD-1] != "*"):
				board[rToL-1][uToD-1] += 1
		## Right corners
		if (rToL != 0) and (uToD != (width-1)):
			if (board[rToL-1][uToD+1] != "*"):
				board[rToL-1][uToD+1] += 1
		if (rToL != (height-1)) and (uToD != (width-1)):
			if (board[rToL+1][uToD+1] != "*"):
				board[rToL+1][uToD+1] += 1
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
		printGameBoard()
	elif (choice == "c") and ((gameBoard[row][collumn] != "*") or (gameBoard[row][collumn] == "F")):
		print("You've chosen to clear", row, ",", collumn)
		play()
	else:
		error()
		flagOrClear()

## Command to overwrite gameBoard to reflect 
def play():
	## If player chooses/hits a mine
	if (board[row][collumn] == "*"):
		print("\n\nYou've hit a mine!")
		print("GAME OVER\n")
		printFinalBoard()
	else:
		## Checks for 0 tiles and overwrites them as '.'
		if (board == 0):
			gameBoard[row][collumn] = "."
		## Checks for numbered tiles and presents them on user's board
		else:
			gameBoard[row][collumn] = board[row][collumn]
		## Below chosen tile check
		for x in range(width-row):
			if (board[row+x][collumn] == 0):
				gameBoard[row+x][collumn] = "!"
				## Check to the right
				for y in range(height-collumn):
					print("PRESENT")
					if (board[row][collumn+y] == 0):
						print("moisturize me")
						gameBoard[row][collumn+y] = "@"
					else:
						print("im about to break")
						gameBoard[row][collumn+y] = board[row][collumn+y]
						break
			else:
				gameBoard[row+x][collumn] = board[row+x][collumn]
				break
		## Above chosen tile check
		for x in range((0-row)*(-1)+1):
			if (board[row-x][collumn] == 0):
				gameBoard[row-x][collumn] = "&"
			else:
				gameBoard[row-x][collumn] = board[row-x][collumn]
				break
		## Right side chosen tile check
		#for x in range(height-collumn):
		#	if (board[row][collumn+x] == 0):
		#		gameBoard[row][collumn+x] = "@"
		#	else:
		#		gameBoard[row][collumn+x] = board[row][collumn+x]
		#		break
		## Left side chosen tile check
		## Right upper corner chosen tile check
		## Right lower corner chosen tile check
		## Left upper corner chosen tile check
		## Left lower corner chosen tile check


		## Checks for all blank adjacent tiles
		## Overwrites them as as '.'
		## Checks for the bump numbers on board and overwrites their matches on gameBoard
		## Checks to see if there are any blank tiles left, if not, YOU WIN

		## Print user's game board
		for x in range(height):
			print(*gameBoard[x])
		print()

		printFinalBoard()
		print()
		## Redirect to choose tile
		flagOrClear()


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