from claseAparato import AparatoElectronico
class lavarropas(AparatoElectronico):
    __capacidad=None
    __velocidad=None
    __cantidadDeProgramas=None
    __tipoDeCarga=None
    def __init__(self,marca,modelo,color,pais,precio,capacidad,velocidad,cantidad,carga):
        super(lavarropas, self).__init__(marca,modelo,color,pais,precio)
        self.__capacidad=int(capacidad)
        self.__velocidad=velocidad
        self.__cantidadDeProgramas=cantidad
        self.__tipoDeCarga=carga
    def getImporte(self):
        importe=self.getPrecioBase()
        if self.__capacidad > 5:
            importe+=self.getPrecioBase()*0,03
        else:
            importe+=self.getPrecioBase()*0,01
        return importe

