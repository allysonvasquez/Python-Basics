# author: Allyson Vasquez
# version: June.13.2020
# Resizes photos into poster format
from PIL import Image, ImageEnhance
import os

os.chdir('original_pictures')
poster_size = (1500, 2100)
sharpness = 3.0

for f in os.listdir('.'):
    i = Image.open(f)
    img_name, img_format = os.path.splitext(f)
    img_resize = i.resize(poster_size)
    enhanced_sharp = ImageEnhance.Sharpness(img_resize)
    img_modified = enhanced_sharp.enhance(sharpness)
    img_modified.save('/Users/allysonvasquez/Documents/Code/PyCharm Projects/Python-Basics/3-Side Projects/PosterResizer/pngs/{}.png'.format(img_name))
    print(i.filename, 'converted...')
print('complete.')