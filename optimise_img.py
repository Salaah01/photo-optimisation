from __future__ import print_function
import sys
from PIL import Image

class Optimise():
    """
    Will take a photo and optimise the photo in accordance to what the user's needs are.
    """

    def __init__(self, photo):
        self.photo = photo
        self.orig_img = Image.open(photo)
        self.orig_width = self.orig_img.size[0]
        self.orig_height = self.orig_img.size[1]
        
    def save(self, optimize=False, quality=100):
        self.img.save('resized_' + self.photo, optimize=optimize, quality=quality)

    def resize(self, width='auto', height='auto'):
        """
        Will resize an image.
        width: set width in pixels or auto to keep aspect ratio.
        height: set height in pixels or auto to keep aspect ratio.
        """

        # Check if there is a integer value for width and height
        
        try:
            int(width)>0
            width = int(width)
            width_input = True
        except:
             width_input = False 

        try:
            int(height)>0
            height = int(height)
            height_input = True
        except:
            height_input = False

        if width_input and height_input:
            self.img = self.orig_img.resize((width, height), Image.ANTIALIAS)
        
        elif height_input:
            ratio = height / self.orig_height
            self.img = self.orig_img.resize(
                (
                    int(self.orig_width * ratio),
                    height
                ),
                Image.ANTIALIAS
            )

        elif width_input:
            ratio = width / self.orig_width
            self.img = self.orig_img.resize(
                (
                    width,
                    int(self.orig_height * ratio)
                ),
                Image.ANTIALIAS
            )

        else:
            raise Exception('You must enter at least a width or a height.\nwidth={}\nheight={}', format(width, height))



x = Optimise('test-pic.jpg')
x.resize('auto',1010)
x.save(False, 10)
