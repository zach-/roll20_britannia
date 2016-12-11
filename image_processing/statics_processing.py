from PIL import Image
from glob import glob
from re import search


def main():
    tile_list = glob('../statics_resized/*.png')
    for tile in tile_list:
        num = search('0x.+?\.', tile)
        num = int(str(num.group(0))[:-1], 0)
        print(num)
        # im = Image.open(tile)
        # im = im.rotate(45)
        # filename = '../statics_resized/static_' + str(num) + '.png'
        # im.save(filename)


if __name__ == '__main__':
    main()
