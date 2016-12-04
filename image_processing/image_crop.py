from PIL import Image
from glob import glob
from re import search


def main():
    tile_list = glob('../tileset/*.bmp')
    for tile in tile_list:
        num = search('\d+', tile)
        im = Image.open(tile)
        box = (7, 7, 38, 38)
        im = im.crop(box)
        filename = '../tileset/processed/tile_' + str(num.group(0)) + '.jpg'
        im.save(filename)


if __name__ == '__main__':
    main()
