from datetime import datetime

class Habitacion:
    def __init__(self, num_habitacion, cap_max, precio_noche):
        self.num_habitacion = num_habitacion
        self.cap_max = cap_max
        self.precio_noche = precio_noche
        self.disponibilidad = True

    def __str__(self):
        return (f"Habitación {self.num_habitacion}: "
                f"Capacidad máxima {self.cap_max}, "
                f"Precio por noche ${self.precio_noche}, "
                f"{'Disponible' if self.disponibilidad else 'Ocupada'}")


class Reserva:
    def __init__(self, habitacion, check_in, check_out, nombre_huesped):
        self.habitacion = habitacion
        self.check_in = check_in
        self.check_out = check_out
        self.nombre_huesped = nombre_huesped

    def calcular_costo_reserva(self):
        dias = (self.check_out - self.check_in).days
        return dias * self.habitacion.precio_noche

    def __str__(self):
        return (f"Habitación {self.habitacion.num_habitacion} - "
                f"Huésped: {self.nombre_huesped}, "
                f"Check-in: {self.check_in.date()}, "
                f"Check-out: {self.check_out.date()}, "
                f"Costo: ${self.calcular_costo_reserva()}")


class Hotel:
    def __init__(self):
        self.lista_habitaciones = []
        self.lista_reservas = []

    def agregar_habitacion(self, habitacion):
        self.lista_habitaciones.append(habitacion)

    def consultar_disponibilidad(self, check_in, check_out, capacidad_requerida):
        habitaciones_disponibles = []
        for habitacion in self.lista_habitaciones:
            if (habitacion.cap_max >= capacidad_requerida and habitacion.disponibilidad):
                habitaciones_disponibles.append(habitacion)
        return habitaciones_disponibles

    def realizar_reserva(self, num_habitacion, check_in, check_out, nombre_huesped):
        self.lista_reservas.append(reserva)
        for habitacion in self.lista_habitaciones:
            if habitacion.num_habitacion == num_habitacion and habitacion.disponibilidad:
                reserva = Reserva(habitacion, check_in, check_out, nombre_huesped)
                habitacion.disponibilidad = False
                self.lista_reservas.append(reserva)
                return reserva
        return None

    def cancelar_reserva(self, num_habitacion):
        for reserva in self.lista_reservas:
            if reserva.habitacion.num_habitacion == num_habitacion:
                reserva.habitacion.disponibilidad = True
                self.lista_reservas.remove(reserva)
                return reserva
        return None

    def mostrar_reservas(self):
        if not self.lista_reservas:
            print("No hay reservas realizadas.")
        for reserva in self.lista_reservas:
            print(reserva)


# Crear el hotel y agregar habitaciones
hotel = Hotel()
hotel.agregar_habitacion(Habitacion(101, 2, 30))
hotel.agregar_habitacion(Habitacion(102, 4, 50))
hotel.agregar_habitacion(Habitacion(103, 6, 80))

# Menú principal
while True:
    print("""
    Sistema de Reservas de Hotel:
    1. Consultar disponibilidad
    2. Realizar reserva
    3. Cancelar reserva
    4. Mostrar reservas
    5. Salir
    """)
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        try:
            fecha_check_in = datetime.strptime(input("Fecha de check-in (YYYY-MM-DD): "), "%Y-%m-%d")
            fecha_check_out = datetime.strptime(input("Fecha de check-out (YYYY-MM-DD): "), "%Y-%m-%d")
            capacidad_requerida = int(input("Capacidad deseada: "))

            if fecha_check_in >= fecha_check_out:
                print("Error: La fecha de check-out debe ser posterior a la fecha de check-in.")
                continue

            habitaciones_disponibles = hotel.consultar_disponibilidad(fecha_check_in, fecha_check_out, capacidad_requerida)
            if habitaciones_disponibles:
                print("Habitaciones disponibles:")
                for habitacion in habitaciones_disponibles:
                    print(habitacion)
            else:
                print("No hay habitaciones disponibles.")
        except ValueError:
            print("Error: Formato de fecha o capacidad inválida.")

    elif opcion == "2":
        try:
            numero_habitacion = int(input("Número de habitación: "))
            fecha_check_in = datetime.strptime(input("Fecha de check-in (YYYY-MM-DD): "), "%Y-%m-%d")
            fecha_check_out = datetime.strptime(input("Fecha de check-out (YYYY-MM-DD): "), "%Y-%m-%d")
            nombre_huesped = input("Nombre del huésped: ")

            if fecha_check_in >= fecha_check_out:
                print("Error: La fecha de check-out debe ser posterior a la fecha de check-in.")
                continue

            reserva = hotel.realizar_reserva(numero_habitacion, fecha_check_in, fecha_check_out, nombre_huesped)
            if reserva:
                print("Reserva realizada con éxito:")
                print(reserva)
            else:
                print("Error: No se pudo realizar la reserva. Verifique la habitación y disponibilidad.")
        except ValueError:
            print("Error: Datos ingresados incorrectos.")

    elif opcion == "3":
        try:
            numero_habitacion = int(input("Número de habitación a cancelar: "))
            reserva_cancelada = hotel.cancelar_reserva(numero_habitacion)
            if reserva_cancelada:
                print(f"Reserva cancelada con éxito para la habitación {numero_habitacion}.")
            else:
                print("No se encontró ninguna reserva para esa habitación.")
        except ValueError:
            print("Error: Número de habitación inválido.")

    elif opcion == "4":
        print("Reservas actuales:")
        hotel.mostrar_reservas()

    elif opcion == "5":
        print("¡Gracias por usar el sistema de reservas!")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
