from PIL import Image
from glob import glob
from re import search


def main():
    tile_list = glob('../statics_resized/*.png')
    for tile in tile_list:
        num = search('0x.+?\.', tile)
        num = int(str(num.group(0))[:-1], 0)
        im = Image.open(tile)
        im = im.rotate(45)
        im = im.resize((44, 44), Image.ANTIALIAS)
        box = (7, 7, 38, 38)
        im = im.crop(box)
        filename = '../static_final/static_' + str(num) + '.png'
        im.save(filename)


if __name__ == '__main__':
    main()
