def agregarNotas():
    notas = []
    asignaturas=[]
    while True:
        try:
            asignatura= input('Nombre Asignatura:')
            asignaturas.append(asignatura)
            nota = float(input("Ingrese una nota: "))
            notas.append(nota)  ### agrega un valor a la lista
        except ValueError:
            print ('Error: Introduzca un valor numerico')
        continuar = input("¿Desea ingresar otra nota? (si/no): ").lower()
        if continuar != "si":
            break

    if len(notas) > 0:
        nota_maxima = max(notas)
        nota_minima = min(notas)
        promedio    = sum(notas)/len(notas)
        
        return notas,asignaturas,nota_maxima,nota_minima,promedio
    else:
        print("No se ingresaron notas.")
### main principal
notas,asignaturas,nota_maxima,nota_minima,promedio=agregarNotas()
##print("Notas ingresadas:", notas)
for nota,asignatura in zip(notas,asignaturas):
    print(f"Asignatura:{asignatura}--->Calificación: {nota}")
print("Resultados")
print("==========")
print("Nota máxima:", nota_maxima)
print("Nota mínima:", nota_minima)
print("Promedio:", promedio)