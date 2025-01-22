## Ao blackjack se xoga con baralla francesa: A,K,Q,J,10..2 un total de 52 cartas.
# As cartas se agrupan en mans e a puntuación da man se consegur sumando a puntuación de cada carta tendo en conta que:
# cada carta númerica vale o seu número
# as cartas K,Q,J valen 10
# O As pode valer 11 ou 1, dependendo do necesario.

# A puntuación máis alta obxectivo é chegar 21. Se a man ten mais de 21 puntos se perde.
# Cada xogador ten unha man e se elixe ao gañador (se o hai) como o que ten a puntuación maior (sen pasarse do límite)

from src import jugador


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



if __name__ == "__main__" :
    
    jugador_1 = jugador.Jugador("Robert")
    jugador_2 = jugador.Jugador("Vanesa")
    banca = jugador.Jugador("Banca")
    
    
    print(f"{jugador_1.nombre}, puntuación: {jugador_1.mano.puntuacion}")
    print(f"{jugador_2.nombre}, puntuación: {jugador_2.mano.puntuacion}")
    print(f"{banca.nombre}, puntuación: {banca.mano.puntuacion}")
    print(f"Ganador: {iniciar_partida(jugador_1, jugador_2, banca)}")
    