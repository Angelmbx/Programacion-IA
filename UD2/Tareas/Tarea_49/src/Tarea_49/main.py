## No sistema temos presente usuarios. Cada un deles ten un nome, un nome de usuario, un contrasinal e un número de tarxeta.
#  O número de tarxeta segue a formula de Luhn. Os usuarios poden ter establecido o número de tarxeta ou non, en todo caso, 
#  se o teñen ten que seguir a formula. Pensa primeiramente que relación existe entre os usuarios e os números de Lunh, e logo implementa. ##
def lunh_method(numero):

        ## VALIDACIÓN DE NÚMERO: Falta quitar espacios y unicos caracteres validos [0..9]       
        if len(numero) < 2:
            return False
        
        numero = numero[::-1]
        pares = []

        for index in range(0, len(numero)):
            if not index % 2 == 0 :
                pares.append(numero[index])
            

        return(pares)


if __name__ == "__main__":
    class usuario:
        def init(self, nome, username, password, tarxeta = None):
            self.nome = nome
            self.username = username
            self.password = password
            if lunh_method(tarxeta):
                self.tarxeta = tarxeta
            else:
                raise Exception
        

    print(lunh_method("1212121212121212"))