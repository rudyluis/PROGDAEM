import funciones as f
def generar_tabla_multiplicarampliada():
    n=int(input('Introduzca un valor entre 1 y 10'))
    tabla=''
    for j in range (1,n+1):
        for i in range(1,11):
            resultado= j*i
            fila=f"{j} x {i} = {resultado}\n"
            tabla+=fila
        tabla+='-------------------\n'
    nombre_archivo= f"tabla_multiplicar-{n}.txt"
    f.escribir_archivo(nombre_archivo,tabla)
    print(f"La tabla de multiplicar del {n} se guardo en el archivo {nombre_archivo}")
    return nombre_archivo

archivo=generar_tabla_multiplicarampliada()
contenido=f.leer_archivo(archivo)
print(contenido)