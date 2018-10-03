## In_Class_More_List_Stuff
## September 28, 2018

i = [[1,2,3], [4, 5, 6], [7, 8, 9]]
## Indicates, go to the first list [0] and grab the first number [0]
i[0][0]

i = [0 for x in range(12)]

## Create a list w/ 12 sets of 0
## You could use this to go in later and change it
j = [0]*12
print(j)

## You can create a list w/ 10 sections of 10 zeros, 
i = [[0]*10 for x in range(10)]
print(i)

for x in range(len(i)):
	print(i[x])

## The asterisk 'unpacks' the list, taking away all the 
## brackets and commas
print(*i[x])