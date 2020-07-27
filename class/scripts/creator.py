import pickle
from data.classes import personagem
from data.classes import arma
def cria():
    c=input('deseja criar um personagem ou uma arma?')
    if c=='p':
        n=input('Digite o nome do seu personagem: ')
        h=input('Digite o hp dele: ')
        v=input('Digite a velocidade dele: ')
        f=input('Digite sua força: ')
        a=input('Digite sua arma: ')
        r=input('Digite a armadura: ')
        p=personagem(h,r,v,f,a,n)
        with open('data/p.pickle','rb') as f:
            dik=pickle.load(f)
        dik[n]=p
        with open('data/p.pickle','wb') as g:
            pickle.dump(dik,g)
    elif c=='a':
        n=input('Digite o nome da sua arma: ')
        v=input('Digite a velocidade dela: ')
        r=input('Digite a durabilidade: ')
        d=input('Digite o dano: ')
        a=arma(d,r,v,n)
        with open('data/a.pickle','rb') as f:
            dik=pickle.load(f)
        dik[n]=a
        with open('data/a.pickle','wb') as g:
            pickle.dump(dik,g)
    else: print('Não existe essa opção')

def ini():
    dik={}
    with open('data/p.pickle','wb') as g:
        pickle.dump(dik,g)
    with open('data/a.pickle','wb') as gg:
        pickle.dump(dik,gg)
def le():
    with open('data/p.pickle','rb') as j:
        le=pickle.load(j)
        for n in le:
            l=le[n]
            print(vars(l))
    with open('data/a.pickle','rb') as jo:
        le2=pickle.load(jo)
        for n in le2:
            l1=le2[n]
            print(vars(l1))
        #print('Ve se funfa:',l.__dict__.keys())
        #print(l)
