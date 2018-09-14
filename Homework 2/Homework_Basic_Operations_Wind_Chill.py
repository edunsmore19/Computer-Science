## Class_Work_Basic_Operations_Wind_Chill
## September 12, 2018
## Program that takes two floats t & v from the command line and writes the wind chill.

import sys

## Importing variables from system line
temperature = sys.argv[1]
windSpeed = sys.argv[2]

## Wind chill computation
windChill = 35.74 + 0.6215 * float(temperature) + (0.4275 * float(temperature) - 35.75) * float(windSpeed) ** 0.16

## Variable print check
print("Temperature: ",sys.argv[1])
print("Wind Speed: ",sys.argv[2])
print("Wind Chill: ", windChill)