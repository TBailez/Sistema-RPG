import json

with open('BattlemapWclasses/data/m.json') as g:
    M=json.load(g)

def cria():
    for m in M: last=m
    print('last:',last)
    while True:
        n=input('Digite o nome da magia: ')
        if n=='n': break
        d=input('Descrição: ')
        t=input('tipo: ')
        l=input('lvl: ')
        du=input('duration: ')
        c='q'
        cs=[]
        while True:
            c=input('Classe: ')
            if c=='all':
                cs=['bardo','wizard','sorcerer','dark lord','druid','paladin','healer','blood mage','warlock']
                while True:
                    que2=input('Digite o nome da magia q quer add ?')
                    if que2=='n': break
                    elif not que2 in cs:
                        print('n existe essa opção, classes:')
                        for Cc in cs: print(Cc)
                    else:
                        cs.remove(que2)
                        cs.append(que2+'?')
                while True:
                    que2=input('Deseja retirar algum?')
                    if que2=='n': break
                    elif not que2 in cs:
                        print('n existe essa opção, classes:')
                        for Cc in cs: print(Cc)
                    else: cs.remove(que2)
            elif c=='n': break
            else: cs.append(c)
        M[n]=({'descricao':d,'classe':cs,'tipo':t,'lvl':l,'duration':du})
    with open('BattlemapWclasses/data/m.json','w') as f:
        json.dump(M,f)

def ve():
    with open('BattlemapWclasses/data/m.json') as g:
        M=json.load(g)
    sair=False
    for x in M:
        if 'jogo' in M[x].keys(): pass
        else:
            print(x,':')
            print('  tipo:',M[x].get('tipo'))
            print('  descrição:',M[x].get('descricao'))
            print('  lvl:',M[x].get('lvl'))
            c=M[x].get('classe')
            print('  classes:')
            for y in c: print('    ',y)
            while True:
                B=True
                ver=input('\nVai querer essa magia ou n?(para oções digite help): ')
                if ver=='help':
                    print('  c=sim, magia de combate\n  h=sim, magia para historia\n  d=decide vc\n  n=nao\n  p=parar(salva as respostas e para o programa)\n  q=vc n deu informação suficiente')
                    B=False
                elif ver=='c':M[x]['jogo']='s/magia de combate'
                elif ver=='h': M[x]['jogo']='s/magia para historia'
                elif ver=='d': M[x]['jogo']='d'
                elif ver=='n': M[x]['jogo']='n'
                elif ver=='p': sair=True
                elif ver=='q': M[x]['jogo']='q'
                else:
                    print('Não existe essa opção')
                    B=False
                if B: break
            with open('BattlemapWclasses/data/m.json','w') as f:
                json.dump(M,f)
            print('-----------------------------------')
            if sair: break
            

def conta(): print('numero de magias:',len(M))

def pa():
    a=0
    for x in M:
        print(x,':')
        print('  tipo:',M[x].get('tipo'))
        print('  descrição:',M[x].get('descricao'))
        print('  lvl:',M[x].get('lvl'))
        c=M[x].get('classe')
        print('  classes:')
        for y in c: print('    ',y)
        print('\n\n')
        a+=1
        if a==20:
            a=0
            input('Continuar?: ')

def pt1():
    ts=[]
    for x in M:
        t=M[x].get('tipo')
        ty=t.split(sep='/')
        T=ty[0]
        Ts=T.split(sep='->')
        for y in Ts:
            s=(y.strip()).split(sep='?')
            if len(s)>1: Y=s[0]
            else: Y=y
            if Y.strip() in ts: pass
            else: ts.append(Y.strip())
    for x in ts: print(x)

def pt2():
    ts=[]
    for x in M:
        t=M[x].get('tipo')
        ty=t.split(sep='/')
        T=ty[1]
        Ts=T.split(sep='-')
        for y in Ts:
            s=(y.strip()).split(sep='?')
            if len(s)>1: Y=s[0]
            else: Y=y
            if Y.strip() in ts: pass
            else: ts.append(Y.strip())
    for x in ts: print(x)

def pt():
    pt1()
    pt2()

def pc():
    cla={}
    cla2={}
    for x in M:
        c=M[x].get('classe')
        for cl in c:
            cm=cl.split(sep='?')
            C=cm[0]
            if C=='idk': print('idk em:',x)
            if C in cla: pass
            else:
                cla[C]=[]
                cla2[C]=[]

    for x in M:
        c=M[x].get('classe')
        for cl in c:
            cm=cl.split(sep='?')
            n=(len(cm)-1)
            C=cm[0]
            a=0
            X=x
            while a<n:
                X=X+'?'
                a+=1
            cla[C].append(X)
            if n==0: cla2[C].append(x)
    q=input('Deseja ver todas(t,all,s) ou só as com certeza(c,n)?: ')
    if (q=='t') or (q=='all') or (q=='s'):
        for x in cla:
            print(x,':')
            for y in cla[x]:
                print('   ',y)
    if (q=='c') or (q=='n'):
        for x in cla2:
            print(x,':')
            for y in cla2[x]:
                print('   ',y)

def menager(qual='none'):
    if qual=='none': qual=input('Deseja usar qual função?: ')
    if qual=='cria': cria()
    elif qual=='conta': conta()
    elif qual=='pa': pa()
    elif qual=='pt': pt()
    elif qual=='pc': pc()
    elif qual=='ve': ve()
    elif qual=='n': return True
    else: print('Não existe essa opção')

while True:
    teste=menager('ve')
    if teste==None: pass
    else: break

'''
for key, value in M.items() :
    if ('lvl') in M[key]: print('deucerto')
    else:
        print('name:',key)
        n=input('lvl: ')
        if n=='s': break
        value['lvl']=n

with open('BattlemapWclasses/data/m.json','w') as f:
    json.dump(M,f)

print('foi')
'''

'''
def addtime():
    n=0
    for m in M:
        if ('duration') in (M[m].keys()): n+=1
    print('já tem',n)
    for m in M:
        if ('duration') in (M[m].keys()): pass
        else:
            print(m)
            M[m]['duration']=input('  duration: ')
            with open('BattlemapWclasses/data/m.json','w') as f:
                json.dump(M,f)
'''
'''
def add_ded():
    Cl={}
    cl=['bardo','healer','druid','paladin','ranger','sorcerer','warlock','wizard']
    try: 
        with open('BattlemapWclasses/data/c.json') as f:
            CL=json.load(f)
    except: CL={}
    else:
        with open('BattlemapWclasses/data/c.json') as f:
            CL=json.load(f)
    for c in cl:
        if c in CL.keys(): pass
        else:
            print('Digite as magias de '+c+': ')
            lm=[]
            while True:
                m=input()
                if m=='n': break
                else: lm.append(m)
            Cl[c]=lm
            s=input('Deseja continuar?: ')
            if s=='n':
                for CcC in Cl:
                    CL[CcC]=Cl[CcC]
                with open('BattlemapWclasses/data/c.json','w') as f:
                    json.dump(CL,f)
                break
'''