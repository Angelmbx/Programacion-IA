import random

class Carta:
    
    tipo = [{"figura": "As", "valor": 11, "cantidad": 4},
            {"figura": "K", "valor": 10, "cantidad": 4},
            {"figura": "Q", "valor": 10, "cantidad": 4},
            {"figura": "J", "valor": 10, "cantidad": 4},
            {"figura": "K", "valor": 10, "cantidad": 4}]
    
    for i in range (10, 1, -1):
        tipo.append({"figura": str(i), "valor": i, "cantidad": 4})


    #print(tipo)
   
    def __init__ (self):
        nueva = random.choice(Carta.tipo)  # Al crearse una instancia de carta, saldrá un tipo de carta al azar de dentro de la lista "tipo" y se restará 1 de dicho tipo a la baraja
        self.figura = nueva["figura"]     
        self.valor = nueva["valor"]  
        self.cantidad = nueva["cantidad"] - 1
    
   