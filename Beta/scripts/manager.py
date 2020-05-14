from .batalha.testedebatalha import batalha
from .jogadores.criacao_personagem import personagem
from .jogadores.checar import checar
from .jogadores.editor import editar
from .jogadores.print import printar
from .funcoes.restore import restaurar
from .funcoes.adicionar import add

def menu(command):
    if command == "cp": 
        personagem()
    elif command == "co":
        batalha()
    elif command == "c":
        checar()
    elif command == "e":
        editar()
    elif command == "p":
        printar()
    elif command == "r":
        restaurar()
    elif command == "a":
        add()
    else: print('Não existe essa opção')