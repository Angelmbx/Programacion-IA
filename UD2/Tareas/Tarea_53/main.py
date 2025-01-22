## Ao blackjack se xoga con baralla francesa: A,K,Q,J,10..2 un total de 52 cartas.
# As cartas se agrupan en mans e a puntuación da man se consegur sumando a puntuación de cada carta tendo en conta que:
# cada carta númerica vale o seu número
# as cartas K,Q,J valen 10
# O As pode valer 11 ou 1, dependendo do necesario.

# A puntuación máis alta obxectivo é chegar 21. Se a man ten mais de 21 puntos se perde.
# Cada xogador ten unha man e se elixe ao gañador (se o hai) como o que ten a puntuación maior (sen pasarse do límite)

from src import jugador
from src.blackjack import iniciar_partida


if __name__ == "__main__" :
    
    jugador_1 = jugador.Jugador("Robert")
    jugador_2 = jugador.Jugador("Vanesa")
    banca = jugador.Jugador("Banca")
    
    
    print(f"{jugador_1.nombre}, puntuación: {jugador_1.mano.puntuacion}")
    print(f"{jugador_2.nombre}, puntuación: {jugador_2.mano.puntuacion}")
    print(f"{banca.nombre}, puntuación: {banca.mano.puntuacion}")
    print(f"Ganador: {iniciar_partida(jugador_1, jugador_2, banca)}")
    