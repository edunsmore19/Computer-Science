## Class_Work_Mandelbrot_Together
## October 19, 2018
## Class-created program to do what mine did but much better.

from PIL import Image

xa, xb = -1.233398, -1.0575758
ya, yb = 0.1875, 0.369140625

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

		r = (252 * i) % 255
		g = (80 ** i) % 255
		b = 3

		image.putpixel((x, y), (r, g, b))

## Makes image pop up but doesn't save
image.show()