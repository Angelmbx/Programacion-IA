## Escribir un programa que almacene nunha lista os números do 1 ao 10 e os ensine por pantalla en orde inversa separados por comas. 
# Usa o metodo join da clase string para separalos por comas ##

if __name__ == "__main__":

    lista_numeros = ['1', '2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9', '10']
    lista_numeros.reverse()

    x = ','.join(lista_numeros)
    print(x)
    

    