def cria():
    lista_de_racas=['humano','elfo','anao','orc','tiefling','deva','qunari','draconato']
    while True:
        qual=input('Qual será a raca do personagem: ')
        if qual in lista_de_racas:
            ra=qual
            break
        else: print('Não existe essa opção\n Lista de racas:\n   ',lista_de_racas)
    lista_de_classes=['fighter','wizard','assassin']
    while True:
        qual=input('Qual será a classe do personagem: ')
        if qual in lista_de_classes:
            cla=qual
            break
        else: print('Não existe essa opção\n Lista de classes:\n   ',lista_de_classes)
    return [ra,cla]

racla=cria()
ra=racla[0]
cla=racla[1]

#--------------------------------------------------------------------------------

class fighter:
    def __init__(self): pass

class wizard:
    def __init__(self): pass

class assassin:
    def __init__(self): pass

class racas(fighter if cla=='fighter' else wizard if cla=='wizard' else assassin):
    def init_racas(self):
        super().__init__()

#--------------------------------------------------------------------------------

class humano:
    def __init__(self):
        self.pontos_lvl+=3

class elfo:
    def __init__(self):
        self.inteligencia=2
        self.velocidade=1

class anao:
    def __init__(self):
        self.forca=1
        self.resistencia=2
    
class orc:
    def __init__(self):
        self.forca=2
        self.inteligencia=-1
        self.Chp=1
        self.resistencia=2
        self.velocidade=-1

class tiefling:
    def __init__(self):
        self.inteligencia=2
        self.Chp=1
        self.intransigencia=-1

class qunari:
    def __init__(self):
        self.forca=2
        self.intransigencia=-1
        self.velocidade=2

class deva:
    def __init__(self):
        self.forca=-1
        self.inteligencia=1
        self.resistencia=-1
        self.intransigencia=1
        self.velocidade=3

class draconato:
    def __init__(self):
        self.Chp=1
        self.intransigencia=2

class classes(humano if ra=='humano' else elfo if ra=='elfo' else anao if ra=='anao' else orc if ra=='orc' else tiefling if ra=='tiefling' else deva if ra=='deva' else qunari if ra=='qunari' else draconato):
    def init_classe(self):
        self.forca=0
        self.inteligencia=0
        self.Chp=0
        self.Cmana=0
        self.velocidade=0
        self.resistencia=0
        self.intransigencia=0
        self.pontos_lvl=3
        super().__init__()

#--------------------------------------------------------------------------------

class personagem(classes,racas):
    def __init__(self):
        super().init_classe()
        super().init_racas()

    def printar(self):
        print('forca:',self.forca,'inteligencia:',self.inteligencia,'Chp:',self.Chp,'Cmana:',self.Cmana,'pontos_lvl:',self.pontos_lvl)
        print('resistencia:',self.resistencia,'intransigencia:',self.intransigencia,'velocidade:',self.velocidade)

player=personagem()
player.printar()