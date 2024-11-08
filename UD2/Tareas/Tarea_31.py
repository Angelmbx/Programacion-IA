## Escribir un programa que almacene as materias dun curso (por exemplo Matemáticas, Física, Química, Historia e Lingua)
#  nunha lista e a mostre por pantalla coa mensaxe Eu estudo <materia>, onde <materia> é cada unha das materias da lista. ##

if __name__ == "__main__":

    materias = ['Matemáticas', 'Historia', 'Economía', 'Física']

    for materia in materias:
        print(f'Eu estudo {materia}')