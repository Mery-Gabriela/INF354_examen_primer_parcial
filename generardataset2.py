from PIL import Image

def main():
    tamano = 28 * 28
    archivo_csv = open("dataset2.csv", "a")
    for n in range(tamano):
        archivo_csv.write('c{}'.format(n) + (',' if n < (tamano - 1) else '\n'))
    for n in range(1, 41):
        im = Image.open('fashionmnist/{}.png'.format(n), 'r')
        pixel_values = list(im.getdata())
        for i in range(tamano):
            archivo_csv.write(str(pixel_values[i]) + (',' if i < (tamano - 1) else '\n'))
    archivo_csv.close()

if __name__ == "__main__":
    main()
