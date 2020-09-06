import json

with open('BattlemapWclasses/data/m.json') as g:
    M=json.load(g)

def cria():
    while True:
        n=input('Digite o nome da magia: ')
        if n=='n': break
        d=input('Descrição: ')
        t=input('tipo: ')
        l=input('lvl: ')
        c='q'
        cs=[]
        while True:
            c=input('Classe: ')
            if c=='n': break
            cs.append(c)
        M[n]=({'descricao':d,'classe':cs,'tipo':t,'lvl':l})

    with open('BattlemapWclasses/data/m.json','w') as f:
        json.dump(M,f)

def conta():
    n=0
    for x in M: n+=1
    print('n:',n)

def pa():
    for x in M:
        print(x,':')
        print('  tipo:',M[x].get('tipo'))
        print('  descrição:',M[x].get('descricao'))
        print('  lvl:',M[x].get('lvl'))
        c=M[x].get('classe')
        print('  classes:')
        for y in c: print('    ',y)
        print('\n\n')

pa()

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

    for x in cla:
        print(x,':')
        for y in cla[x]:
            print('   ',y)

    for x in cla2:
        print(x,':')
        for y in cla2[x]:
            print('   ',y)


'''
for key, value in M.items() :
    if ('lvl') in M[key]: print('deucerto')
    else:
        print('name:',key)
        n=input('lvl: ')
        if n=='s': break
        value['lvl']=n

with open('data/m.json','w') as f:
    json.dump(M,f)

print('foi')
'''