## Escribir un programa que pida ao usuario dous números enteiros e mostre por pantalla a < n> entre < m> dá un  cociente < c>
#  e un resto < r> onde < n> e < m> son os números introducidos polo usuario, e < c> e < r> son o  cociente e o resto da división 
# enteira respectivamente. Neste exercicio se trata de prácticar o uso de tuplas. Na función que fagas para implementar a división
#  terás como parámetros o dividende o mailo divisor, e vas calcular o dividendo e máis o resto. Como só podes devolver no return 
# un elemento terás que empaquetar a resposta nunha tupla. No programa principal podes chamar a esa función, recoller o resultado 
# e acceder á tupla devolta para facer a impresión en pantalla. ##

if __name__ == "__main__":

    num_1 = float(input('Introduza un número enteiro ("num 1"): '))
    num_2 = float(input('Introduza outro número enteiro ("num 2"): '))

    def division_calculator(num_1, num_2):
        cociente = num_1 / num_2
        resto = num_1 % num_2
        
        return (cociente, resto)
    
    print(f'{num_1} entre {num_2} da un cociente de {division_calculator(num_1, num_2)[0]} e un resto de {division_calculator(num_1, num_2)[1]} ')