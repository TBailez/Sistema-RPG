from .batalha.testedebatalha import batalha
from .jogadores.criacao_personagem import personagem

def menu(command):
    if command == "cp": 
        personagem()
    elif command == "co":
        batalha()
    elif command == "s": pass