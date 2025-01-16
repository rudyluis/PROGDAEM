def factorial_recursivo(n):
    if(n==0):
        return 1
    else:
        return n*factorial_recursivo(n-1)
### Main principal
if __name__=="__main__":
    n=int(input("Ingrese la cantidad de términos para el factorial : n = "))
    resultado=factorial_recursivo(n)
    print("El factorial de ", n, " es:", resultado)