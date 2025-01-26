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

    jugadores_eliminados = []  # Lista para registrar jugadores eliminados

    for jugador in participantes:
        print(f"Turno de {jugador.nombre} - Puntuación inicial {jugador.mano.puntuacion}: ")

        while True:
            pedir = input("¿Quieres pedir otra carta? ").strip()
            if pedir.strip() == "1":
                jugador.mano.añadir_carta()
                print(f"{jugador.nombre} ha recibido un {jugador.mano.nueva_carta.figura}, tu nueva es puntuación {jugador.mano.puntuacion}")

                if jugador.mano.puntuacion == puntuacion_obj:
                    print(f"{jugador.nombre} ha alcanzado la puntuación máxima con {jugador.mano.puntuacion} puntos!")
                    break
                elif jugador.mano.puntuacion > puntuacion_obj:
                    print(f"{jugador.nombre} ha superado la puntuación máxima con {jugador.mano.puntuacion} puntos.")
                    jugadores_eliminados.append(jugador)
                    break
            elif pedir.strip() == "0":
                break
            else:
                print("Respuesta incorrecta. Debes elegir entre (1) Pedir carta y (0) Plantarse")
       
   
    validos = [jugador for jugador in participantes if jugador not in jugadores_eliminados]   
       
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

    while True:
        otra_partida = input("Otra partida? (1 para sí / 0 para no): ").strip()
        if otra_partida == "1":
            comprobar_ganadores()
            break
        elif otra_partida == "0":
            print("Entendido, hasta otra!!")
            break
        else:
            print("Respuesta incorrecta. Debes elegir entre (1) Jugar otra partida y (0) Salir")