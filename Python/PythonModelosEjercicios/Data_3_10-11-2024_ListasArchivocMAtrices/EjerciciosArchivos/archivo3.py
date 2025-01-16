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
    
