# Images with Python
The pillow library is a fork of the PIL (Python Imaging Library), which easy to use function calls. 
```py
from PIL import Image # pip install pillow
image_file = Image.open('examples/cat.jpg')
# image_file.show() # this opens the image to view
print(image_file.size) # (481, 480) # print out the size of the image
print(image_file.filename) # cat.jpg 
print(image_file.format_description) # JPEG (ISO 10918)
image_file.crop((0, 0, 100, 200)).show() # origin is top left corner. start from origin, width = 100px, and hight = 200px. returns the cropped file. 
cropped_file = image_file.crop((50, 50, 100, 200))
image_file.paste(im=cropped_file, box=(0, 0)) # put cropped_file at origin of the image_file, modify image_file in-place
image_file.show()
image_file.resize((2000, 300)).show() # stretch this file, return a stretched file
image_file.rotate(90).show() # rotate this image by 90 deg, return a new file

red = Image.open('red.jpg') # opens a red image
blue = Image.open('blue.jpg') # opens a blue image
blue.putalpha(128) # changes the transparency of this image in place. 0 is complete transparent, 255 is not transparent at all
red.putalpha(128) 
blue.paste(im=red, box=(0, 0)) # paste red on top of blue, now blue is a purple image
blue.save('purple.png') # save this image as file, overwrite if already exists
```



























