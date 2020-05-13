from .batalha.testedebatalha import batalha
from .jogadores.criacao_personagem import personagem
from .jogadores.checar import checar
from .jogadores.editor import editar
from .jogadores.print import printar
from .jogadores.nivel import level
from .funcoes.mestre import 

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
    else: print('Não existe essa opção')