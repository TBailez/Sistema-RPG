

def eqar():
 arma=list()
 arma=['sword','staff',['gaunlet'],['adaga']]
 print(arma)
 no=input('Qual arma vc quer equipar?\n')
 if no in arma:
    arma.index(no)
    arma.remove(no)
    arma.insert(0,no)
    print('Você equipou',arma[0])
 else: print('Você não tem essa arma')
 