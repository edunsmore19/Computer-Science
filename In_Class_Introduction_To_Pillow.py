## In_Class_Introduction_To_Pillow
## October 10, 2018

from PIL import Image

imgx = 512
imgy = 512

image = Image.new("RGB", (imgx, imgy))

image.putpixel((0, 0), (255, 0, 0))

image.save("demo_image.png", "PNG")