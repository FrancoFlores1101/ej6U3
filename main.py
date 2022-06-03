from jsonEncoder import ObjectEncoder
from claseHeladera import heladera
from claseLavarropas import lavarropas
from claseTelevisor import televisor
from Menu import menu
from ColeccionAparatos import coleccion

if __name__ == '__main__':
    jsonF=ObjectEncoder()
    diccionario=jsonF.abrirJSON()
    unaColeccion=jsonF.decodificarDiccionario(diccionario)
    MenuOpciones=menu()
    opcion=MenuOpciones.iniciar()
    while opcion != 0:
        if opcion==1:
            print('Ingrese el tipo de aparato, sus datos y la posicion')
            posicion=int(input('Posicion: '))
            print('[1] Televisor  [2] Lavarropas [3] Heladera')
            tipo=int(input())

            if tipo==1
                marca=input('Marca')
                modelo=input('Modelo')
                color=input('Color')
                pais=input('Pais de Fabricación')
                precio=input('Precio Base')
                tipodepantalla=input('Tipo de pantalla')
                pulgadas=input('Pulgadas')
                tipodedefinicion=input('Tipo de definición')
                bandera=int(input('Internet? 1:SI 0:NO')
                if bandera == 1:
                    internet=True
                else:
                    internet=False
                unAparato=televisor(marca,modelo,color,pais,precio,tipodepantalla,pulgadas,tipodedefinicion,internet)
                unaColeccion.insertarElemento(unAparato,posicion)
            elif tipo==2
                marca=input('Marca')
                modelo=input('Modelo')
                color=input('Color')
                pais=input('Pais de Fabricación')
                precio=input('Precio Base')
                capacidad=input('Capacidad en Litros')
                bandera=int(input('Freezer? 1:SI 0:NO')
                if bandera == 1:
                    freezer=True
                else:
                    freezer=False
                bandera=int(input('cíclica? 1:SI 0:NO')
                if bandera == 1:
                    ciclica=True
                else:
                    ciclica=False
                unAparato=heladera(marca,modelo,color,pais,precio,capacidad,freezer,ciclica)
                unaColeccion.insertarElemento(unAparato,posicion)
            elif tipo==3
                marca=input('Marca')
                modelo=input('Modelo')
                color=input('Color')
                pais=input('Pais de Fabricación')
                precio=input('Precio Base')
                capacidad=input('Capacidad de lavado')
                velocidad=input('velocidad de centrifugado')
                cantidaddeprogramas=input('cantidad de programas')
                tipodecarga=input('tipo de carga')
                unAparato=heladera(marca,modelo,color,pais,precio,capacidad,velocidad,cantidaddeprogramas,tipodecarga)
                unaColeccion.insertarElemento(unAparato,posicion)
            else:
                print('numero invalido')
        elif opcion==2:
            print('Ingrese el tipo de aparato, sus datos')
            print('[1] Televisor  [2] Lavarropas [3] Heladera')
            tipo=int(input())
            if tipo==1
                marca=input('Marca')
                modelo=input('Modelo')
                color=input('Color')
                pais=input('Pais de Fabricación')
                precio=input('Precio Base')
                tipodepantalla=input('Tipo de pantalla')
                pulgadas=input('Pulgadas')
                tipodedefinicion=input('Tipo de definición')
                bandera=int(input('Internet? 1:SI 0:NO')
                if bandera == 1:
                    internet=True
                else:
                    internet=False
                unAparato=televisor(marca,modelo,color,pais,precio,tipodepantalla,pulgadas,tipodedefinicion,internet)
                unaColeccion.agregarElemento(unAparato)
            elif tipo==2
                marca=input('Marca')
                modelo=input('Modelo')
                color=input('Color')
                pais=input('Pais de Fabricación')
                precio=input('Precio Base')
                capacidad=input('Capacidad en Litros')
                bandera=int(input('Freezer? 1:SI 0:NO')
                if bandera == 1:
                    freezer=True
                else:
                    freezer=False
                bandera=int(input('cíclica? 1:SI 0:NO')
                if bandera == 1:
                    ciclica=True
                else:
                    ciclica=False
                unAparato=heladera(marca,modelo,color,pais,precio,capacidad,freezer,ciclica)
                unaColeccion.agregarElemento(unAparato)
            elif tipo==3
                marca=input('Marca')
                modelo=input('Modelo')
                color=input('Color')
                pais=input('Pais de Fabricación')
                precio=input('Precio Base')
                capacidad=input('Capacidad de lavado')
                velocidad=input('velocidad de centrifugado')
                cantidaddeprogramas=input('cantidad de programas')
                tipodecarga=input('tipo de carga')
                unAparato=heladera(marca,modelo,color,pais,precio,capacidad,velocidad,cantidaddeprogramas,tipodecarga)
                unaColeccion.agregarElemento(unAparato)
            else:
                print('numero invalido')
        elif opcion==3:
            p=int(input('posicion del aparato a mostrar:'))
            unaColeccion.mostrarElemento(p)
        elif opcion==4:
            unaColeccion.mostrarPhilips()
        elif opcion==5:
            unaColeccion
        elif opcion==6:
            unaColeccion.mostrarTodos()
        elif opcion==7:

        opcion=MenuOpciones.iniciar()

