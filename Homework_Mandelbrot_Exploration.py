## Homework_Mandelbrot_Exploration
## October 18, 2018
## A program that will draw the basic mandelbrot set.

from PIL import Image

## Initialize variables
global red
red = 0
global green
green = 0
global blue
blue = 0

global timesEscaped
timesEscaped = 0

numRange = [-2, 2]
z = [0, 0]
c = []
zSquared = []
zAndC = []
tempC = [-2, 2]
killerC = []

## Set size of image
image = Image.new("RGB", (500, 500))

## Generates a list of numbered pairs for 'c' to run through
def generateNumbers():
	## Declaring global 'itHasBegun' so program knows when to skip (-2,2)
	global itHasBegun
	itHasBegun = False
	for a in range(0, 3):
		for b in range(0, 3):
			## Skips first pair b/c (-2,2) is already included in list
			if (tempC[0] == (-2)) and (tempC[1] == 2) and (itHasBegun == False):
				tempC.append(tempC[0] + 2)
				tempC.append(tempC[1])
				killerC.append(tempC[2])
				killerC.append(tempC[3])
				itHasBegun = True
			## If b is not in its first iteration and killerC[0] isn't 2
			if (b != 0) and (killerC[0] < 2):
				killerC[0]+= 2
				tempC.append(killerC[0])
				tempC.append(killerC[1])
			## If b is zero and killerC[1] isn't two
			elif (b == 0) and (killerC[1] != 2):
				tempC.append(killerC[0])
				tempC.append(killerC[1])
		killerC[0] = (-2)
		killerC[1]-= 2
	## Reroutes to 'run' in order to calculate equations
	run()

## Calculate equations
def run():
	## If 'tempC' runs out of pairs, end program
	if (len(tempC) == 0):
		print("tempC is empty & you have no more pairs.")
		exit()
	## Equations
	## Find z^2
	zSquared.append(z[0]**2 - z[1]**2)
	zSquared.append(2*z[0]*z[1])
	print("\nZSquared:", zSquared)
	print("tempC:", tempC)
	## If 'z' has not ever escaped before, append first two values of 'tempC'
	## to 'c' & then delete f/ 'tempC'
	if (timesEscaped == 0):
		c.append(tempC[0])
		c.append(tempC[1])
		del tempC[0:2]
	print("c:", c)
	## Now find z + c
	zAndC.append(zSquared[0] + c[0])
	zAndC.append(zSquared[1] + c[1])
	print("zAndC:", zAndC)
	check()

## Checks to see if z has escaped
def check():
	global timesEscaped
	## Check if z escaped
	if (((zAndC[0]**2 + zAndC[1]**2)**1/2) >= 2):
		print("Value of Z:", ((zAndC[0]**2 + zAndC[1]**2)**1/2))
		print("Z has escaped.")
		## Clean up extra 'zAndC' values
		del zAndC[0:2]
		print("zAndC:", zAndC)
		## Clean up extra 'zSquared' values
		del zSquared[0:]
		print("zSquared:", zSquared)
		## Reroute to 'drawPixel'
		drawPixel()
	else:
		timesEscaped+= 1
		print("timesEscaped:", timesEscaped)
		## Clean up extra 'zAndC' values
		del zAndC[0:2]
		print("zAndC:", zAndC)
		## Clean up extra 'zSquared' values
		del zSquared[0:]
		print("zSquared:", zSquared)
		## Kill-command for if 'z' escapes more than 3 times
		if (timesEscaped >= 3):
			print("timesEscaped has reached its limit")
			## Redirects to 'drawPixel'
			drawPixel()
		run()

## WILL NOT DRAW PIXEL
## Draws pixel
def drawPixel():
	global timesEscaped
	c[0]*()
	x*(xb-xa)/(imgx-1)+xa




	## Give 'c' coordinates real life x/y counterparts
	x = 250
	x+= c[0]
	y = 250
	y+= c[1]
	del c[0:2]
	print("x:", x, "y:", y)
	## Determine color
	if (timesEscaped == 0):
		red = 255
		green = 0
		blue = 0
	elif (timesEscaped == 1):
		red = 0
		green = 255
		blue = 0
	elif (timesEscaped == 2):
		red = 0
		green = 0
		blue = 255
	## Print pixel
	image.putpixel((x, y), (255, 0, 0))
	## Reset 'timesEscaped' to present as 0 again
	timesEscaped = 0
	## Redirect back to 'run'
	run()

## Save name/file type
image.putpixel(250, 250), (255, 0, 0)
image.save("Homework_Mandelbrot_Exploration.png", "PNG")

## Run program
generateNumbers()