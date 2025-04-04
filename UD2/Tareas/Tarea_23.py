## Escribir un programa que pida ao usuario un número enteiro e mostre por pantalla se é un número primo ou non. 
# Para iso basta que tentes dividir o número polos números menores a n/2. 
# Se algún deles divide de xeito exacto ao número entón non é primo ##

if __name__ == '__main__':
    
    numero = int(input("Introduza un número enteiro: "))
    numero_primo = True
    index = 1

    for index in range(2, numero//2+1):
        if numero % index == 0:
            numero_primo = False
            break
            
    if numero_primo:
        print("O número introducido é primo")
    # else:
        print("O número introducido NON é primo")
