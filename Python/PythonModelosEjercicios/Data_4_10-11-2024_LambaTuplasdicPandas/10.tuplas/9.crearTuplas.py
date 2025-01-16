def crear_tuplas():
    """Crea una lista de tuplas a partir de valores ingresados por el usuario."""
    lista_tuplas = []
    print("Introduce pares de valores para crear tuplas (escribe 'salir' para terminar):")
    
    while True:
        valor1 = input("Introduce el primer valor (o escribe 'salir' para finalizar): ")
        if valor1.lower() == 'salir':
            break
        valor2 = input("Introduce el segundo valor: ")
        # Crear tupla y añadir a la lista
        tupla = (valor1, valor2)
        lista_tuplas.append(tupla)
    
    return lista_tuplas

# Uso de la función
tuplas = crear_tuplas()
print("Tu lista de tuplas es:", tuplas)
