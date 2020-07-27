import pickle
from data.classes import personagem
from data.classes import arma

def combate():
    with open('class/data/p.pickle','rb') as f:
        p=pickle.load(f)
    with open('class/data/a.pickle','rb') as f:
        a=pickle.load(f)
    vf=0
    hs=[]
    for c in p:
        hs.append(p[c].hp)
        vi=p[c].vel
        if vi>vf: vf=vi
    for jk in p:
        if p[jk].vel==vf: nome=p[jk].nome
        else: nome2=p[jk].nome
    while True:
        atk=[]
        print('É sua vez',nome)
        print('Qual seu ataque?')
        for mn in dir(a[p[nome].arma]):
            try: callable(getattr(a[p[nome].arma],mn)(1,1))
            except: pass
            else:
                if mn=='__subclasshook__': pass
                else:
                    atk.append(mn)
                    print('  ',mn)
        while True:
            atkc=input()
            if atkc in atk: break
            else: print('Não existe esse ataque')
        fo=int(p[nome].forca)
        ve=int(p[nome].vel)
        d=getattr(a[p[nome].arma],atkc)(fo,ve)
        print('hp inicial:',p[nome2].hp)
        print('armor:',p[nome2].armor)
        p[nome2].hp-=d-p[nome2].armor
        print('dano',d)
        print('hp final:',p[nome2].hp)
        print('deseja continuar o combate?(s ou n)')
        op=input()
        if op=='s':
            nome3=nome
            nome=nome2
            nome2=nome3
        elif op=='n': break
        else: print('Não existe essa opção')
        