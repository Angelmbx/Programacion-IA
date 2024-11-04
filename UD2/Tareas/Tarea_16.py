## Escribir un programa que pida ao usuario unha palabra e a amose por pantalla 10 veces. ##

if __name__ == '__main__':
    palabra = input('Introduza unha palabra: ')
    repeticions = 1

    while repeticions <= 10:
        print(repeticions,':', palabra)
        repeticions += 1