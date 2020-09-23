import random
class personagem:
    def __init__(self,vida,armadura,velocidade,forca,arma,nome):
        self.nome=nome
        self.hp=int(vida)
        self.armor=int(armadura)
        self.vel=int(velocidade)
        self.forca=int(forca)
        self.arma=arma
        
    def curse(self,NoDoCo):
        qual=random.randint(0,2)
        if qual==0: print('vai se fuder',NoDoCo,'!')
        if qual==1: print(NoDoCo,'sua puta!')
        if qual==2: print('piranha!')
    def atacar(self,oponente):
        if self.arma==None: pass
        else:
            lista=self.arma.ataques
            print('lista de ataques:',lista)
class arma:
    def __init__(self,dano,durabilidade,velocidade,nome):
        self.dano=int(dano)
        self.nome=nome
        self.du=int(durabilidade)
        self.vel=int(velocidade)
    def leve(self,forca,velocidade):
        d=self.dano+forca
        v=self.vel+velocidade
        DpV=d+v
        return DpV
    def pesado(self,forca,velocidade):
        d=(self.dano*2)+forca
        v=(self.vel/2)+velocidade
        DpV=d+v
        return DpV