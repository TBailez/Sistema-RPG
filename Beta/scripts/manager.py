import json
from .batalha.testedebatalha import batalha
from .jogadores.criacao_personagem import personagem
from .jogadores.checar import checar
from .jogadores.editor import editar
from .jogadores.print import printar
from .funcoes.restore import restaurar
from .funcoes.adicionar import add
from .funcoes.lvlup import lvlup

with open('Beta/data/nomes.json') as f:
    nomes=json.load(f)

def menu(command):
    #cs=command split
    cs=command.split(sep=' ')
    if command == "cp": 
        personagem()
    elif command == "co":
        batalha()
    elif command == "c" or cs[0]=='c':
        if len(cs)==1: checar(0,0)
        elif len(cs)==2: checar(cs[1],1)
        else: print('Escreva :c-espaço-oq vc deseja checar')
    elif command == "e":
        editar()
    elif command == "p" or cs[0]=='p':
        if len(cs)==1: printar(0,0)
        elif len(cs)==2: printar(cs[1],1)
        else: print('Escreva :p-espaço-oq vc deseja printar')
    elif command == "r" or cs[0]=='r':
        if len(cs)==1: restaurar(0,0,0)
        elif len(cs)==2:
            if cs[1]=='a':
                for n in nomes:
                    restaurar(n,'f',1)
            else: print('Digitou errado')
        elif len(cs)==3: restaurar(cs[1],cs[2],1)
        else: print('Escreva :r-espaço-quem vc deseja restaurar-espaço-oq vc deseja restaurar')
    elif command == "a":
        add()
    elif command=="lu":
        lvlup(0,0,0)
    else: print('Não existe essa opção')