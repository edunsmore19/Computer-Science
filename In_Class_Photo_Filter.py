## In_Class_Photo_Filter
## Honor Code: I have neither given nor recieved any unauthorized aid.
## Sources:
## Figuring out how to load a given image & find pixel values in rgb for an already
## rendered image.
## https://stackoverflow.com/questions/138250/how-can-i-read-the-rgb-value-of-a-given-pixel-in-python
## November 12, 2018
## Add a filter/effect to a photo of the user's choosing.

import sys
import colorsys
from PIL import Image

## Initialize variables
imageName = sys.argv[1]
image = Image.open(imageName)
width, height = image.size

## Show the image!
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
			r = b
			g = r
			b = g
		image.putpixel((x, y), (r, g, b))


image.show()


print(imageName)
print(image)
print(width)
print(height)