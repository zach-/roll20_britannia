from wand.image import Image
from glob import glob
from re import search


def main():
    static_list = glob('../statics/*.bmp')
    for static in static_list:
        num = search('\d.+\.', static)
        num = int(str(num.group(0))[:-1], 0)
        with Image(filename=static) as img:
            img.format('png')
            img.transparent_color('#ffffff')
            img.rotate(45)
        filename = '../statics_nonrotated/static_' + str(num) + '.png'
        img.save(filename=filename)


if __name__ == '__main__':
    main()
