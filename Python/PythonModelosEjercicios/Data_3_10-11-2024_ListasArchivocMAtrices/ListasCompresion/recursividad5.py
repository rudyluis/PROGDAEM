def numero_motzkin(n):
    if n<0:
        return []
    motzkin=[1]
    if(n==0):
        return motzkin
    motzkin.append(1)
    if(n==1):
        return motzkin
    for i in range(2,n):
        nuevo_numero=((2*i+1)*motzkin[-1]+(3*i-3)*motzkin[-2])//(i+2)
        motzkin.append(nuevo_numero)
    return motzkin

n= int(input('n>>>>'))
resultado=numero_motzkin(n)
print(resultado)
