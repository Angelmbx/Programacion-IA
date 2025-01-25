class Droides:
    def __init__(self, name, height, mass,  birth_year, gender, homeworld,  films):
        self.height = height
        self.name = name
        self.mass = mass
        self.birth_year = birth_year
        self.gender = gender
        self.homeworld = homeworld
        self.films = films

    def __str__ (self):
        return f"· Nombre: {self.name}, planeta natal: {self.homeworld}, películas: {self.films}"