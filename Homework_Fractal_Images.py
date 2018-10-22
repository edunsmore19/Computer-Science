## Homework_Fractal_Images
## October 21, 2018
## Program that draws fractals with Pillow, producing three fractal images, two
## mandelbrot sets and one Julia set.

import random
from PIL import Image

global goAgain
goAgain = 0

## Code generates Mandelbrot sets
def generateMandelbrot():
	## Code to change coordinates the second time around
	global goAgain
	if (goAgain == 0):
		print("goAgain:", goAgain)
		xa, xb = -1.233398, -1.0575758
		ya, yb = 0.1875, 0.369140625
	elif (goAgain == 1):
		print("goAgain:", goAgain)
		xa, xb = -1.7477612625807524, -1.745780685916543
		ya, yb = -0.00505908764898777, -0.0030785109847784042
	else:
		print("goAgain:", goAgain)
		print("Killing me...")
		julia()

	imgx, imgy = 512, 512

	maxIt = 256

	image = Image.new("RGB", (imgx, imgy))

	for y in range(imgy):
		cy = y * (yb-ya)/(imgy-1) + ya
		for x in range(imgx):
			cx = x * (xb-xa)/(imgx-1) + xa
			c = complex(cx, cy)
			z = 0
			for i in range(maxIt):
				if abs(z) >= 2.0:
					break
				z = z**2 + c
			if (goAgain == 0):
				print("choosing color")
				r = (252 * i) % 255
				g = (80 ** i) % 255
				b = 3
			elif (goAgain == 1):
				print("choosing color again")
				r = (100 * i) % 255
				g = (20 ** i) % 255
				b = 65

			image.putpixel((x, y), (r, g, b))

	## Generate image
	image.show()
	## Code to repeat the program for the second fractal
	goAgain+= 1
	generateMandelbrot()

## Code generates Julia set
def julia():
	exit()

## Generates fractals
generateMandelbrot()