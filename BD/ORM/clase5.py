class mascota:
    def __init__(self,nombre,raza,edad):
        self._nombre=nombre
        self._edad=edad
        self._raza=raza
   
    def saludar(self):
        print("Hola mi nombre es ",self._nombre," soy de raza",self._raza," y tengo ",self._edad," años.")

class propietario:
    def __init__(self,nombre,telefono):
        self._nombre=nombre
        self._telefono=telefono
       
    def mostrar_contacto(self):
        print("Nombre: ",self._nombre)
        print("Telefono: ",self._telefono)

class adopcionMascota:
    def __init__(self, mascota, propietario):
        self.mascotas=[mascota]
        self.propietarios= {mascota: propietario}

    def adoptarNuevaMascota(self, nueva_mascota, nuevo_propietario):
        self.mascotas.append(nueva_mascota)
        self.propietarios[nueva_mascota]=nuevo_propietario

        print("Mascota registrada correctamente.... :)")
        print("Propietario:", nuevo_propietario._nombre)
        nueva_mascota.saludar()
    
    def mostrarMascotas(self):
        for mascota in self.mascotas:
            mascota.saludar()
            print("Propietario:", self.propietarios[mascota]._nombre)

if __name__=="__main__":
    mascota1= mascota('Oreo','Hasky','5')
    mascota2= mascota('Kiwi Firulais','Pequines','3')
    propietario1= propietario( 'Melissa','123456')

    adopcion= adopcionMascota(mascota1, propietario1)
    adopcion.adoptarNuevaMascota(mascota2, propietario1)

    adopcion.mostrarMascotas()