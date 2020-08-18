import pickle
from data.classes import arma
from data.classes import Piercing
from data.classes import Blunt

def cria():
    print('Qual o nome da arma?')
    n=input()
    while True:
        print('A arma é piercing(p), blunt(b) ou os 2(2)?')
        x=input()
        if x=='p':
            t=(arma,Piercing)
            break
        elif x=='b':
            t=(arma,Blunt)
            break
        elif x=='2':
            t=(arma,Piercing,Blunt)
            break
        else: print('Não existe essa opção')
    teste=type(n,t,{'durabilidade':20,'material':'steel'})
    getattr(teste,'__init__')(teste,n)
    for func in dir(teste):
        lista=func.split(sep='_')
        if len(lista)==2 and lista[0]=='i':
            getattr(teste,func)(teste)
            '''
    with open('class2/data/a.pickle','rb') as f:
        dic=pickle.load(f)
    print('dic: ',dic)
    dic[n]=teste
    with open('class2/data/a.pickle','wb') as f:
        pickle.dump(dic,f)
    with open('class2/data/a.pickle','rb') as f:
        dic=pickle.load(f)
    print('dic2: ',dic)
    '''

#def printt():
    o=teste
    k=list(o.__dict__.keys())
    v=list(o.__dict__.values())
    print('Nome:',o.nome)
    aux=len(k)
    while aux>0:
        spl=k[aux-1].split(sep='__')
        if len(spl)>1:
            del k[aux-1]
            del v[aux-1]
        aux-=1
    for a,b in zip(k,v):
        if a=='nome': pass
        else: print('  ',a,':',b)
