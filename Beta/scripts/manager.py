import json
from .batalha.iniciativa import batalha
from .jogadores.criacao_personagem import personagem
from .jogadores.checar import checar
from .jogadores.editor import editar
from .jogadores.print import printar
from .funcoes.restore import restaurar
from .funcoes.adicionar import add
from .funcoes.lvlup import lvlup
from .funcoes.addinv import additem
from .funcoes.useit import useitem
from .funcoes.creators.classcreator import ccreator
from .funcoes.creators.racecreator import rcreator
from .funcoes.creators.magiccreator import mcreator
from .funcoes.creators.shieldcreator import screator
from .funcoes.creators.weaponcreator import wcreator
from .funcoes.creators.armorcreator import acreator

def menu(command):
    with open('Beta/data/nomes.json') as f:
        nomes=json.load(f)
    #cs=command split
    cs=command.split(sep=',')
    if command == "cp" or cs[0]=='cp':
        if len(cs)==1: personagem(0,0)
        elif len(cs)==2: personagem(cs[1],1)
        else: print('Escreva :cp,tipo de personagem')
    elif command == "co":
        n=batalha()
        #for no in n:
        #    restaurar(no,'f',1)
    elif command == "c" or cs[0]=='c':
        if len(cs)==1: checar(0,0)
        elif len(cs)==2: checar(cs[1],1)
        else: print('Escreva :c,oq vc deseja checar')
    elif command == "e" or cs[0]=='e':
        if len(cs)==1: editar(0,0)
        elif len(cs)==2: editar(cs[1],1)
        else: print('Escreva :c,quem vc deseja editar')
    elif command == "p" or cs[0]=='p':
        if len(cs)==1: printar(0,0)
        elif len(cs)==2: printar(cs[1],1)
        else: print('Escreva :p,oq vc deseja printar')
    elif command == "r" or cs[0]=='r':
        if len(cs)==1: restaurar(0,0,0)
        elif len(cs)==2:
            if cs[1]=='a':
                for n in nomes:
                    restaurar(n,'f',1)
            else: print('Digitou errado')
        elif len(cs)==3: restaurar(cs[1],cs[2],1)
        else: print('Escreva :r,quem vc deseja restaurar,oq vc deseja restaurar')
    elif command == "ait" or cs[0]=='a' or cs[0]=='add':
        if len(cs)==1: additem(0,0,0)
        elif len(cs)==2: print('Digitou errado')
        elif len(cs)==3: additem(cs[1],cs[2],1)
        else: print('Escreva :a,qual item vc deseja adicionar,quem vai ter o item adicionado')
    elif command=="lu" or cs[0]=='tl':
        if len(cs)==3: lvlup(cs[1],cs[2],2)
        else: lvlup(0,0,0)
    elif command == "a":
        add()
    elif command == "cm":
        mcreator()
    elif command == "cc":
        ccreator()
    elif command == "cr":
        rcreator()
    elif command == "cs":
        screator()
    elif command == "cw":
        wcreator()
    elif command == "ca":
        acreator()
    elif command == "uit" or cs[0]=='use':
        if len(cs)==1: useitem(0,0,0)
        elif len(cs)==2: print('Digitou errado')
        elif len(cs)==3: useitem(cs[1],cs[2],1)
        else: print('Escreva :use,qual item vc deseja usar,quem vai usar o item')
    else: print('Não existe essa opção')
