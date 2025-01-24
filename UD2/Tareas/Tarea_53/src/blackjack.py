from src.jugador import Jugador


def seleccionar_participantes():
    jugador_1 = Jugador(input("Introduce nombre de jugador 1: "))
    jugador_2 = Jugador(input("Introduce nombre de jugador 2: "))
    banca = Jugador("Banca")

    participantes = (jugador_1, jugador_2, banca)

    return participantes  


def iniciar_partida():
    puntuacion_obj = 21 

    participantes = seleccionar_participantes()
    jugador1 = participantes[0]
    jugador2 = participantes[1]
    banca = participantes[2]
    

    estado_inicial= [
        (jugador1, jugador1.mano.puntuacion),
        (jugador2, jugador2.mano.puntuacion),
        (banca, banca.mano.puntuacion)
    ]
    

    # Comprueba que la puntuación inicial sea menor o igual a 21
    validos = [jugador for jugador in estado_inicial if jugador[1] <= puntuacion_obj]
    no_validos = [jugador for jugador in estado_inicial if jugador[1] > puntuacion_obj]

    if validos:
        jugadores_eliminados = []  # Lista para registrar jugadores eliminados
        
        for jugador, jugador.mano.puntuacion in validos:
            # puntuacion = jugador.mano.puntacion
            print(f"Turno de {jugador.nombre} - Puntuación inicial {jugador.mano.puntuacion}: ")
    
            jugando = True
            
            if jugador.mano.puntuacion == puntuacion_obj:
                print(f"{jugador.nombre} ha alcanzado la puntuación límite con {jugador.mano.puntuacion} puntos!.")
                jugando = False

            while jugando:
                pedir = input("¿Quieres pedir otra carta? (1 para sí / 0 para no): ").lower().strip()
                if pedir == "1":
                    jugador.mano.añadir_carta()
                    print(f"Nueva puntuación {jugador.mano.puntuacion}")
                    
                    if jugador.mano.puntuacion == puntuacion_obj:
                        print(f"{jugador.nombre} ha alcanzado la puntuación límite con {jugador.mano.puntuacion} puntos!.")
                        break
                    elif jugador.mano.puntuacion > puntuacion_obj:
                        print(f"{jugador.nombre} ha superado la puntuación límite con {jugador.mano.puntuacion}.")
                        jugadores_eliminados.append((jugador, jugador.mano.puntuacion))
                        break
                else:
                    jugando = False
        

        # Actualizar la lista de válidos eliminando los jugadores que superaron 21 puntos
        validos = [jugador for jugador in validos if jugador not in jugadores_eliminados]
        
    else:
        for jugador, puntuacion in no_validos:
            print(f"{jugador.nombre} superó la puntuación límite: {puntuacion}: ")


    return validos



def comprobar_ganadores():


    puntuaciones_finales = iniciar_partida()
    #print(puntuaciones_finales)

    for elemento in puntuaciones_finales:
        jugador = elemento[0]
        puntuacion = elemento[1]
        print(jugador.nombre, puntuacion)
        