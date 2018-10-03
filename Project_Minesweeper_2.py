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

board = []
bombLocation = []

## Welcome user, explain game
def title():
	print("\n\nWelcome to MineSweeper!")
	print("To select a tile, enter the row and collumn number.")
	print("Here is your board.\n\n")
	blankBoard()

## Generates & prints game board
def blankBoard():
	## Get board
	board = [[0]*width for x in range(height)]

	## Print blank board
	for x in range(height):
		print(*board[x])
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

def printFinalBoard():
	## Print board with bombs and numbers
	for x in range(height):
		print(*board[x])

## Run
title()