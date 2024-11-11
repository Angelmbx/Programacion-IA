## Escribir un programa que almacene as materias dun curso (por exemplo Matemáticas, Física, Química, Historia e Lingua) nunha lista, 
# pregunte ao usuario a nota que sacou en cada materia, e despois as amose por pantalla coa mensaxe En <materia> 
# sacaches un <nota> onde <materia> é cada unha das materias da lista e  <nota> cada unha das correspondentes notas introducidas 
# polo usuario. ##

if __name__ == "__main__":
    materias = ['Matemáticas', 'Historia', 'Economía', 'Física']
    resultados = dict.fromkeys(materias) # creo un diccionario cuyas claves serán los elementos de 'materias', aunque sin valores aún
    
    for materia in materias: 
         nota = input(f'Que nota tes en {materia}?: ') 
         resultados[materia] = nota


    print('--------')
    print('NOTAS')
    print('--------')
    
    for materia, nota in resultados.items(): 
        print(f'En {materia} tienes un {nota}')



    