x=1
f=int(input("força do atacante:"))
ba=int(input("bonus da arma do atacante:"))
va=int(input("velocidade do atacante:"))
d=int(input("fortitude do defensor:"))
bd=int(input("bonus da armadura do defensor:"))
vd=int(input("velocidade do defensor:"))
while x==1:
    d1=int(input("dado 1:"))
    d2=int(input("dado 2:"))
    qa=f+ba+(d1-d2)
    qd=d+bd
    qva=(d1-d2)+va
    dano=qa-qd
    desvio=qva-vd
    print("Dano =",dano," :(",f,"+",ba,"+",(d1-d2),")-(",d,"+",bd,")")
    if desvio<=0:
        print("Desvio")
    else:
        print("Dano =",int(dano*1.5)," :(",f,"+",ba,"+",(d1-d2),")-(",d,"+",bd,")x1,5")
    x=int(input("Tentar d en ovo?"))
