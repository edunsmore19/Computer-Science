## Homework_Fractal_Images
## October 21, 2018
## Program that draws fractals with Pillow, producing three fractal images, two
## mandelbrot sets and one Julia set.

import random
import colorsys
import math
from PIL import Image

global goAgain
goAgain = 0

## Code generates Mandelbrot sets
def generateMandelbrot():
	## Code to change coordinates the second time around
	global goAgain
	if (goAgain == 0):
		xa, xb = 0.3358112724851627, 0.3358112916849378
		ya, yb = 0.5781364408463064, 0.5781364600460815
	elif (goAgain == 1):
		xa, xb = -0.72914898404959059395, -0.729138958594958
		ya, yb = 0.210768863199801323939, 0.2107788614848048
	else:
		generateJulia()

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
			## Chooses color for first & second generation
			if (goAgain == 0):
				r = (252 * i) % 255
				g = (80 ** i) % 255
				b = 3
			elif (goAgain == 1):
				h = ((i**3)-(i**2))/256
				s = 1.0/i *100
				v = 1.0
				r,g,b = colorsys.hsv_to_rgb(h,s,v)

			## Makes sure that the first image isn't white w/ if-statement
			if (goAgain == 0):
				image.putpixel((x, y), (r, g, b))
			else:
				image.putpixel((x, y), (int(r*256), int(g*256), int(b*256)))

	## Generate image
	image.show()
	## Code to repeat the program for the second fractal
	goAgain+= 1
	generateMandelbrot()

## Code generates symmetrical Julia set, which is a sub-set ("lace") contained
## within the larger Mandelbrot set.
def generateJulia():
## Generate xab and yab points
	xa, xb = -0.40005, 0.4003335
	ya, yb = -0.40005, 0.4003335

## Basic image generation stuff
	imgx, imgy = 512, 512
	maxIt = 256
	image = Image.new("RGB", (imgx, imgy))

## Generation of symmetrical Julia set w/ equation
	for y in range(imgy):
		zy = y * (yb-ya)/(imgy-1) + ya
		for x in range(imgx):
			zx = x * (xb-xa)/(imgx-1) + xa
			## Change 'c' to equal an imaginary & real coordinate pair
			c = complex(-0.835, -0.2321)
			## Change the first 'z' value to equal the imaginary & real coordinates
			## Basically: let 'z' have a stab at it
			z = complex(zy, zx)
			for i in range(maxIt):
				if abs(z) >= 2.0:
					break
				z = z**2 + c

			## Chooses color
			r = (21 * i) % 255
			g = int((i ** 2) / 25)
			b = 100
			
			image.putpixel((x, y), (r, g, b))

	## Generate image
	image.show()
	exit()

## Generates fractals
generateMandelbrot()
#generateJulia()