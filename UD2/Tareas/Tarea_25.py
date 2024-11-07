## Escribir unha función que reciba un número enteiro positivo e devolva o seu factorial. ##

if __name__ == "__main__":

    numero = int(input("Introduza un número enteiro positivo: "))

    def factorial_calculator(numero):
        for i in range(1, numero):
            numero *= i
        return numero

    if numero < 0:
        print("O número debe ser positivo")
    else:
        print("Resultado: ", factorial_calculator(numero))
