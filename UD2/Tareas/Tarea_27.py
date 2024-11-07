## Escribir unha función que calcule o total dunha factura tras aplicarlle o IVE. 
# A función debe recibir a cantidade sen IVE e a porcentaxe de IVE a aplicar, e devolver o total da factura. 
# Se se invoca a función sen pasarlle a porcentaxe de IVE, deberá aplicar un 21%. ##

if __name__ == "__main__":

    factura_sen_ive = float(input('Introduza o importe da súa factura sen IVE: '))
    tipo_ive = float(input('Indique a porcentaxe de IVE a aplicar: 21, 10, ou 4'))/100 +1
    IVE_XERAL = 1.21
    factura_con_ive = 0

    if tipo_ive != null:
        def ive_calculator(tipo_ive):
            factura_con_ive = factura_sen_ive * tipo_ive
            return factura_con_ive
    else:
        print('Tipo de IVE non escificado, aplicarase o IVE xeral')
        factura_con_ive = factura_sen_ive * IVE_XERAL

    
    print('A súa factura aplícandolle o')
