import random
import os
def llenarMatriz(filas,columnas):
    matriz=[[random.randint(1,10) for c in range(columnas)] for f in range (filas)]
    return matriz

def guardarMatriz(matriz, nombre_archivo):
    with open (nombre_archivo,'w') as archivo:
        for fila in matriz:
            linea= ' '.join(map(str,fila))
            archivo.write(linea+"\n")
        print('se ha guardado los registro en el archivo correctamente')

def leer_matriz(nombre_archivo):
    try:
        matriz=[]
        with open(nombre_archivo,'r') as archivo:
            for fila in archivo:
                fila= list(map(int,fila.strip().split()))
                matriz.append(fila)
    except IOError:
        print("Error no existe el archivo ")
    return matriz
def eliminarArchivo(nom_archivo):
    if( os.path.exists(nom_archivo)):
        os.remove(nom_archivo)
    else:
        print(f"El archivo>>> {nom_archivo} no existe")

def copiar_archivo(origen,destino):
    with open(origen,'r') as archivo_origen:
        contenido=archivo_origen.read()
    with open(destino,'w') as archivo_destino:
        archivo_destino.write(contenido)
    print("El archivo se copiado correctamente")



sele= input('Desea generar una matriz [R] \n o leer una existente [L] \n'
            + "o eliminar un archivo existente [E] \n"
            + "o copiar un archivo con todo su contenido [C]"
            )
if(sele=='L'):
    nom_archivo=input('Introduzca el nombre del archivo existente [txt]')  
    matriz=leer_matriz(nom_archivo)  
    for fila in matriz:
        print(fila)
elif(sele=='R'):
    filas = int(input('Filas>>>>'))
    columnas = int(input('Columnas>>>>'))
    matriz= llenarMatriz(filas,columnas)
    nom_archivo=input('Introduzca un nombre del archivo a guardar [txt]')
    guardarMatriz(matriz,nom_archivo)
elif(sele=='E'):
    nom_archivo=input('Introduzca el nombre del archivo a eliminar [txt]')
    eliminarArchivo(nom_archivo)
else:
    nom_archivo_origen=input('Introduzca el nombre del archivo a copiar')
    nom_archivo_destino=input('Introduzca el nombre del archivo destino')
    copiar_archivo(nom_archivo_origen,nom_archivo_destino)
