import random

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
    
    def take_dmg(self, cantidad):
        cantidad = max(0, cantidad)
        self.life -= cantidad
        if self.life <= 0:
            print(f"{self.name} ha recibido {cantidad} de daño y se ha debilitado")
        else:
            print(f"{self.name} recibe {cantidad} de daño, aún conserva {self.life} puntos de vida")
        
class Guerrero(Personaje):
    def hachazo(self, rival):
        dmg = (self.attack * 2) - rival.defense
        rival.take_dmg(dmg)
        print(f"{self.name} usa HACHAZO sobre {rival.name}, es super efectivo")

class Hechicero(Personaje):
    def fireball(self, rival):
        luck = random.randint(1, 10)
        dmg = (self.attack + luck) - rival.defense
        rival.take_dmg(dmg)
        print(f"{self.name} conjura BOLA DE FUEGO sobre {rival.name}, causándole quemaduras")
        
class Arquero(Personaje):
    def ench_arrow(self, rival):
        luck = random.randint(1, 5)
        dmg = (self.attack + luck) - rival.defense
        rival.take_dmg(dmg)
        print(f"{self.name} dispara FLECHA ENCANTADA sobre {rival.name}, aplicando sangrado")

g = Guerrero("Groal, El Grande", 250, 7, 11)
h = Hechicero("Lucas, El Todopoderoso", 170, 9, 8)
a = Arquero("Legolas, El elfo", 185, 8, 5)