from PIL import Image
import numpy as np

def genera_img(name, data):
    img = Image.fromarray(data.reshape(28, 28), 'L')
    img.save(name)

def main():
    tamano = 28 * 28
    archivo_csv = open('dataset2.csv', 'r')
    lineas = archivo_csv.readlines()
    data = []
    for n in range(1, 41): 
        if (len(data) == 0):
            data = np.array([int(s) for s in lineas[n].split(',')])
        else:
            data = np.vstack((data, np.array([int(s) for s in lineas[n].split(',')])))

    media = np.average(data, axis=0)
    moda = np.median(data, axis=0)
    desviacion_std = np.std(data, axis=0)

    genera_img('ejercicio1/media_2.png', media)
    genera_img('ejercicio1/moda_2.png', moda)
    genera_img('ejercicio1/desviacion_std_2.png', desviacion_std)
    resultado_csv = open('ejercicio1/resultado_numpy_2.csv', 'w')
    resultado_csv.write('columna,')
    for n in range(tamano):
        resultado_csv.write('c{}'.format(n) + (',' if n < (tamano - 1) else '\n'))
    resultado_csv.write('media,')
    for n in range(tamano):
        resultado_csv.write('{}'.format(media[n]) + (',' if n < (tamano - 1) else '\n'))
    resultado_csv.write('moda,')
    for n in range(tamano):
        resultado_csv.write('{}'.format(moda[n]) + (',' if n < (tamano - 1) else '\n'))
    resultado_csv.write('desviacion_std,')
    for n in range(tamano):
        resultado_csv.write('{}'.format(desviacion_std[n]) + (',' if n < (tamano - 1) else '\n'))
    resultado_csv.close()

if __name__ == "__main__":
    main()
