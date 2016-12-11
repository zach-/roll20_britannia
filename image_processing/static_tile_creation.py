import json
from PIL import Image, ImageTk
from cv2 import imread, imwrite
from numpy import zeros, unique
from tkinter import Toplevel, Label
from glob import glob
import os
from re import search


def change_values(data):
    removex = data[0]["X"]
    removey = data[0]["Y"]
    for cell in data:
        cell["X"] = cell["X"] - removex
        cell["Y"] = cell["Y"] - removey


def main():
    file_list = glob('../map_json/DungeonMapStatics*.txt')
    dir = '../static_final/static_'
    ext = '.png'
    coorx = 7936
    coory = 8091
    for file in file_list:
        num = search('\d+', file)
        print('Started processing wolrd file ' + str(num.group(0)))
        new_img = Image.new('RGBA', (coorx, coory))
        with open(file) as json_data:
            data = json.load(json_data)
        change_values(data)
        data = sorted(data, key=lambda k: int(k['Z']), reverse=False)
        for cell in xrange(len(data)):
            if (data[cell]["ID"] == 0):
                pass
            else:
                try:
                    img = Image.open(dir + str(data[cell]["ID"]) + ext)
        # img = Image.open(dir + cell["ID"] + ext)
                    new_img.paste(img, (data[cell]["X"] * 31,
                                        data[cell]["Y"] * 31))
        # new_img.paste(img, (cell["X"], cell["Y"]))
                except IOError as err:
                    print err
        filename = '../map_images/dungeon_statics_' + str(num.group(0)) + '.png'
        new_img.save(filename)
        print('Finished processing world file ' + str(num.group(0)))


if __name__ == '__main__':
    main()
