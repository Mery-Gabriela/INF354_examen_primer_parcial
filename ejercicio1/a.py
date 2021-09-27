import math

def main():
    archivo_csv = open('dataset2.csv', 'r')
    lineas = archivo_csv.readlines()
    tamano = 28 * 28
    suma = [0] * tamano
    valores = [None] * tamano
    media = [None] * tamano
    moda = [None] * tamano
    desviacion_std = [None] * tamano

    for n in range(1, 41):
        pixel_values = [int(s) for s in lineas[n].split(',')]
        for i in range(tamano):
            if (valores[i] == None):
                valores[i] = []
            valores[i].append(pixel_values[i])
            suma[i] = suma[i] + pixel_values[i]

    for i in range(tamano):
        media[i] = suma[i] / 40
        valores[i].sort()
        moda[i] = valores[i][19] + valores[i][20]
        suma_cuadrada = 0
        for j in range(40):
            suma_cuadrada = suma_cuadrada + pow(valores[i][j] - media[i], 2)
        ponderada = suma_cuadrada / 40
        desviacion_std[i] = math.sqrt(ponderada)
    
    resultado_csv = open('ejercicio1/resultado2.csv', 'w')
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
