## In_Class_Matplotlib
## January 9, 2019
## Using the matplot library

import random
import matplotlib.pyplot as plt

results = []
for j in range(1000):
	total = 0
	for i in range(10):
		flip = random.randint(0, 1)
		total += flip
	results.append(total)

display = [0 for i in range(11)]
for i in range(len(results)):
	display[results[i]] += 1

r = [x for x in range(5, 16)]
d = [x for x in range(5, 16)]

## Plotting two dashed lines on top of each other lines
#plt.plot(r, display, 'r--', r, d, 'g--')

## Creating a bar graph
## Last value is the opacity (Alpha)
plt.bar(r, display, color = (.5, 0, 0.5, 1))
## Creat y & x labels
plt.ylabel("Number of Trials")
plt.xlabel("Number of Heads")
plt.show()