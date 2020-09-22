class arma():
    def __init__(self, nome, tipo):
        self.__nome = nome
        self.__tipo = tipo

    def description(self):
        print(f"{self.__nome}, {self.__tipo}")

class Piercing(arma):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)
    
    

class Blunt(arma):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)
    def p(self):
        print("lol")


thistuple = ("Piercing", "Blunt")
print(thistuple[1])


class Spear(arma):
    def __init__(self, nome, tipo):
        super().__init__(nome, tipo)
        return type("Spear", (arma),(thistuple))

thistuple = ("Piercing", "Blunt")
print(thistuple[1])

x = Piercing("espada", "slashing")
y = Blunt("hammer", "blunt")
w = Spear("spear", "piercing")
y.description()
y.p()
w.description()
w.p()








     
