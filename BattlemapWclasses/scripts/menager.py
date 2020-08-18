from .MapC import cria

def menage(x):
    if x=='c': cria()
    elif x=='help': print('Opcões: c / help')
    else: print('Não existe essa opção')