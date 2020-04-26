
nome = input('Qual seu nome? \n')
FOR = input('Quanto de força você tem? \n')
INT = input('Quanto de inteligência você tem? \n')
RES = input('Quanto de resistência você tem? \n')
ING = input('Quanto de intransigência você tem? \n')
VEL = input('Quanto de velocidade você tem? \n')
CHP = input('Quanto é seu coeficiente de HP? \n')
CMN = input('Quanto é seu coeficiente de MANA? \n')
int_CHP = int(CHP)
int_CMN = int(CMN)
int_FOR = int(FOR)
int_INT = int(INT)
int_RES = int(RES)
int_ING = int(ING)
int_VEL = int(VEL)
RAÇA = input('Qual a sua Raça? \n')
if RAÇA == 'Humano' :
    int_FOR += 1
    int_RES += 1
    int_VEL += 1
    
elif RAÇA == 'Elfo':
    int_INT += 2
    int_VEL += 1
elif RAÇA == 'Orc':
    int_FOR += 2
    int_RES += 2
    int_CHP += 1
    int_INT -= 1
    int_VEL -= 1
    

HP = int_CHP*15
MN = int_CMN*15
print('Os status de',(nome),'são:')
print('HP:',(HP))
print('MANA:',(MN))
print('Força:',(int_FOR))
print('Inteligência:',(int_INT))
print('Resistência:',(int_RES))
print('Instransigência:',(int_ING))
print('Velocidade:',(int_VEL))
