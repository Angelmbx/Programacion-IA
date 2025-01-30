## Fai unha función que recolla como parámetro unha lista de números e nos indique que elementos son primos ##

def primos_checker(n):
    
    primos = []

    for item in n:
        if item > 1:
            primo = True
            for numero in range(2, item//2+1):
                if item % numero == 0:
                    primo = False
                    break
            if primo:
                    primos.append(item)
    
    return primos
        

if __name__ == "__main__":
    lista = [2,10,4,7,12,13,20]

    primos = primos_checker(lista)
    print(f'Da lista indicada son primos: {", ".join(map(str, primos))}')
