materias=['Progrmacion','Calculo','Estadistica','Macroeconomia','Microeconomia']
print(materias)
for a in materias:
    print('Asignatura:',a)

n= int(input('Introduzca un tamaño de la lista'))
asignaturas=[]
for i in range(n):
    materia=input('Asignatura>>>>>')
    asignaturas.append(materia)
print(asignaturas)

asignaturas.extend(materias)
print(asignaturas)

