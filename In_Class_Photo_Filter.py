## In_Class_Photo_Filter
## Honor Code: I have neither given nor recieved any unauthorized aid.
## Sources:
## Figuring out how to load a given image & find pixel values in rgb for an already
## rendered image.
## https://stackoverflow.com/questions/138250/how-can-i-read-the-rgb-value-of-a-given-pixel-in-python
## November 12, 2018
## Add a filter/effect to a photo of the user's choosing.

import sys
import os
import colorsys
import math
from PIL import Image

os.system("open ~/Users/eilidh/Desktop/OneDrive\ Files/Documents\ \&\ Powerpoints/School/Twelfth\ Grade\;\ Choate/Computer\ Science/error.png")

## Initialize variables
imageName = sys.argv[1]
otherImage = Image.open('error.png')
image = Image.open(imageName)
width, height = image.size

## Show the image!
print("\n\n\n\nGet ready to corrupt!\n\n\n\n\n")
image.show()

## Muckin' about
for y in range(height):
	for x in range(width):
		colors = image.getpixel((x, y))
		r, g, b = colors
		## This forms grayscale
		#r = b
		#g = r
		#b = g
		if (g >= 150):
			r = (r ** 2) % 255
			g = r
			b = g
		if (r >= 150 ):
			g = r
		if (r >= 200):
			r = (r ** 3) % 255
		if (b >= 150):
			b = (b ** 3) % 255
		if (r >= 100):
			r = (r ** 3) % 255
		if (r >= 230) and (b >= 230) and (g >= 230):
			 r = math.random(0, 255)
			 b = math.random(0, 255)
			 g = math.random(0, 255)
		image.putpixel((x, y), (r, g, b))


image.show()
otherImage.show()
