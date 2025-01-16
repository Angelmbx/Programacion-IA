## Esta tarefa é igual que a anterior, cunhas pequenas modificacións, polo que se pode partir do feito nela.
# Co feito ata o de agora, cando se crea unha instancia se valida o número co algoritmo de Lunh. Pero que pasa despois? 
# O numero de tarxeta pode ser cambiado e non se valida para nada.
# Usa properties para modificar isto, de tal xeito que o número de tarxeta sexa validado cando se lle intente cambiar o valor. 
## Se o número non e correcto, o usuario debe manter o código de tarxeta anterior e se debe lanzar unha excepción.


from Tarea_50.errores import error_de_formato, error_numero_caracteres, error_algoritmo_luhn
from Tarea_50.usuario import Usuario


if __name__ == "__main__":
    try:
        usuario_1 = Usuario(nombre="Paco", username="magic_paco", password="123.", tarjeta="4539 3195 0343 6467")
        print(usuario_1.mostrar_usuario())
        
        # Nuevo número de tarjeta válido
        usuario_1.tarjeta = "6011 5144 3354 6201"
        print("Tarjeta cambiada exitosamente:", usuario_1.mostrar_usuario())

        # Nuevo número de tarjeta inválido
        usuario_1.tarjeta = "tarjeta"  # Lanza excepción de error de formato

    except error_algoritmo_luhn as invalid_card_number:
        print(invalid_card_number)
    except error_numero_caracteres as invalid_length:
        print(invalid_length)
    except error_de_formato as format_error:
        print(format_error)