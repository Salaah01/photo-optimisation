from __future__ import print_function
import sys
import os
from PIL import Image
import img_extentions


class Optimise():
    """
    Will take a photo and optimise the photo in accordance to what the user's needs are.
    """

    def __init__(self, photo):
        self.photo = photo
        self.orig_img = Image.open(photo)
        self.orig_width = self.orig_img.size[0]
        self.orig_height = self.orig_img.size[1]
        self.optimize = False
        self.quality = 100

        def check_if_img(self):
            if not(os.path.splitext(self.photo)[1] in img_extentions.extentions):
                raise Exception('The uploaded file is not a supported file type')

    def save(self):
        self.img.save('resized_' + self.photo, optimize=self.optimize, quality=self.quality)

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
    
    def change_format(self, extention):
        self.photo = os.path.splitext(self.photo)[0] + extention

    def optimise(self, opt):
        if opt == True:
            self.optimise = opt

    def change_quality(self, quality):
        try:
            self.quality = int(quality)
        except:
            pass


img = Optimise('test-pic.jpg')
img.change_format('.bmp')
img.resize(height=300)
img.optimise = True
img.quality = 10
img.save()
Image.open('test-pic.jpg')