from PIL import Image
import os
import sys


def main():
    im = Image.open('../tileset/Landtile 1004.bmp')
    print(im.format, im.size, im.mode)


if __name__ == '__main__':
    main()
