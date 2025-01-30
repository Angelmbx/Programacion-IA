## Ao blackjack se xoga con baralla francesa: A,K,Q,J,10..2 un total de 52 cartas.
# As cartas se agrupan en mans e a puntuación da man se consegur sumando a puntuación de cada carta tendo en conta que:
# cada carta númerica vale o seu número
# as cartas K,Q,J valen 10
# O As pode valer 11 ou 1, dependendo do necesario.

# A puntuación máis alta obxectivo é chegar 21. Se a man ten mais de 21 puntos se perde.
# Cada xogador ten unha man e se elixe ao gañador (se o hai) como o que ten a puntuación maior (sen pasarse do límite)

from src.blackjack import comprobar_ganadores


if __name__ == "__main__" :
    
    comprobar_ganadores()