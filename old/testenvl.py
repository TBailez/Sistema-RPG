from nivel import level
level()
        if spell.get('Type')=='heal':
            while True:
                qual=input('Qual nome do personagem que você deseja healar?')
                if qual in combatentes: break
                else: print('Esse personagem não está no combate')
            if combatentes.get(qual).get('hp')+spell.get('dano')>combatentes.get(qual).get('chp')*15: combatentes[qual]['hp']=combatentes.get(qual).get('chp')*15
            else: combatentes[qual]['hp']+=spell.get('dano')
            return 0