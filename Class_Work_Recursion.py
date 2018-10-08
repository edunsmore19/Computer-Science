## Class_Work_Recursion.py
## October 8, 2018
## Introducing recursion




def fact(n):
	if n is 0 or n is 1:
		return 1
	neturn n*fact(n-1)

def fib(n)
	if n is 0 or n is 1:
		return n
	return fib(n-1) + fib(n-2)