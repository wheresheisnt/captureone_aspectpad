"""
This program gives an image a frame, padding it out to a specified aspect ratio, center & colour.
The defaults are an instagram friendly aspect ratio of 1080 * 1350 and a black background.
Colour can be changed by passing the name of one in to add_padding.


Copy and paste the following into an automator "shell script" command.
Shell must be set to "bin/bash" and Pass Input must be set to "as argument"

/usr/local/bin/python3 [your path] "$1"

"your path" can be found by dragging this python file onto a terminal window and copy-pasting the
output. Don't forget to remove the [] surrounding [your path]!

"""

import os
import argparse
from sys import argv
from PIL import Image, ImageOps


def add_padding(image, aspect_ratio, colour, center):
    img = Image.open(image)

    if not isinstance(aspect_ratio, tuple) and not isinstance(center, tuple):
        raise RuntimeError("aspect_ratio and center are not tuples!")

    elif not isinstance(aspect_ratio, tuple):
        raise RuntimeError("aspect_ratio is not a tuple!")

    elif not isinstance(center, tuple):
        raise RuntimeError("centre is not a tuple!")

    else:
        bimg = ImageOps.pad(img, aspect_ratio, method=3, color=colour, centering=center)

    bimg.save(image)


parser = argparse.ArgumentParser()
parser.add_argument("path", type=str)
args = parser.parse_args()
filename = args.path


# leave filename!! it will break.
# border is whatever aspect ratio you want it to be (in px), in the form (width, height).
# colour is the usual, i.e. pass 'black', 'white', 'yellow', 'green', 'red' etc.
# center is where the image sits. it is in the form (horizontal, vertical). (0.5, 0.5) will keep
# the image centered. (0, 0) will keep the image aligned to the top left. (1, 1) will keep the image
# aligned to the bottom right.

add_padding(filename, aspect_ratio=(1080, 1350), colour='black', center=(0.5, 0.5))


