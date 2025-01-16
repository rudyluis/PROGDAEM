def primo(n):
    cont=0
    sw=0
    while(cont<n):
        cont+=1
        if(n%cont==0):
            sw+=1
    if(sw==2):
        return True
    else:
        return False

def sophie(n):
    sophie=[]
    cont=2
    while (len(sophie)<n):
            if primo(cont)==True and primo((2*cont)+1)==True:
                sophie.append(cont)
            cont+=1
    return sophie

if __name__=="__main__":
    n=int(input("Ingrese la cantidad de números para la serie Sophie Germain: n = "))
    print("La serie Sophie Germain es: ",sophie(n))

