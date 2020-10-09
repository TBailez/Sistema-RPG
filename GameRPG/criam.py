from data.magias import dano
from data.magias import buff_debuff
from data.magias import healing
import pickle

def cria():
    while True:
        nome=input('Digite o nome da magia(para sair digite n): ')
        if nome=='n': break
        mana=input('Digite quanto de mana a magia vai custar: ')
        ms=[]
        number=1
        while True:
            if number>1: qual=input('Qual o tipo da magia?(dano(d)/healing(h)/buff_debuff(b)/para sair digite n)')
            else: qual=input('Qual o tipo da magia?(dano(d)/healing(h)/buff_debuff(b))')
            if qual=='d':
                m=dano(number,nome,mana)
                number+=1
            elif qual=='b':
                m=buff_debuff(number,nome,mana)
                number+=1
            elif qual=='h':
                m=healing(number,nome,mana)
                number+=1
            elif (qual=='n') and (number>1):
                break
            else: print('Não existe essa opção')
            ms.append(m)
        try:
            with open('GameRPG/data/magias.pickle','rb') as f:
                M=pickle.load(f)
        except: M=[]
        M.append(ms)
        with open('GameRPG/data/magias.pickle','wb') as f:
            pickle.dump(M,f)

def ler():
    with open('GameRPG/data/magias.pickle','rb') as f:
        M=pickle.load(f)
        for m in M:
            print((m[0].nome+':'))
            rd={}
            for x in m:
                print('  ',x)
                d=dir(x)
                for c in d:
                    ds=c.split(sep='__')
                    if len(ds)==1: rd[c]=getattr(x,c)
            rd['nome']=m[0].nome
            print('   atributos:',rd)

ler()