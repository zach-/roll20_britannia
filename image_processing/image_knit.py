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
    file_list = glob('../map_json/*.txt')
    dir = '../tileset/tile_'
    ext = '.jpg'
    coorx = 9920
    coory = 15872
    for file in file_list:
        num = search('\d+', file)
        new_img = Image.new('RGB', (coorx, coory))
        with open(file) as json_data:
            data = json.load(json_data)
        change_values(data)
        for cell in xrange(len(data)):
            try:
                img = Image.open(dir + str(data[cell]["ID"]) + ext)
        # img = Image.open(dir + cell["ID"] + ext)
                new_img.paste(img, (data[cell]["X"] * 31,
                                    data[cell]["Y"] * 31))
        # new_img.paste(img, (cell["X"], cell["Y"]))
            except IOError as err:
                print err
            filename = './map_json/world_file_' + str(num.group(0)) + '.jpg'
            new_img.save(filename)
    # for x in xrange(len(data)):
    #     tupl = (data[x]["ID"])
    #     tuple_list.append(tupl)
    #
    # for y in xrange(0, coory, 31):
    #     for x in xrange(0, coorx, 31):
    #
    #         new_img.paste(img, (x, y))
    #
    # new_img.show()

    # print tuple_list
# test()

# json format: {"CoordX":544,"CoordY":0,"Name":"water","ID":170,"CoordZ":-5}


if __name__ == '__main__':
    main()
