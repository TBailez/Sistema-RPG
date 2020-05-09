from .batalha.testedebatalha import batalha
from .jogadores.criacao_personagem import personagem
from .jogadores.checar import checar
from .jogadores.editor import editar

def menu(command):
    if command == "cp": 
        personagem()
    elif command == "co":
        batalha()
    elif command == "c":
        checar()
    elif command == "e":
        editar()
    else: print('Não existe essa opção')