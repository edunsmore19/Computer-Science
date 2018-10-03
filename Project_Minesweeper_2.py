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
	printFinalBoard()
	firstClear()

## Command that prompts the user to pick their first tile & clear it
def firstClear():
	print("Type the row and then collumn of the tile you would like to begin with.")
	print("It will clear all of the blank tiles around it and reveal the numbers.")
	print("Collumns and rows begin at zero.")

	## Row choice
	while True:
		try:
			global row
			row = int(input("Type your row choice:\n"))
			break
		except ValueError:
			error()
			firstClear()
			firstOverWrite()
	if (0 <= row <= width-1):
		print("Row:", row,"\n")
	else:
		error()
		firstClear()

	## Collumn choice
	while True:
		try:
			global collumn
			collumn = int(input("Type your collumn choice:\n"))
			break
		except ValueError:
			error()
			firstClear()
			firstOverWrite()
	if (0 <= collumn <= height-1):
		print("Collumn:", collumn, "\n")
		firstOverWrite()
	else:
		error()
		firstClear()

		#------------------------------------

## Comand that prompts the user to either flag or clear a space
def flagOrClear():
	print("Type the row and then collumn of the tile you would like to either clear or flag.")
	print("Collumns and rows begin at zero.")

	## Row choice
	while True:
		try:
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
	if (choice == "f"):
		print("You've chosed to flag", row, ",", collumn)
	elif (choice == "c"):
		print("You've chosen to clear", row, ",", collumn)
	else:
		error()
		flagOrClear()

## Command to overwrite blankBoard to present 
def firstOverWrite():
	gameBoard[row][collumn] = "."

	## Print user's game board
	for x in range(height):
		print(*gameBoard[x])


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