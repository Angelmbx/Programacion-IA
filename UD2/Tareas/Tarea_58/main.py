class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.salud = 3

    def hit(self, rival, daño=1):
        rival.recibir_daño(daño)

    def recibir_daño(self, daño):
        self.salud -= daño

    def is_alive(self):
        return self.salud > 0


class Decorator:
    def __init__(self, decorado):
        self._decorado = decorado

    def __getattr__(self, attr):
        return getattr(self._decorado, attr)

    def __setattr__(self, attr, value):
        if attr == "_decorado":
            super().__setattr__(attr, value)
        else:
            setattr(self._decorado, attr, value)

    def recibir_daño(self, daño):
        self._decorado.recibir_daño(daño)


class EscudoPersonal(Decorator):
    def __init__(self, decorado):
        super().__init__(decorado)
        self.durabilidad = 5
        self.capacidad = 1

    def recibir_daño(self, daño):
        if self.durabilidad > 0:
            absorcion = min(self.capacidad, daño)
            self.durabilidad -= absorcion
            daño -= absorcion
        super().recibir_daño(daño)


class EscudoCombate(Decorator):
    def __init__(self, decorado):
        super().__init__(decorado)
        self.durabilidad = 20
        self.capacidad = 5

    def recibir_daño(self, daño):
        if self.durabilidad > 0:
            absorcion = min(self.capacidad, daño)
            self.durabilidad -= absorcion
            daño -= absorcion
        super().recibir_daño(daño)


if __name__ == "__main__":
    alien1 = Alien(0, 0)
    alien2 = EscudoPersonal(Alien(1, 1))
    alien3 = EscudoCombate(Alien(2, 2))

    print(f"Salud inicial alien2: {alien2.salud}, con escudo personal")
    alien1.hit(alien2)
    print(f"Después de recibir 1 de daño: {alien2.salud}, escudo restante: {alien2.durabilidad}")
    
    print(f"Salud inicial alien3: {alien3.salud}, con escudo de combate")
    alien1.hit(alien3, 6)
    print(f"Después de recibir 6 de daño: {alien3.salud}, escudo restante: {alien3.durabilidad}")
