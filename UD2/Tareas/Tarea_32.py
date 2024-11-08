## Escribir un programa que almacene as materias dun curso (por exemplo Matemáticas, Física, Química, Historia e Lingua) nunha lista, 
# pregunte ao usuario a nota que sacou en cada materia, e despois as amose por pantalla coa mensaxe En <materia> 
# sacaches un <nota> onde <materia> é cada unha das materias da lista e  <nota> cada unha das correspondentes notas introducidas 
# polo usuario. ##

if __name__ == "__main__":

    materias = {'Matemáticas': 7.8, 'Historia': 6.0, 'Economía': 3.75, 'Física': 9.0}

    for nota in materias.keys(): 
        print("{} => {}".format(nota, materias[nota])) 
    
    