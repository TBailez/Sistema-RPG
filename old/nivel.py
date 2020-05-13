
def level():
    xp=int(input('Quanto de xp inicial você tem?\n'))
    if xp < 50:
      lvl = 1
      print(lvl)
    elif xp < 300:
      lvl = 2
    elif xp < 1300:
      lvl = 3
    elif xp < 3050:
      lvl = 4
    elif xp < 5550:
      lvl = 5
    elif xp < 10550:
      lvl = 6
    elif xp < 16800:
      lvl = 7
    elif xp < 24300:
      lvl = 8
    elif xp < 33900:
      lvl = 9
    elif xp < 42000:
      lvl = 10
    elif xp < 55600:
      lvl = 11
    elif xp < 69000:
      lvl = 12
    elif xp < 84000:
      lvl = 13  
    elif xp < 101350:
      lvl = 14
    elif xp < 121350:
      lvl = 15
    elif xp < 148850:
      lvl = 16
    elif xp < 183850:
      lvl = 17
    elif xp < 225000:
      lvl = 18
    elif xp < 300000:
      lvl = 19
    elif xp > 250000:
      lvl = 20