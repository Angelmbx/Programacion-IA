## Unha xoguetería ten moito éxito en dous dos seus produtos: pallasos e bonecas. Adoita facer venda por correo 
# e a empresa de loxística cóbralles por peso de cada paquete así que deben calcular o peso dos pallasos e bonecas 
# que sairán en cada paquete a demanda. Cada pallaso pesa 112  g e cada boneca 75  g. Escribir un programa que lea o número de 
# pallasos e bonecas vendidos no último pedido e calcule o peso total en Kg do paquete que será enviado. ##

if __name__ == "__main__":

    peso_pallasos = 112
    peso_bonecas = 75

    num_pallasos = int(input('Introduza o número de pallasos: '))
    num_bonecas = int(input('Introduza o número de bonecas: '))

    def peso_calculator(num_pallasos, num_bonecas):
        return num_pallasos * peso_pallasos + num_bonecas * peso_bonecas
    
    print(f'O peso total é de {peso_calculator(num_pallasos, num_bonecas)} kgs')

