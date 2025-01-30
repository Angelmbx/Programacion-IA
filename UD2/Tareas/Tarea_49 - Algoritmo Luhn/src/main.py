## No sistema temos presente usuarios. Cada un deles ten un nome, un nome de usuario, un contrasinal e un número de tarxeta.
#  O número de tarxeta segue a formula de Luhn. Os usuarios poden ter establecido o número de tarxeta ou non, en todo caso, 
#  se o teñen ten que seguir a formula. Pensa primeiramente que relación existe entre os usuarios e os números de Lunh, e logo implementa. ##

from Tarea_49.errores import error_de_formato, error_numero_caracteres, error_algoritmo_luhn
from Tarea_49.usuario import Usuario


if __name__ == "__main__":
    
    try:
        usuario_1 = Usuario(nombre="Paco", username="magic_paco", password = "123.", tarjeta= "4539 3195 0343 6467" )
        print(usuario_1.mostrar_usuario())
    except error_numero_caracteres as invalid_length:
        print(invalid_length)
    except error_de_formato as format_error:
        print(format_error)
    except error_algoritmo_luhn as invalid_card_number:
        print(invalid_card_number)