n=int(input("Ingrese el tamaño de la lista: "))
vector=[]
for i in range(n,0,-1):
    if i%2==0:
        vector.append(i)
    else:
        vector.insert(0, i)
print("El vector es: ",vector)