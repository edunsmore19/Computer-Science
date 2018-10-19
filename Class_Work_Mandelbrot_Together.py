## Class_Work_Mandelbrot_Together
## October 19, 2018
## Class-created program to do what mine did but much better.

from PIL import Image

xa, xb = -2.0, 2.0
ya, yb = -2.0, 2.0

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

		r = (i * 35) % 55
		g = 10 - i
		b = (200 * i) % 255

		image.putpixel((x, y), (r, g, b))

## Makes image pop up but doesn't save
image.show()