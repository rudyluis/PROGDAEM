class vehiculo:
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

class auto(vehiculo):
    def __init__(self, marca, modelo, anio, color, precio, velocidad_maxima, transmision):
        super().__init__(marca, modelo, anio, color, precio, velocidad_maxima)
        self._transmision=transmision
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print('Tipo de Transmision', self._transmision)

class moto(vehiculo):
    def __init__(self, marca, modelo, anio, color, precio, velocidad_maxima,pata_cabra):
        super().__init__(marca, modelo, anio, color, precio, velocidad_maxima)
        self._pata_cabra=pata_cabra
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print('Pata Cabra', self._pata_cabra)

if __name__ =="__main__":
    auto1= auto('Suzuki','Desire','2024','Negro',15000,200,'Automatica')
    auto1.mostrar_informacion()
    print('--------')
    moto1= moto('Honda','Bonito y Rojo','2024','rojo','3000',240,'si')
    moto1.mostrar_informacion()