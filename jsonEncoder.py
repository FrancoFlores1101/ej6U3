import json
from ColeccionAparatos import coleccion

class ObjectEncoder(object):
    def abrirJSON(self):
        data= open('aparatoselectronicos.json')
        diccionario=json.load(data)
        data.close()
        return diccionario

    def decodificarDiccionario(self, d):
        retorno = None
        if "__class__" not in d:
            retorno = d
        else:
            class_name = d["__class__"]
            class_ = eval(class_name)
            if class_name == "ColeccionAparatos":
                aparatos = d["aparatos"]
                unaColeccionAparatos:coleccion = class_()
                for i in range(len(aparatos)):
                    dAparato = aparatos[i]
                    class_name = dAparato.pop("__class__")
                    class_ = eval(class_name)
                    atributos = dAparato["__atributos__"]
                    unAparato = class_(**atributos)
                    unaColeccionAparatos.insertarElemento(unAparato, 0)
            retorno = unaColeccionAparatos
        return retorno
