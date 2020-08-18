import matplotlib.pyplot as plt

#n fiz nada aqui ainda

plt.ion()

class map:
    def __init__(self):
        self.fig=plt.figure()
        self.axes=self.fig.add_subplot(111)

def cria():
    mapa=map()
    plt.show()
    s=input()