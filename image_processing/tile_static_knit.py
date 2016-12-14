import json
from PIL import Image, ImageTk
from cv2 import imread, imwrite
from numpy import zeros, unique
from tkinter import Toplevel, Label
from glob import glob
import os
from re import search


def main():
    file_list = glob('../map_images/world_statics_*.png')
    dir = '../map_images/world_file_'
    ext = '.jpg'
    coorx = 9920
    coory = 15872
    for file in file_list:
        num = search('\d+', file)
        fmap = dir + str(num.group(0)) + ext
        map = Image.open(fmap)
        map = map.convert('RGBA')
        static = Image.open(file)
        print('Started processing world file ' + str(num.group(0)))
        new_img = Image.new('RGBA', (coorx, coory))
        new_img = Image.alpha_composite(map, static)
        filename = '../final_images/world_final_' + str(num.group(0)) + '.jpg'
        new_img.save(filename)
        print('Finished processing world file ' + str(num.group(0)))


if __name__ == '__main__':
    main()
