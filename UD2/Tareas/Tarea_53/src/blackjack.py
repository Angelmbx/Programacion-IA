def iniciar_partida(jugador1, jugador2, banca):
    puntuacion_obj = 21 
    
    participantes = [
        (jugador1.nombre, jugador1.mano.puntuacion),
        (jugador2.nombre, jugador2.mano.puntuacion),
        (banca.nombre, banca.mano.puntuacion)
    ]
    
    validos = [p for p in participantes if p[1] <= puntuacion_obj]
    
    if validos:
        # Ver que puntuación es la más alta de las válidas
        max_puntuacion = max(participante[1] for participante in validos)
        
        # Encontrar qué jugadores tienen esa puntuación (para que si hay más de 1 ganador, se reflejen todos y no solo el primero que aparezca)
        ganadores = [p[0] for p in validos if p[1] == max_puntuacion]
        
        return ", ".join(ganadores) 
        
    else:
        return "No hay ganador" 
