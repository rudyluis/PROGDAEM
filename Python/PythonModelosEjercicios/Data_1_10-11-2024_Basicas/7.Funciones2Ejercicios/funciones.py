import random
def primo(n):
    sw=0
    es_primo=False
    for _ in range (1,n+1):
        if n % _==0:
            sw+=1
    if(sw==2):
        es_primo=True 
    else:
        es_primo=False
    return es_primo

def capicuav2(n):
    numero=n
    numero_str=str(n)   ### vovlerlo una cadena
    numero_str=numero_str[::-1]   ## con esta indtruccion lo damos la vuelta edge
    print('El valor inverso >>>>'+numero_str)
    if(int(numero_str)==numero):
        return True
    else:
        return False

def juegodado():
    valor_dado= random.randrange(1,7)
    opcion_j=0
    cont=1
    while(opcion_j!=valor_dado):
        opcion_j=int(input('Introduzca el valor del dado a adivinar>>>>'))
        if(opcion_j==valor_dado):
            print('GANASTE  :)')
            print('En el intento #'+str(cont))
            break
        else:
            cont+=1
            print("Te equivocaste")
            pregunta=input('Desea continuar en el juego [s] o [n]')
            if(pregunta=='n'):
                print("No lo lograste :( el numero era >>>"+str(valor_dado))
                break    

def serie_simple(n):
    for _  in range(1,n+1):
        print( _ ,end=' ')

def serie_doble(n):
    for _ in range(1,n+1):
        ser=''
        for _ in range(1, _ +1):
            ser=ser+str(_)
        print(ser, end=' ')

def serie_doble2(n):
    for i in range(1,n+1):
        ser=''
        for j in range(1, i+1):
            ser=ser+str(i)
        print(ser, end=' ')

def serie_inversa(n):
    for i in range(n,0,-1):
        print(inversa(2**i), end='  ')

def inversa(n):
    n=str(n)
    return(int(n[::-1]))


def serie_doble_modificada (n):
    ser=''
    for _ in range(1,n+1):
        ser=ser+str(_)
    return int(ser)
        
def serie_progresiva(n):
    for i in range(1,n+1):
        vs=serie_doble_modificada(i)
        numero=str(vs)+str(inversa(vs))
        print(numero, end="   ")

def serie_rara(n,a=1,b=1):
    c=a+b
    print(a,end=" ")
    print(b,end=" ")
    print(c,end=" ")
    for i in range (1,n+1):
        if(c % 2==0):
            valor=a+b+c
        else:
            valor=b+c
       ## a=b
       ## b=c
       ## c=valor
        a,b,c=b,c,valor
        print(valor, end=" ")
def paresImpares(n,sem1=1, sem2=2, inicio=1):
    dato=inicio*sem1
    print(dato, end=" ")
    for _ in range(1,n+1):
        if(_ % 2==0):
            dato*=sem1
            print(dato, end=" ")
        else:
            dato*=sem2
            print(dato*-1,end=" ")

def serie_3 (n, sem1=1, sem2=2, inicio=1):
    print(inicio, end=" ")
    for i in range(2,n+1):
        valor=sem1*inicio+sem2
        inicio+=valor
        print(inicio, end=" ")
        
    


def fibonacci_inversa(n,a,b):
    print(a,end=' ')
    ##print(b,end=' ')
    while n>0 and a>=0:
        ##s=a-b
        ##a=s
        ##b=a
        ##a,b=a-b,a
        a,b=b,a-b
        n-=1
        print(a, end=" ")

def serie_paso(n,semilla,valor):
    print(semilla, end=" ")
    for _ in range (1,n+1):
        if(_ %2==0):
            
            semilla*=valor
        else:
            semilla+=valor
        print(semilla,end=" ")
    
def serieTerminoGeneral(n):
    sumatoria=0
    for i in range (1,n+1):
        an= i*(i+1)/(i**2+2*i)
        print(f'{an}={i}({i}+1)/{i}^2+2{i}', end="\n")
        sumatoria+=an
    print(sumatoria,end=" ")

def conway(n):
    serien='1'
    print(serien,end="\n")
    for i in range (1,n+1):
        s= serien+'#'
        cont=1
        numero=''
        for j in range(1,len(s)):  ### len sirve para mostrar los cant de carcteres
            if(s[j]!=s[j-1]):
                numero+=(str(cont))+s[j-1]
                cont=1
            else:
                cont+=1
        print(numero, end="\n")
        serien=numero
    

                





    