# name, height, mass, hair_color, skin_color, eye_color, birdth_year, sex, gender, homeworl, species, films

class Seres_biologicos:
    

    def __init__(self, name, height, mass, hair_color, skin_color, eye_color, birth_year, sex, gender, homeworld, species, films):
        self.name = name
        self.height = height
        self.mass = mass
        self.hair_color = hair_color
        self.skin_color = skin_color
        self.eye_color = eye_color
        self.birth_year = birth_year
        self.sex = sex
        self.gender = gender
        self.homeworld = homeworld
        self.species = species
        self.films = films


    def __str__(self):
        return f"{self.name}, especie: {self.species}, películas: {self.films}"