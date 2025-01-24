import numpy as np

# 1. Obten os elementos que se encontran en a e en b na mesma posicion.
print("Ejercicio 1 ")
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c = np.array([(elementoA,elementoB) for elementoA, elementoB in zip(a,b) if elementoA == elementoB])
print(c)

# new_arr = np.concatenate((a, b), axis=0)
# print(new_arr)

# 2. Obten todos os numeros do array a que se encontren entre 5 e 10
print("Ejercicio 2 ")
a = np.array([2, 6, 1, 9, 10, 3, 27])

new_arr = np.array([elemento for elemento in a if elemento < 10 and elemento > 5])
print(new_arr)

# 3. Sexa a función maxx definida como:
# print("Ejercicio 3")

# def maxx(x, y):
#     """Get the maximum of two items"""
#     if x >= y:
#         return x
#     else:
#         return y
    
# # Fai que se aplique de xeito vectorial de tal xeito que se o aplicamos aos array a e b obteñamos o seguinte resultado.
# a = np.array([5, 7, 9, 8, 6, 4, 5])
# b = np.array([6, 3, 4, 8, 9, 7, 1])
# print(maxx(a, b))
# #> array([ 6.,  7.,  9.,  8.,  9.,  7.,  5.])





# 4. Lee mediante pandas o ficheiro iris.data. Obten a columna sepallength como un array numpy. 
# Normaliza os datos: os novos valores terán un valor minimo de 0 e maximo de 1.
# Podes descargar os ficheiros de datos de aquí: https://archive.ics.uci.edu/dataset/53/iris
# Nesa url tes tanto o ficheiro de datos como a súa descrición.
print("Ejercicio 4")

import pandas as pd
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler

iris_data = datasets.load_iris()
iris_data
iris = pd.DataFrame(iris_data.data,columns=iris_data.feature_names)
datos = np.array([iris['sepal length (cm)']]) 

scaler = MinMaxScaler()
datos_normalizados = scaler.fit_transform(datos)

print(datos_normalizados)
