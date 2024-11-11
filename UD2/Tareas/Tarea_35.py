## Escribir un programa que almacene as materias dun curso (por exemplo Matemáticas, Física, Química, Historia e Lingua) nunha lista,
#  pregunte ao usuario a nota que sacou en cada materia e elimine da lista as materias aprobadas. 
#  Ao final o programa debe mostrar por pantalla as materias que o usuario ten que repetir. ##

if __name__ == "__main__":

    materias = ['Matemáticas', 'Historia', 'Economía', 'Física']
    suspensas = materias[::]
    
    for materia in materias: 
         nota = float(input(f'Que nota tes en {materia}?: ')) 
         if nota >= 5:
             suspensas.remove(materia)
             

    print('--------')
    print('MATERIAS A REPETIR')
    print('--------')

    print(f'As materias a repetir son {','.join(suspensas)}')


