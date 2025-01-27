from src.Tarea_57.alien import Alien, generador_de_alienigenas_en_serie, contador_de_alienigenas

if __name__ == '__main__':
    
    total_aliens = []

    #crear aliens manualmente
    alien1 = Alien(2,5,total_aliens)
    alien2 = Alien(7,14,total_aliens)
    
    print("Alien1 golpea a Alien2!")
    alien1.hit(alien2, 6)
    print(f"Ahora la salud de Alien2 es {alien2.salud}")
    
    print(alien2.is_alive())

    lista_posiciones = [(20,3), (12,10), (5,9), (3,1)]

    generador_de_alienigenas_en_serie(lista_posiciones, total_aliens)
    
    print(contador_de_alienigenas(total_aliens))


    # for alien in total_aliens:
    #     print(alien.x, alien.y)


