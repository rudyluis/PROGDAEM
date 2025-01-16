lista=[4,5,6]
Matriz=[
    [2,5,6],
    [3,4,7],
    [2,8,9]
]
print(Matriz)
print(Matriz[1][1])
print(Matriz[2][2])
Matriz2=[]
lista1=[6,3,4]
lista2=[3,5,6]
lista3=[0,7,1]
Matriz2.append(lista1)
Matriz2.append(lista2)
Matriz2.append(lista3)
print(Matriz2)

n=3
m=4
Matriz3=[]
for i in range (n):
    fila=[]
    for j in range (m):
        valor = int(input(f'Introduzca un valor en la posicion {i} {j}:'))
        fila.append(valor)
    Matriz3.append(fila)

for fila in Matriz3:
    print(fila)

