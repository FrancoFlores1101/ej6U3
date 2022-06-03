from claseAparato import  AparatoElectronico
from claseTelevisor import televisor
from claseHeladera import heladera
from claseLavarropas import lavarropas
from interface import Icoleccion
from zope.interface import implementer


@implementer(Icoleccion)
class coleccion:
    __Comienzo=None
    __Actual=None
    __indice=None
    __tope=None
    def __init__(self):
        self.__Comienzo=None
        self.__Actual=self.__Comienzo
        self.__indice=0
        self.__tope=0
    def agregarElemento(self,elemento):
        unNodo=Nodo(elemento)
        if self.__Comienzo == None:
            self.__Comienzo=unNodo
            self.__Actual=self.__Comienzo
        else:
            aux=self.__Comienzo
            while aux.getSiguiente() != None
                aux=aux.getSiguiente()
            aux.setSiguiente(unNodo)
        self.__tope+=1
    def insertarElemento(self,elemento,indice):
        unNodo=Nodo(elemento)
        insertado=False
        if indice == 0:
            unNodo.setSiguiente(self.__Comienzo)
            self.__Comienzo=unNodo
            self.__Actual=self.__Comienzo
            insertado=True
        else:
            if self.__Comienzo != None:
                i=1
                aux=self.__Comienzo
                while aux.getSiguiente() != None and i < indice:
                    aux=aux.getSiguiente()
                    i+=1
                if i == indice:
                    unNodo.setSiguiente(aux.getSiguiente)
                    aux.setSiguiente(unNodo)
                    insertado=True
                else:
                    raise IndexError('indice fuera de rango')
        self.__tope+=1
        return insertado

    def mostrarElemento(self,indice):
        if indice=0:
            if self.__Comienzo== None:
                raise IndexError('indice fuera de rango')
            unNodo=self.__Comienzo
        else:
            i=1
            if self.__Comienzo== None:
                raise IndexError('indice fuera de rango')
            unNodo=self.__Comienzo.getSiguiente()
            while i < indice and unNodo.getSiguiente() != None:
                i+=1
                unNodo=unNodo.getSiguiente()
            if i < indice:
                raise IndexError('indice fuera de rango')
        unAparato=unNodo.getDato()
        print(unAparato)
    def __iter__(self):
        return self
    def mostrarPhilips(self):
        if self.__Comienzo != None:
            aux=self.__Comienzo
            while aux != None:
                unAparato=aux.getDato()
                if unAparato.getMarca() == 'Philips'
                    print(unAparato)
                aux=aux.getSiguiente()
        else:
            print('lista vacia')
    def mostrarTodos(self):
         if self.__Comienzo != None:
            aux=self.__Comienzo
            while aux != None:
                unAparato=aux.getDato()
                    print(unAparato)
                aux=aux.getSiguiente()
        else:
            print('lista vacia')
