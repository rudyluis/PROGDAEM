num=int(input('Introduzca un valor>>>>'))
sumanotas=0
aprobados=0
reprobados=0
for i in range(1,num+1,1):
    notas= int(input('Introduzca la nota #'+str(i)+" >>>>"))
    sumanotas= sumanotas+notas
    if(notas>=51):
        aprobados+=1
    else:
        reprobados+=1
    #### pregunta
    opcion=input('Desea continuar introduciendo notas?? [S] o [N]')
    if(opcion=='N'):
        cantidad=i
        promedio_parcial= sumanotas/cantidad
        print('El promedio parcial de notas es: '+str(promedio_parcial))
        break    
promedio= sumanotas/num
print('El promedio del curso es ',str(promedio))
print('la cantidad de aprobados es',str(aprobados))
print('la cantidad de reprobados es',str(reprobados))

