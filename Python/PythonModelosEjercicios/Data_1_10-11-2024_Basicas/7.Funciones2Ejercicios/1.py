###### programa principal
from funciones import primo  
n= int(input('>>>>'))
i=0
cont=2
while i<n:
    if(primo(cont)):
        print(cont,end=" ")
        i+=1
    cont+=1