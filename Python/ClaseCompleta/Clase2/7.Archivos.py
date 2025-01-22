"""
Conceptos básicos sobre archivos en Python
Modos de apertura:

'r': Modo lectura. El archivo debe existir; de lo contrario, arrojará un error.
'w': Modo escritura. Si el archivo no existe, lo crea; si ya existe, sobrescribe su contenido.
'a': Modo agregar. Si el archivo no existe, lo crea; si ya existe, agrega contenido al final.
'r+': Modo lectura y escritura. El archivo debe existir.
Contexto (with):

El bloque with open(...) asegura que el archivo se cierre automáticamente después de usarse, incluso si ocurre un error durante la operación.
Funciones comunes:

read(): Lee todo el contenido del archivo como una cadena.
readlines(): Lee el archivo línea por línea y devuelve una lista.
write(): Escribe texto en el archivo.
writelines(): Escribe una lista de líneas en el archivo.
Diferencias entre write y append:

write sobrescribe el contenido existente.
append agrega contenido al final del archivo sin borrar lo anterior.
Archivos binarios:

Además de archivos de texto, Python permite trabajar con archivos binarios (imágenes, videos, etc.) utilizando el modo 'rb' (lectura) o 'wb' (escritura).
Errores comunes:

Intentar leer un archivo inexistente sin manejar la excepción (FileNotFoundError).
Escribir en un archivo abierto en modo lectura.
"""

#%% Crear y leer un archivo
# 1 Basico
# Se utiliza la función `open` para trabajar con archivos.
# El modo `'w'` permite escribir en el archivo, sobrescribiendo cualquier contenido previo.
with open('hola.txt', 'w') as archivo:
    archivo.write('Este es mi primer mensaje')  # Escribe texto en el archivo
print("El archivo se creó exitosamente")

# El modo `'r'` permite leer el contenido de un archivo existente.
with open('hola.txt', 'r') as archivo:
    contenido = archivo.read()  # Lee todo el contenido del archivo
    print(contenido)  # Imprime el contenido del archivo
#%%

#%% Funciones para manejar archivos
# Esta función lee el contenido de un archivo y lo retorna como una cadena de texto.
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:  # Abre el archivo en modo lectura
        contenido = archivo.read()  # Lee el contenido del archivo
    return contenido  # Devuelve el contenido leído

# Esta función sobrescribe el contenido de un archivo con el texto proporcionado.
def escribir_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:  # Abre el archivo en modo escritura
        archivo.write(contenido)  # Escribe el contenido en el archivo

# Esta función agrega contenido al final de un archivo existente.
def escribir_archivo_continuo(nombre_archivo, contenido):
    with open(nombre_archivo, 'a') as archivo:  # Abre el archivo en modo agregar
        archivo.write(contenido + '\n')  # Escribe contenido seguido de un salto de línea
#%%

#%% Interactuar con el usuario para editar un archivo
##2
import funciones as f  # Importa las funciones definidas previamente
archivo = input('Introduzca el nombre del archivo con formato txt: ')  # Solicita el nombre del archivo
print('Cuando presione la tecla [S] se saldrá de la edición')  # Indica cómo salir del bucle

sw = True
while sw:  # Ciclo para agregar contenido al archivo
    contenido = input('>>>>> ')  # Solicita texto al usuario
    f.escribir_archivo_continuo(archivo, contenido)  # Agrega el contenido al archivo
    if contenido == 'S':  # Condición para salir del bucle
        sw = False  # Cambia la bandera para salir del ciclo
        break
#%%

#%% Generar y guardar una tabla de multiplicar en un archivo
import funciones as f
# 3
# Función para generar la tabla de multiplicar de un número y guardarla en un archivo
def generar_tabla_multiplicar():
    n = int(input('Introduzca un valor entre 1 y 10: '))  # Solicita un número al usuario
    tabla = ''  # Variable para almacenar la tabla de multiplicar

    # Genera la tabla de multiplicar utilizando un bucle
    for i in range(1, 11):
        resultado = n * i
        fila = f"{n} x {i} = {resultado}\n"  # Formatea cada línea de la tabla
        tabla += fila  # Agrega la línea a la tabla completa

    # Define el nombre del archivo dinámicamente
    nombre_archivo = f"tabla-{n}.txt"
    f.escribir_archivo(nombre_archivo, tabla)  # Guarda la tabla en el archivo
    print(f"La tabla de multiplicar del {n} se guardó en el archivo {nombre_archivo}")
    return nombre_archivo  # Devuelve el nombre del archivo generado

# Llama a la función para generar la tabla y guarda el archivo
archivo = generar_tabla_multiplicar()
# Lee el contenido del archivo generado
contenido = f.leer_archivo(archivo)
# Muestra la tabla en pantalla
print(contenido)
#%%
