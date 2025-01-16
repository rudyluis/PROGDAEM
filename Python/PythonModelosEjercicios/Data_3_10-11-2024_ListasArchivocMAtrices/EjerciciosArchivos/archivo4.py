import funciones as f
def generar_tabla_multiplicar():
    n=int(input('Introduzca un valor entre 1 y 10'))
    tabla=''
    for i in range(1,11):
        resultado= n*i
        fila=f"{n} x {i} = {resultado}\n"
        tabla+=fila
    
    nombre_archivo= f"tabla-{n}.txt"
    f.escribir_archivo(nombre_archivo,tabla)
    print(f"La tabla de multiplicar del {n} se guardo en el archivo {nombre_archivo}")
    return nombre_archivo

archivo=generar_tabla_multiplicar()
contenido=f.leer_archivo(archivo)
print(contenido)
