import sys
import os
from PIL import Image
import img_extentions


class Optimise():
    """
    Will load a photo and optimise in accordance to the user input.
    """

    def __init__(self, photo):
        self.photo = photo
        self.orig_img = Image.open(photo)
        self.img = self.orig_img
        self.orig_width = self.orig_img.size[0]
        self.orig_height = self.orig_img.size[1]
        self.optimize = False
        self.quality = 100

        def check_if_img(self):
            if not(os.path.splitext(self.photo)[1] in img_extentions.extentions):
                raise Exception('The uploaded file is not a supported file type')

    def save(self, save_dir):

        base_filename = os.path.basename(self.photo)
        save_path = os.path.join(save_dir, 'resized_' + base_filename)

        if os.path.isfile(save_path):
            save_path_exists = True
            path_pre = os.path.splitext(save_path)[0]
            path_extention = os.path.splitext(save_path)[1]

            counter = 0
            while save_path_exists:
                
                counter += 1
                save_path = f"{path_pre} ({counter}){path_extention}"
                
                if not(os.path.isfile(save_path)):
                    save_path_exists = False                

        self.img.save(save_path, optimize=self.optimize, quality=self.quality)

    def resize(self, width='auto', height='auto'):
        """
        Will resize an image.
        width: set width in pixels or auto to keep aspect ratio.
        height: set height in pixels or auto to keep aspect ratio.
        """

        # Check if there is a integer value for width and height
        
        try:
            if int(width)>0:
                width = int(width)
                width_input = True
            else:
                width_input = False
        except:
             width_input = False 

        try:
            if int(height)>0:
                height = int(height)
                height_input = True
            else:
                height_input = False
        except:
            height_input = False

        if width_input and height_input:
            self.img = self.img.resize((width, height), Image.ANTIALIAS)
        
        elif height_input:
            ratio = height / self.orig_height
            self.img = self.img.resize(
                (
                    int(self.orig_width * ratio),
                    height
                ),
                Image.ANTIALIAS
            )

        elif width_input:
            ratio = width / self.orig_width
            self.img = self.img.resize(
                (
                    width,
                    int(self.orig_height * ratio)
                ),
                Image.ANTIALIAS
            )

        else:
            pass
    
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

def run_optimisation(img_file, save_dir, **kwargs):
    img = Optimise(img_file)

    # Auto
    if 'auto' in kwargs:
        auto = int(kwargs['auto'])

        if auto:
            img.quality = 80
    
    else:

        # Change Format
        if 'new_format' in kwargs:
            new_format = kwargs['new_format']
            if new_format in img_extentions.keys:
                img.change_format(img_extentions.formats[new_format]['extension'])
        
        # Change Size
        if 'resize' in kwargs:
            new_size = kwargs['resize']
            print(new_size)
            if len(new_size) == 2 and isinstance(new_size[0], int) and isinstance(new_size[1], int):
                img.resize(width=new_size[0], height=new_size[1])
        
        # Quality
        if 'quality' in kwargs:
            quality = int(kwargs['quality'])
            if quality < 100:
                img.quality = quality
    
    return img.save(save_dir)

# img_file = 'testimg.jpg'
# run_optimisation(img_file=img_file, save_dir="C:\\Users\\Salaah\\Documents\\Portfolio\\Image Optimisation\\image-optimisation\\code", new_format="JPEG", quality=80)