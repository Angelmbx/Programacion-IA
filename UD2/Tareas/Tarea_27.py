## Escribir unha función que calcule o total dunha factura tras aplicarlle o IVE. 
# A función debe recibir a cantidade sen IVE e a porcentaxe de IVE a aplicar, e devolver o total da factura. 
# Se se invoca a función sen pasarlle a porcentaxe de IVE, deberá aplicar un 21%. ##

if __name__ == "__main__":      

    factura_sen_ive = float(input('Introduza o importe da súa factura sen IVE: '))
    tipo_ive = input('Indique a porcentaxe de IVE a aplicar (4, 10 ou deixar baleiro para aplicar o ive xeral 21%): ')

    if tipo_ive == "":
        tipo_ive = 21
    else:
        tipo_ive = float(tipo_ive)
    
    if tipo_ive not in [4, 10, 21]:
        print('IVE non válido. Aplicarase o IVE xeral (21%)...')
        tipo_ive = 21
    
    def factura_con_ive_calculator(factura_sen_ive, tipo_ive=21):
        return factura_sen_ive * (1 + tipo_ive / 100)

    total_factura = factura_con_ive_calculator(factura_sen_ive, tipo_ive)
    
    print(f'O montante da súa factura é de {total_factura:.2f}')
