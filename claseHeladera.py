from claseAparato import  AparatoElectronico

class heladera(AparatoElectronico):
    __capacidad=None
    __freezer=None
    __ciclica=None
    def __init__(self,marca,modelo,color,pais,precio,capacidad,freezer:bool,ciclica:bool):
        super(heladera, self).__init__(marca,modelo,color,pais,precio)
        self.__capacidad=capacidad
        self.__freezer=freezer
        self.__ciclica=ciclica
    def getImporte(self) -> float:
        importe=self.getPrecioBase()
        if self.__freezer:
            importe+=self.getPrecioBase()*0,05
        else:
            importe+=self.getPrecioBase()*0,01
        if self.__ciclica:
            importe+=self.getPrecioBase()*0,1
        return importe
