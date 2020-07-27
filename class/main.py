from scripts.creator import ini
from scripts.creator import cria
from scripts.creator import le
from scripts.combate import combate

while True:
    i=input('Deseja usar qual função?')
    if i=='i': ini()
    if i=='c': cria()
    if i=='l': le()
    if i=='o': combate()
    if i=='b': break

#  Vc tem q usar a função ini antes de qualquer outra pro programa funfar
#          ^
#          |
#       Só se n tiver nada em nos pickles 