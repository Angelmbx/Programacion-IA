
def suma(n1,n2):
    if type(n1) == int and type(n2)== int:
        return n1+n2
    else:
        raise(TypeError('Só se poden sumar ints'))

if __name__ == "__main__":
    
    numero_1 = int(input('Dame un numero'))
    numero_2 = int(input ('Dame outro numero'))

    result = suma(numero_1, numero_2)
    print(f'O resultado é {result}')