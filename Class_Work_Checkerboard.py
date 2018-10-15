## Class_Work_Checkerboard
## October 15, 2018
## Creating a checkerboard using the 'Pillow' class

from PIL import Image

sizeX = 501
sizeY = 501

x = 0
y = 0

whiteOrBlack = 0

add = 0

image = Image.new("RGB", (sizeX, sizeY))
for y in range(0, 501):
	for x in range(0, 501):
		print(x, y)
		print(whiteOrBlack)
		if (x <= 50 + add):
			if (y <= 50 + add):
				whiteOrBlack = 255
			elif (y <= 100 + add):
				whiteOrBlack = 0
			elif (y <= 150 + add):
				whiteOrBlack = 255
			elif (y <= 200 + add):
				whiteOrBlack = 0
			elif (y <= 250 + add):
				whiteOrBlack = 255
			elif (y <= 300 + add):
				whiteOrBlack = 0
			elif (y <= 350 + add):
				whiteOrBlack = 255
			elif (y <= 400 + add):
				whiteOrBlack = 0
			elif (y <= 450 + add):
				whiteOrBlack = 255
			elif (y <= 500 + add):
				whiteOrBlack = 0
		image.putpixel((x, y), (whiteOrBlack, whiteOrBlack, whiteOrBlack))





#for y in range(0, 51):
#	for x in range(0, 51):
#		print(x, y)
#		image.putpixel((x, y), (255, 255, 255))
#for y in range(0, 51):
#	for x in range(51, 101):
#		print(x, y)
#		image.putpixel((x, y), (100, 20, 73))

image.save("Class_Work_Checkerboard.png", "PNG")