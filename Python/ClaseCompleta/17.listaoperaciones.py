n= int(input('introduzca una cantidad de notas'))
notas=[]
for indice in range(1,n+1):
    nota=int(input(f"Introduzca la nota {indice}: "))
    notas.append(nota)

print(notas)
for nota in notas:
    print(nota," ", end="")

promedio_notas=sum(notas)/len(notas)
print("Promedio de Notas: ", promedio_notas)
print("La nota maxima:",max(notas) )
print("La nota minima:", min(notas))

notas.sort()
for nota in notas:
    print(nota," ", end="")