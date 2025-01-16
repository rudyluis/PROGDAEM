n=int(input("Introduzca un numero -->"))
a=[]
## serializar
for i in range(n):
    a.append(0)
print(a)

for i in range(n):
    a[i]=i+1
print(a)