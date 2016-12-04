import json
from PIL import Image, ImageTk
from cv2 import imread, imwrite
from numpy import zeros
from tkinter import Toplevel, Label
from glob import glob
import os


def test():
    win = Toplevel()
    path = r'C:\Users\zbric\Code\Python\roll20_britannia\tileset'
    COLUMNS = 10
    image_count = 0
    for infile in glob(os.path.join(path, '*.jpg')):
        image_count += 1
        r, c = divmod(image_count - 1, COLUMNS)
        im = Image.open(infile)
        tkimage = ImageTk.PhotoImage(im)
        myvar = Label(win, image=tkimage)
        myvar.image = tkimage
        myvar.grid(row=r, column=c, padx=0, pady=0)
    win.mainloop()


def main():
    dir = '../tileset/tile_'
    ext = '.jpg'
    tuple_list = []
    new_img = Image.new('RGB', (4960, 3968))
    with open('../map_json/WriteMap10.txt') as json_data:
        data = json.load(json_data)

    for x in xrange(len(data)):
        tupl = (data[x]["CoordX"], data[x]["CoordY"], data[x]["ID"])
        tuple_list.append(tupl)

    for t in xrange(len(tuple_list) / 1024):
        img = Image.open(dir + str(tuple_list[t][2]) + ext)
        for x in xrange(0, 4960, 31):
            for y in xrange(0, 3968, 31):
                print(t)
                new_img.paste(img, (x, y))

    new_img.show()

    # print tuple_list
# test()

# json format: {"CoordX":544,"CoordY":0,"Name":"water","ID":170,"CoordZ":-5}


if __name__ == '__main__':
    main()
