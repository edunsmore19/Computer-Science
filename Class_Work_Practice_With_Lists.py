## Class_Work_Practice_With_Lists
## September 26, 2018
## Some practice with lists

## An 'empty list' is a list with nothing in it
a = []

## Adding the int 2 to the end of the list, which was previously empty
a += [2]

## list.append command adds stuff to the END of the list
a.append(4)
a.append(7)
a.append(1)
print(a)

## Adding the stuff in [brackets] to a puts it in front of what
## was previous included in a in the list, essentially putting it
## at the START of the list
a = [2, 1, 2, 3, 4, 5] + a
print(a)

## Update a value based on its position (4) and replace it w/ (7)
a[4] = 7

## Print the list
print(a)

## To remove something from the list
## 1-5 is the range, inclusive of 1, not of 5
	##del a[1:5]
## To delete just the thing in position 5
	##del a[5]
## To delete everything 5 and after
	##del a[5:]
## To delete everything before 5 (not including 5)
	##del a[:5]

## To take something out of a list but still be able to do something
## with it
a.pop()
print(a)
print(a.pop())

## To remove something, but it's not about positions, it's about
## essentially search and delete your content & it takes it
## literally, and it removes the first thing it sees that matches it
a.remove(2)
print(a)

## Access an element in the list
print(a[3])
print(a[len(a)-1]) 
## Short cut for above to print the last thin in the list
print(a[-1])
## To print second to last (a[-2]) and so on

## How to switch things using temporary variables
x = 1
b = 5

temp = x
x = b
b = temp

x,b = 1, 5
x,b = b,x
print(x,b)

## How to switch things in lists using the same method
a[3],a[5] = a[5],a[3]
print(a)

###############

sevens = []
count = 0
while count <= 700:
	sevens.append(count)
	count += 7
print(sevens, len(sevens))

########

sevens = []
for x in range(0, 700, 7):
	sevens.append(x)
print(sevens, len(sevens))

########

sevens = [x for x in range(0, 700, 7)]
print(sevens, len(sevens))
## 'list comprehention'

#########
sevens = []
for i in range(100):
	sevens.append(7*1)


## range(5) = 0-4
## range(5,8) = 5-7
print("\n\n\n\n\n\n")
yesPrime = False
prime = []
print(prime)
for i in range(1, 11):
	##print("i:", i)
	for checker in range(2, 11):
		isItPrime = i % checker
		##print("checker:",checker)
		##print("isItPrime:",isItPrime)
		if (isItPrime != 0):
			yesPrime = True
	if (yesPrime == True):
		prime.append(i)
		yesPrime = False
print(prime)


