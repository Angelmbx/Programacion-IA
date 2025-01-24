# 1. Lee mediante pandas o ficheiro iris.data. Obtén un lista cos valores únicos da columna class
import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ["sepal length", "sepal width", "petal length", "petal width", "class"]

iris = pd.read_csv(url, header=None, names= column_names)

np_iris = iris.to_numpy()

valores = np.array([fila[-1] for fila in np_iris])

valores_unicos = np.unique(valores)
print("-"*100)
print("Posibles valores de la columna class:", ", ".join(valores_unicos))
print("-"*100)

# # 2. Asignalles a cada un deles un valor numérico de xeito automático. Crea unha nova columna onde se cambie o valor categórico polo número.

np_class = iris['class'].to_numpy()
tipos_codificados = np.zeros(shape= np_class.shape, dtype= int)

tipos_codificados[np_class == 'Iris-setosa'] = 1
tipos_codificados[np_class == 'Iris-versicolor'] = 2
tipos_codificados[np_class == 'Iris-virginica'] = 3

iris['tipo'] = tipos_codificados

# si se quisiera eliminar la columna class -> iris.drop(['class'])

print(iris)
print("-"*100)

# #3. Crea unha nova columna por cada categoría, na que aparecerá un 1 se a fila pertence a esa clase.

np_setosa = np.zeros(shape= np_class.shape, dtype= int)
iris['setosa'] = np_setosa
np_versicolor = np.zeros(shape= np_class.shape, dtype= int)
iris['versicolor'] = np_versicolor
np_virginica = np.zeros(shape= np_class.shape, dtype= int)
iris['virginica'] = np_virginica

np_setosa[np_class == 'Iris-setosa'] = 1
np_versicolor[np_class == 'Iris-versicolor'] = 1
np_virginica[np_class == 'Iris-virginica'] = 1

iris['setosa'] = np_setosa
iris['versicolor'] = np_versicolor
iris['virginica'] = np_virginica

iris.drop(columns= ['tipo', 'class'], inplace= True)

print(iris)