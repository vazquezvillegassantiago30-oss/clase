print("Hello world!")


def triangulo (b, h):
    area = (b * h) / 2
#Aldo

def circle(r):
    area = 3.1416 * r**2
    return area


class Personaje:
    def __init__(self, nombre, vida, ataque, defensa):
        self.name = nombre
        self.life = vida
        self.attack = ataque
        self.defense = defensa
        
