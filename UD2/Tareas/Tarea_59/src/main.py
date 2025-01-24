import numpy as np

# 1. Crea un array de 1D cos números do 0 ao 9
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# 2. Crea un array de 1D cos números do 1 ao 10
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# 3. Indica dos elementos do seguinte array cales son pares:
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

pares = arr[arr % 2 == 0]
print("pares: ", pares)
# 4. Do seguinte array, substitúe todos os números impares por 0
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

pares_y_ceros = np.array([elemento if elemento % 2 == 0 else 0 for elemento in arr]) 
print("Pares y ceros: ", pares_y_ceros)
# 5. Une os arrays a e b de xeito que as filas de b se encontren debaixo das de a.
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)

new_arr = np.concatenate((a,b))
print(new_arr)
# 6. Une os arrays a e b de xeito que as columnas de b se encontren a dereita das de a.
new_arr = np.concatenate((a,b), axis=1)
print(new_arr)



