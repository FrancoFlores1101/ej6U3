class menu:
    def iniciar(self):
        print('----Menu----')
        print('1- Insertar aparato en una posición')
        print('2- Agregar aparato')
        print('3- Mostrar aparato en posición')
        print('4- Mostrar aparatos philips')
        print('5- Mostrar Lavarropas con carga superior')
        print('6- Listar todos los aparatos')
        print('7- Almacenar objetos')
        print('0- Salir')
        opcionCorrecta=False
        while not opcionCorrecta:
            opcion=int(input())
            if opcion in [1,2,3,4,5,6,7]:
                opcionCorrecta=True
        return opcion
