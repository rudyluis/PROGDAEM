# Diseña y desarrolla un sistema de reservas para un hotel en Python, utilizando 
# conceptos de programación orientada a objetos (POO). El sistema debe permitir a 
# los huéspedes realizar reservas, gestionar habitaciones y consultar disponibilidad 
# en el hotel.

from datetime import datetime, timedelta

class Habitacion:
    def __init__(self, num_habitacion, cap_max, precio_noche):
        self.num_habitacion = num_habitacion
        self.cap_max = cap_max
        self.disponibilidad = True
        self.precio_noche = precio_noche

    def __str__(self):
        return f"Habitación: {self.num_habitacion} - Capacidad: {self.cap_max} - Precio por noche: {self.precio_noche}"


class Reserva:
    def __init__(self, habitacion, check_in, check_out, nombre_huesped):
        self.habitacion = habitacion
        self.check_in = check_in
        self.check_out = check_out
        self.nombre_huesped = nombre_huesped
    
    def calcular_costo_reserva(self):
        dias = (self.check_out - self.check_in).days
        return dias * self.habitacion.precio_noche


class Hotel:
    def __init__(self):
        self.lista_habitaciones = []
        self.lista_reservas = []
    

    def consultar_disponibilidad(self, check_in, check_out, capacidad_requerida):
        habitaciones_disponibles = []
        for habitacion in self.lista_habitaciones:
            if habitacion.cap_max >= capacidad_requerida and habitacion.disponibilidad:
                habitaciones_disponibles.append(habitacion)
        return habitaciones_disponibles
                

    def realizar_reserva(self, habitacion, check_in, check_out, nombre_huesped):
        reserva = Reserva(habitacion, check_in, check_out, nombre_huesped)
        habitacion.disponibilidad = False
        self.lista_reservas.append(reserva)
        return reserva

    def cancelar_reserva(self, numero_habitacion, fecha_check_in, fecha_check_out):
        for reserva in self.lista_reservas:
            if reserva.habitacion.num_habitacion == numero_habitacion and reserva.check_in == fecha_check_in and reserva.check_out == fecha_check_out:
                reserva.habitacion.disponibilidad = True
                self.lista_reservas.remove(reserva)
                return True
        return False
    
    def mostrar_reservas(self):
        for reserva in self.lista_reservas:
            print(f"Habitación {reserva.habitacion.num_habitacion} - Check-in: {reserva.check_in} - Check-out: {reserva.check_in} - Huesped: {reserva.nombre_huesped}")


# Crear algunas habitaciones
habitacion1 = Habitacion(101, 2, 30)
habitacion2 = Habitacion(102, 4, 50)
habitacion3 = Habitacion(103, 6, 80)

# Crear el hotel
hotel = Hotel()
hotel.lista_habitaciones = [habitacion1, habitacion2, habitacion3]

# Simulación
while True:
    print("""
        Sistema de Reservas en un Hotel: \n\n
        1. Buscar habitaciones disponibles \n
        2. Realizar reserva \n
        3. Cancelar reserva \n
        4. Mostrar reservas \n
        5. Salir \n
    """)
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        fecha_check_in = datetime.strptime(input("Fecha de check-in (YYYY-MM-DD): "), "%Y-%m-%d")
        fecha_check_out = datetime.strptime(input("Fecha de check-out (YYYY-MM-DD): "), "%Y-%m-%d")
        capacidad_requerida = int(input("Capacidad deseada: "))

        habitaciones_disponibles = hotel.consultar_disponibilidad(fecha_check_in, fecha_check_out, capacidad_requerida)

        if habitaciones_disponibles:
            print("Habitaciones disponibles:")
            for habitacion in habitaciones_disponibles:
                print(habitacion)
        else:
            print("No hay habitaciones disponibles en esas fechas.")

    elif opcion == "2":
        numero_habitacion = int(input("Número de habitación: "))
        fecha_check_in = datetime.strptime(input("Fecha de check-in (YYYY-MM-DD): "), "%Y-%m-%d")
        fecha_check_out = datetime.strptime(input("Fecha de check-out (YYYY-MM-DD): "), "%Y-%m-%d")
        nombre_huesped = input("Nombre del huésped: ")

        for habitacion in hotel.lista_habitaciones:
            if habitacion.num_habitacion == numero_habitacion:
                reserva = hotel.realizar_reserva(habitacion, fecha_check_in, fecha_check_out, nombre_huesped)
                print(f"Reserva realizada: {reserva.habitacion} - Check-in: {reserva.check_in} - Check-out: {reserva.check_out}")
                break
        else:
            print(f"No se encontró la habitación con número {numero_habitacion}.")
    
    elif opcion == "3":
        numero_habitacion = int(input("Número de habitación: "))
        fecha_check_in = datetime.strptime(input("Fecha de check-in (YYYY-MM-DD): "), "%Y-%m-%d")
        fecha_check_out = datetime.strptime(input("Fecha de check-out (YYYY-MM-DD): "), "%Y-%m-%d")

        if hotel.cancelar_reserva(numero_habitacion, fecha_check_in, fecha_check_out):
            print("Reserva cancelada correctamente.")
        else:
            print("No se encontró una reserva con los datos proporcionados.")

    elif opcion == "4":
        print("Reservas:")
        hotel.mostrar_reservas()
    
    elif opcion == "5":
        print("¡Gracias por usar nuestro sistema de reservas!")
        break

