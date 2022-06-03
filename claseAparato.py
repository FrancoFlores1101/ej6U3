from abc import ABC
import abc

class AparatoElectronico(ABC):
    __marca=None
    __modelo=None
    __color=None
    __paisDeFabricacion=None
    __precioBase=None
    def __init__(self,marca,modelo,color,pais,precio):
        self.__marca=marca
        self.__modelo=modelo
        self.__color=color
        self.__paisDeFabricacion=pais
        self.__precioBase=float(precio)
    def __str__(self):
        cadena = "Marca: {0}\n".format(self.__marca)
        cadena += "Modelo: {0}\n".format(self.__modelo)
        cadena += "Color: {0}\n".format(self.__color)
        cadena += "Pais de origen: {0}\n".format(self.__paisDeFabricacion)
        cadena += "Precio Base: {0}\n".format(self.__precioBase)
        return cadena
    def getPrecioBase(self):
        return self.__precioBase
    def getMarca(self):
        return self.__marca
    @abc.abstractmethod
    def getImporte(self):
        pass


