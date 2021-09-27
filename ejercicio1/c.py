# import tkinter

from PIL import Image

import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

def main():
    dataset = 1

    for i in range(1, 11):
        im = Image.open('{}/{}.png'.format('mnist' if dataset == 1 else 'fashionmnist', i), 'r')
        plt.subplot(3, 5, i)
        plt.imshow(im, cmap='gray')

    im = Image.open('ejercicio1/media_{}.png'.format(dataset), 'r')
    plt.subplot(3, 5, i)
    i = i + 1
    plt.imshow(im, cmap='gray')
    im = Image.open('ejercicio1/moda_{}.png'.format(dataset), 'r')
    plt.subplot(3, 5, i)
    i = i + 1
    plt.imshow(im, cmap='gray')
    im = Image.open('ejercicio1/desviacion_std_{}.png'.format(dataset), 'r')
    plt.subplot(3, 5, i)
    i = i + 1
    plt.imshow(im, cmap='gray')

    plt.show()

if __name__ == "__main__":
    main()
