def ver(message):
    while True:
        print(message)
        t=input()
        try: float(t)
        except: print('String dada n é um numero')
        else: return int(t)

class magia:
    def __init__(self,number,nome,mana):
        self.nome=nome
        self.mana=mana
        while True:
            continuar=False
            teste=input('É uma magia em area(a) ou multiple target(m) ou single target(s): ')
            if teste=='a': self.area=(ver('Qual a area?'))
            elif teste=='m': self.quantas=(ver('Quantas pessoas o spell pode atingir?'))
            elif teste=='s': self.quantas=1
            else:
                print('Não existe essa opção')
                continuar=True
            if not continuar: break

class dano(magia):
    def __init__(self,number,nome,mana):
        if number==1: super(dano,self).__init__(number,nome,mana)
        else: self.nome=(nome+' '+str(number))
        danos={}
        while True:
            sair=False
            while True:
                tipos=['fire','cold','acid','lighning','radiant','necrotic','psychic','slashing','piercing','bludgeoning','poison']
                tipo=input('Qual tipo de dano(para ver os tipos digite qualquer coisa q n seja um tipo): ')
                if tipo in tipos: break
                elif tipo=='n':
                    sair=True
                    break
                else:
                    print('Não existe essa opção')
                    print('Tipos:',tipos)
            if sair: break
            damage=ver(('Qunto de '+(str(tipo))+' damage esse spell vai ter?'))
            danos[tipo]=damage
        self.danos=danos

class healing(magia):
    def __init__(self,number,nome,mana):
        if number==1: super(healing,self).__init__(number,nome,mana)
        else: self.nome=(nome+' '+str(number))
        self.heal=(ver('Quanto de healing o spell da?'))

class buff_debuff(magia):
    def __init__(self,number,nome,mana):
        if number==1: super(buff_debuff,self).__init__(number,nome,mana)
        else: self.nome=(nome+' '+str(number))
        mods={}
        while True:
            sair=False
            while True:
                tipos=['fire damage','cold damage','acid damage','lighning damage','radiant damage','necrotic damage','psychic damage','slashing damage','piercing damage','bludgeoning damage','poison damage']
                tipos2=['fire resistance','cold resistance','acid resistance','lighning resistance','radiant resistance','necrotic resistance','psychic resistance','slashing resistance','piercing resistance','bludgeoning resistance','poison resistance']
                tipos3=['forca','resistencia total','velocidade','inteligencia','intransigencia total','dextreza']
                tipo=input('Qual tipo de buff_debuff(para ver os tipos digite qualquer coisa q n seja um tipo): ')
                if tipo in tipos: break
                elif tipo in tipos2: break
                elif tipo in tipos3: break
                elif tipo=='n':
                    sair=True
                    break
                else:
                    print('Não existe essa opção')
                    print('Tipos:',tipos,tipos2,tipos3)
            if sair: break
            modifier=ver(('Qunto de '+(str(tipo))+' buff_debuff esse spell vai ter?'))
            mods[tipo]=modifier
        self.mods=mods
        self.duration=(ver('Por quanto tempo esse spell fica ativo?(em turnos)'))