class auto:
    def __init__(self, marca, modelo, anio, color, precio, velocidad_maxima):
        self._marca=marca
        self._modelo=modelo
        self._anio=anio
        self._color=color
        self._precio=precio
        self._velocidad_maxima=velocidad_maxima
        self._velocidad_actual=0

    def mostrar_informacion(self):
        print('Marca:',self._marca)
        print('Modelo:',self._modelo)
        print('Año:',self._anio)
        print('Color:',self._color)
        print('Precio:',self._precio)
        print('Velocidad Maxima:',self._velocidad_maxima)
        print('Velocidad Actual:',self._velocidad_actual)

    def acelerar(self, velocidad_aumento):
        if(self._velocidad_actual+velocidad_aumento<=self._velocidad_maxima):
            self._velocidad_actual+=velocidad_aumento
            print('La velocidad del auto es--->',self._velocidad_actual)
        else:
            print("El auto ha alcanzado su velocidad maxima")
    def frenar (self, velocidad_frenado):
        if(self._velocidad_actual-velocidad_frenado>0):
            self._velocidad_actual-=velocidad_frenado
            print('La velocidad del auto es--->',self._velocidad_actual)
        else:
            print('El coche se ha detenido')
            self._velocidad_actual=0

if __name__ =="__main__":
    auto1= auto('Suzuki','Desire','2024','Negro',15000,200)
    print('Informacion del Auto')
    auto1.mostrar_informacion()
    auto1.acelerar(20)
    auto1.acelerar(30)
    auto1.acelerar(80)
    ##auto1.acelerar(100)
   
    auto1.frenar(50)
    auto1.frenar(30)
    auto1.frenar(100)
    auto1.frenar(30)
    auto1.frenar(30)