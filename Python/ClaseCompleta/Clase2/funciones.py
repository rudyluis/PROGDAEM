def leer_archivo(nombre_archivo):
    with open(nombre_archivo,'r') as archivo:
        contenido=archivo.read()
    return contenido

def escribir_archivo(nombre_archivo,contenido):
    with open(nombre_archivo,'w') as archivo:
        archivo.write(contenido)

def escribir_archivo_continuo(nombre_archivo,contenido):
    with open(nombre_archivo,'a') as archivo:
        archivo.write(contenido+'\n')

