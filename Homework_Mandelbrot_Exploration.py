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

z = [0, 0]
c = [-2, 2]
zSquared = []
zAndC = []

## Set size of image
image = Image.new("RGB", (512, 512))

## Calculate equations
def run():
	## Equations
	## Find z^2
	zSquared.append(z[0]**2 - z[1]**2)
	zSquared.append(2*z[0]*z[1])
	print("ZSquared:", zSquared)
	## Find z + c
	zAndC.append(zSquared[0] + c[0])
	zAndC.append(zSquared[1] + c[1])
	del zSquared[0:2]
	print("ZSquared:", zSquared)
	print("zAndC:", zAndC)
	check()

## Checks to see if z has escaped
def check():
	global timesEscaped
	timesEscaped = 0
	## Check if z escaped
	if (((zAndC[0]**2 + zAndC[1]**2)**1/2) >= 2):
		print("Value of Z:", ((zAndC[0]**2 + zAndC[1]**2)**1/2))
		print("Z has escaped.")
		del zAndC[0:2]
		print("zAndC:", zAndC)
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
		## Draw pixel
		print("draw pixel")
		image.putpixel((z[0], z[1]), (red, green, blue))
	else:
		timesEscaped+= 1
		print("timesEscaped:", timesEscaped)
	if (timesEscaped >= 3):
		print("timesEscaped has reached its limit")
		exit()
	## Redirect to newNumber for a new set of coordinates
	newNumber()

## Changes 'c' and then rerouts to do calculation over again
def newNumber():
	## Edits the x coordinate of 'c'
	for a in range(0, 3):
		print("Check")
		## Edits the y coordinate of 'c'
		for b in range(0, 3):
			print("2nd Check")
			print("c:", c)
			print("b:", b)
			if (c[0] == (-2)) and (c[1] == 2):
				c[1] = c[1] - 2
			if (b != 0):
				c[1] = c[1] - 2
			print("c:", c)
			print("Redirecting...\n\n")
			run()
		print("3rd Check")
		c[0] = c[0] + 2
		c[1] = 2



## Save name/file type
image.save("Homework_Mandelbrot_Exploration.png", "PNG")

## Test print
print("z:", z)
print("c:", c)
## Run program
run()