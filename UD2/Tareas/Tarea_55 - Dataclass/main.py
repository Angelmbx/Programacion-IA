# Similar á tarefa 49.
# No sistema temos presente usuarios. Cada un deles ten un nome, apelidos, o nome completo (que se obtén de xuntar o nome e os apelidos) 
# un nome de usuario, un contrasinal e un número de tarxeta. O número de tarxeta segue a formula de Luhn. 
# Os usuarios poden ter establecido o número de tarxeta ou non, en todo caso, se o teñen ten que seguir a formula.
# Implementa un par de dataclass para os usuarios: 
# - A primeira versión vai a ser inmutable (frozen) de tal xeito que so terás que comprobar o numero de tarxeta no constructor. 
# - A segunda versión non vai a ser inmutable, deberás sobreescribir os métodos de acceso para a tarxeta usando property (non se pode usar a sintaxe nova do decorador).

from src.usuario_inmutable import Usuario_inmutable
from src.usuario_properties import Usuario_properties

if __name__ == '__main__':

    usuario_inm = Usuario_inmutable("Paco", "Martinez López", "pacman", "123.", "4539 3195 0343 6467")
    print(usuario_inm)

    usuario_mod = Usuario_properties("Manuel", "Sánchez López", "manolo_445", "123.", "4539 3195 0343 6467")
    print(usuario_mod)