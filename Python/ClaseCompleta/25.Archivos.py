#%%
with open('hola.txt','w') as archivo:
    archivo.write('Este es mi primer mensaje')
print("El archivo se creo exitosamente")

with open('hola.txt','r') as archivo:
    contenido=archivo.read()
    print(contenido)
#%%
#%% Escribir en un archivo funciones
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

#%%
import funciones as f
archivo= input('Introduzca el nombre del archivo con formato txt')
print('Cuando presion la tecla [S] se saldra de la edicion')
sw=True
while (sw):
    contenido=input('>>>>>')
    f.escribir_archivo_continuo(archivo,contenido)
    if(contenido=='S'):
        sw=False
        break
    
#%%
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
# %%
