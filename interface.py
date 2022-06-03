from zope.interface import Interface
from zope.interface import implementer

class Icoleccion(Interface):
    def insertarElemento(self,elemento:object,pos:int):
        pass
    def agregarElemento(self,elemento:object):
        pass
    def mostrarElemento(self,pos:int):
        pass
