## In_Class_Coin_Flip
## January 7, 2018
## Program that calculates the number of times 'heads' is present during X amount of coin flips

import random

numFlips = int(1000/10)
whatAmI = 0
zeroThruTen = 0
bellCurve = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in range(0, numFlips):
	whatAmI = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
	if (whatAmI == 0):
		bellCurve[0] += 1
	if (whatAmI == 1):
		bellCurve[1] += 1
	if (whatAmI == 2):
		bellCurve[2] += 1
	if (whatAmI == 3):
		bellCurve[3] += 1
	if (whatAmI == 4):
		bellCurve[4] += 1
	if (whatAmI == 5):
		bellCurve[5] += 1
	if (whatAmI == 6):
		bellCurve[6] += 1
	if (whatAmI == 7):
		bellCurve[7] += 1
	if (whatAmI == 8):
		bellCurve[8] += 1
	if (whatAmI == 9):
		bellCurve[9] += 1
	if (whatAmI == 10):
		bellCurve[10] += 1
print(*bellCurve)