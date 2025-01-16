#%%
def convertir_a_entero(cadena):
    try:
        return int(cadena)
    except ValueError:
        return "Error: no se puede convertir a entero"

# Prueba la función
print(convertir_a_entero("123"))  # Salida esperada: 123
print(convertir_a_entero("abc"))  # Salida esperada: Error: no se puede convertir a entero

#%%
def obtener_elemento(lista, indice):
    try:
        return lista[indice]
    except TypeError:
        return "Error: el índice debe ser un número entero"
    except IndexError:
        return "Error: índice fuera de rango"

# Prueba la función
mi_lista = [10, 20, 30]
print(obtener_elemento(mi_lista, 1))  # Salida esperada: 20
print(obtener_elemento(mi_lista, "a"))  # Salida esperada: Error: el índice debe ser un número entero
print(obtener_elemento(mi_lista, 5))  # Salida esperada: Error: índice fuera de rango

# %%
