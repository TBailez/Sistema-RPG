class dragon:
    def __init__(self):
        print('teste1')
    
    def fire_breath(self):
        print('firebreath')


class person:
    def __init__(self):
        print('teste2')

    def speak(self):
        print('ah!')

class goat:
    def __init__(self):
        print('teste3')

    def walk(self):
        print('walked')

t='dragon'

class criatura(dragon if t=='dragon' else person if t=='person' else goat):
    def __init__(self):
        super().__init__()

Object=criatura()
Object.fire_breath()
Object.speak()

