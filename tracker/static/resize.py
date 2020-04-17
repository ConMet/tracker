#Background image resizing script

from PIL import Image

image = Image.open('background.gif')
image.thumbnail((2000,2750))

image.save('background.png')


