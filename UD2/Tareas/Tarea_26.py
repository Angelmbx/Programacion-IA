## Escribir un programa que pida  ao usuario ou  seu peso (en kg) e estatura (en centímetros),
# calcule ou índice de masa corporal e  o almacene  nunha variable, e  mostre por pantalla a frase:
# O  teu índice de masa corporal  é <imc>  onde <imc>  é o índice de masa corporal calculado redondeado con  dous  decimais.
# O indice de masa corporal de calcula dividindo o peso en Kg polo cuadrado da altura medida en metros.
# fórmula = kilogramos dividido por el cuadrado de la estatura en metros. ##

if __name__ == "__main__":
    estatura = float(input("Introduza a súa estatura en centimetros: ")) / 100
    peso = float(input("Introduza o seu peso en kg: "))

    def imc_calculator(e, p):
        return p / pow(e, 2)

    imc = round((imc_calculator(estatura, peso)), 2)

    print(f"O seu índice de masa corporal é {imc}")
