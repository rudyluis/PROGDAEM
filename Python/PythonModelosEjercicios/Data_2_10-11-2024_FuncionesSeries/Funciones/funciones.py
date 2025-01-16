def suma(x,y):
    z=x+y
    return z
 
 
def escribirNombre(nombre, cantidad):
    for a in range(0,cantidad):
        print(nombre)

def factorial(numero):
    c=1
    for a in range(1,numero+1):
        c*=a
    return c
def sumatoria(numero):
    c=0
    for a in range(1,numero+1):
        c+=a
    return c
def dec_bin(num):
    valor=''
    while (num!=0):
        dig=num %16
        num=num //16
        dig=str(dig)
        match dig:
            case '10': dig='A'
            case '11': dig='B'
            case '12': dig='C'
            case '13': dig='D'
            case '14': dig='E'
            case '15': dig='F'
        valor=dig+valor
    return(valor)

def bin_to_decimal(num):
    conta=0
    decimal=0
    for dig in range (len(num)-1,-1,-1):
        decimal=decimal+int(num[dig])*2**conta
        conta+=1
    return decimal