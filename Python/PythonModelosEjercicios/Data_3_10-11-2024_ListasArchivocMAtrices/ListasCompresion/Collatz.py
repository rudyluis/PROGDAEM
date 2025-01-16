
def collatz(n):
    collatz=[n]
    while (n>1):
        if n%2==0:
            n//=2   
        else:
            n=(3*n)+1
        collatz.append(n)   
    return collatz

if __name__ == "__main__":
    n=int(input("Ingrese un valor n = "))
    print("La serie collatz es: ",collatz(n))