class Blunt:
    def i_initb(self):
        print('Digite o dano do tipo blunt')
        d=int(input())
        self.blunt_damage=d
    def p(self):
        print('lol')

class Piercing:
    def i_initp(self):
        print('Digite o dano do tipo piercing')
        d=int(input())
        self.piercing_damage=d
    def p2(self):
        print('turntables')

class arma:
    def __init__(self,nome):
        print('teste nome:',nome)
        self.nome=nome
    def p3(self):
        print('rye')