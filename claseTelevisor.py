from claseAparato import AparatoElectronico

class televisor(AparatoElectronico):
    __tipoDePantalla=None
    __pulgadas=None
    __tipoDefinicion=None
    __conexion=None
    def __init__(self,marca,modelo,color,pais,precio,tipo,pulgada,definicion,conexion):
        super(televisor, self).__init__(marca,modelo,color,pais,precio)
        self.__tipoDePantalla=tipo
        self.__pulgadas=pulgada
        self.__tipoDefinicion=definicion
        self.__conexion=conexion
    def getImporte(self):
        importe=self.getPrecioBase()
        if self.__tipoDefinicion == 'SD'
            importe=self.getPrecioBase()*0,01
        elif self.__tipoDefinicion=='HD'
            importe=self.getPrecioBase()*0,02
        elif self.__tipoDefinicion=='FULL HD'
            importe=self.getPrecioBase()*0,03
        if self.__conexion:
            importe+=self.getPrecioBase()*0,1



