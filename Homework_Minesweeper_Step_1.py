## Homework_Minesweeper_Step_1
## September 30, 2018
## User provices the width and height for the board as well as
## the number of bombs that will be randomly placed and then 
## the program determines how many bombs surround each space.

import sys
import random

## Initialize variables
width = int(sys.argv[1])
height = int(sys.argv[2])
bombs = int(sys.argv[3])

board = []
bombLocation = []

## Get board
board = [[0]*width for x in range(height)]

## Print board
for x in range(height):
	print(*board[x])

## Generate bombs
for x in range(bombs):
	bombLocation.append(random.randint(0, (width * height - 1)))
print(bombLocation)

## Put bombs on the board
for x in range(len(bombLocation)):
	rToL = bombLocation[x] / width
	rToL = int(rToL)
	uToD = bombLocation[x] % width
	board[rToL][uToD] = "*"

## Reprint board with bombs
for x in range(height):
	print(*board[x])

print("\n\n\n\n\n\n\n")

## Put the numbers on the board
for a in range(height):
	for b in range(width):
		if (board[a][b] == "*"):
			## NEED TO FIGURE OUT HOW TO LOOP TO CLEAN UP CODE
			for x in range(1):
				## Next to bombs
				if (b != 0) and (board[a][b-1] == 0):
					board[a][b-1] = 1
				elif (b != 0) and (board[a][b-1] == 1):
					board[a][b-1] = 2
				elif (b != 0) and (board[a][b-1] == 2):
					board[a][b-1] = 3

				if (b != (width-1)) and (board[a][b+1] == 0):
					board[a][b+1] = 1
				elif (b != (width-1)) and (board[a][b+1] == 1):
					board[a][b+1] = 2
				elif (b != (width-1)) and (board[a][b+1] == 2):
					board[a][b+1] = 3

				## Above/below bombs
				if (a != 0) and (board[a-1][b] == 0):
					board[a-1][b] = 1
				elif (a != 0) and (board[a-1][b] == 1):
					board[a-1][b] = 2
				elif (a != 0) and (board[a-1][b] == 2):
					board[a-1][b] = 3

				if (a != (height-1)) and (board[a+1][b] == 0):
					board[a+1][b] = 1
				elif (a != (height-1)) and (board[a+1][b] == 1):
					board[a+1][b] = 2
				elif (a != (height-1)) and (board[a+1][b] == 2):
					board[a+1][b] = 3

				## Left corners
				if (a != (height-1)) and (b != 0) and (board[a+1][b-1] == 0):
					board[a+1][b-1] = 1
				elif (a != (height-1)) and (b != 0) and (board[a+1][b-1] == 1):
					board[a+1][b-1] = 2
				elif (a != (height-1)) and (b != 0) and (board[a+1][b-1] == 2):
					board[a+1][b-1] = 3

				if (a != 0) and (b != 0) and (board[a-1][b-1] == 0):
					board[a-1][b-1] = 1
				elif (a != 0) and (b != 0) and (board[a-1][b-1] == 1):
					board[a-1][b-1] = 2
				elif (a != 0) and (b != 0) and (board[a-1][b-1] == 2):
					board[a-1][b-1] = 3

				## Right corners
				if (a != 0) and (b != (width-1)) and (board[a-1][b+1] == 0):
					board[a-1][b+1] = 1
				elif (a != 0) and (b != (width-1)) and (board[a-1][b+1] == 1):
					board[a-1][b+1] = 2
				elif (a != 0) and (b != (width-1)) and (board[a-1][b+1] == 2):
					board[a-1][b+1] = 3

				if (a != (height-1)) and (b != (width-1)) and (board[a+1][b+1] == 0):
					board[a+1][b+1] = 1
				elif (a != (height-1)) and (b != (width-1)) and (board[a+1][b+1] == 1):
					board[a+1][b+1] = 2
				elif (a != (height-1)) and (b != (width-1)) and (board[a+1][b+1] == 2):
					board[a+1][b+1] = 3

## Print board
for x in range(height):
	print(*board[x])