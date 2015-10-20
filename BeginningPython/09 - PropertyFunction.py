'''
Este script mostra como e possivel utilizar propriedades em uma classe
Nao esquecer de a classe herdar a classe object, pois pode ser que a funcao get funcione a nao a funcao set.
'''



__author__ = 'daniloqb'



class Rectangule(object):
    def __init__(self):
        self.width = 0
        self.height = 0

    def setSize(self,size):
        self.width, self.height = size

    def getSize(self):
        return self.width, self.height


    # Criando uma propriedade para a classe
    size = property(getSize,setSize)




r = Rectangule()

r.width = 10
r.height = 5

print r.getSize()

r.setSize((100,50))

print r.getSize()


#usando a propriedade size da classe Rectangule
r.size = 640,480

print r.size