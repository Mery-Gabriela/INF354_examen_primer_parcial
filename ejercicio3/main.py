from sklearn import preprocessing
import numpy as np

def main():
    archivo_csv = open("dataset1.csv", "r")
    lineas = archivo_csv.readlines()
    data = []
    for n in range(1, 41): 
        if (len(data) == 0):
            data = np.array([int(s) for s in lineas[n].split(',')])
        else:
            data = np.vstack((data, np.array([int(s) for s in lineas[n].split(',')])))

    matriz_salida = preprocessing.scale(data, with_mean=True)
    print(matriz_salida)

    matriz_normalizada = preprocessing.normalize(data)
    print(matriz_normalizada)

    transformer = preprocessing.FunctionTransformer(np.log1p, validate=True)
    matriz_logaritmizada = transformer.transform(data)
    print(matriz_logaritmizada)

if __name__ == "__main__":
    main()
