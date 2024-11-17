## Escribir un programa que garde nun dicionario os prezos das froitas da táboa, pregunte ao usuario por unha froita, 
# un número de quilos e mostre por pantalla o prezo dese número de quilos de froita. Se a froita non está no dicionario
# debe mostrar unha mensaxe informando diso. ## 

if __name__ == "__main__":

    froitas = {"platano": 1.35, "mazá": 0.80, "pera": 0.85, "laranxa": 0.80}

    tipo_froita = input("Que froita queres?: ").lower()
    kgs_froita = float(input("Cantos quilos queres?: "))

    def prezo_froita_calculator(froita, kgs):
        if froita in froitas:
            return f"O prezo do seu pedido é {froitas[froita] * kgs:.2f} euros"
        else:
            return "A froita introducida non se atopa disponible."
        
    print(prezo_froita_calculator(tipo_froita, kgs_froita))