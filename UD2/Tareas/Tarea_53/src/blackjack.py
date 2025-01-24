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
    jugador1, jugador2, banca = participantes

    estado_inicial = [jugador1, jugador2, banca]

    # Comprueba que la puntuación inicial sea menor o igual a 21
    validos = [jugador for jugador in estado_inicial if jugador.mano.puntuacion <= puntuacion_obj]
    no_validos = [jugador for jugador in estado_inicial if jugador.mano.puntuacion > puntuacion_obj]

    if validos:
        jugadores_eliminados = []  # Lista para registrar jugadores eliminados

        for jugador in validos:
            print(f"Turno de {jugador.nombre} - Puntuación inicial {jugador.mano.puntuacion}: ")

            jugando = True

            if jugador.mano.puntuacion == puntuacion_obj:
                print(f"{jugador.nombre} ha alcanzado la puntuación límite con {jugador.mano.puntuacion} puntos!")
                jugando = False

            while jugando:
                pedir = input("¿Quieres pedir otra carta? (1 para sí / 0 para no): ").lower().strip()
                if pedir == "1":
                    jugador.mano.añadir_carta()
                    print(f"Nueva puntuación {jugador.mano.puntuacion}")

                    if jugador.mano.puntuacion == puntuacion_obj:
                        print(f"{jugador.nombre} ha alcanzado la puntuación límite con {jugador.mano.puntuacion} puntos!")
                        break
                    elif jugador.mano.puntuacion > puntuacion_obj:
                        print(f"{jugador.nombre} ha superado la puntuación límite con {jugador.mano.puntuacion}.")
                        jugadores_eliminados.append(jugador)
                        break
                else:
                    jugando = False

        # Actualiza la lista de válidos eliminando los jugadores que superaron 21 puntos
        validos = [jugador for jugador in validos if jugador not in jugadores_eliminados]

    else:
        for jugador in no_validos:
            print(f"{jugador.nombre} superó la puntuación límite: {jugador.mano.puntuacion}: ")

    return validos


def comprobar_ganadores():
    participantes_validos = iniciar_partida()

    max_puntuacion = max([j.mano.puntuacion for j in participantes_validos ])
    
    ganadores = [j for j in participantes_validos if j.mano.puntuacion == max_puntuacion]
    
    print(f"Enhorabuena {ganadores[0].nombre}!!")
    

def comprobar_ganadores():
    participantes_validos = iniciar_partida()

    if not participantes_validos:
        print("No hay ganadores, todos los jugadores han sido eliminados.")
        return

    #Obtener la puntuación máxima entre los jugadores válidos
    max_puntuacion = max([j.mano.puntuacion for j in participantes_validos])

    # Se añade a ganadores a aquellos jugadores que obtuviesen esa puntuación (por si hay empate a puntos)
    ganadores = [j for j in participantes_validos if j.mano.puntuacion == max_puntuacion]

    nombres_ganadores = ", ".join([j.nombre for j in ganadores])

    print(f"Enhorabuena {nombres_ganadores} por la victoria con {max_puntuacion} puntos!")
