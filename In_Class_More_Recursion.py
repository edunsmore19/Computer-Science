## In_Class_More_Recursion
## October 10, 2018
## Recursion as w/ the Towers of Hanoi

def moves(n, left):
	if (n == 0):
		return
	moves(n-1, not left)
	if (left):
		print(str(n), "left")
	else:
		print(str(n), "right")
	moves(n-1, not left)

## In parentheses whatever is in = provides the values for the function variables
moves(3, True)