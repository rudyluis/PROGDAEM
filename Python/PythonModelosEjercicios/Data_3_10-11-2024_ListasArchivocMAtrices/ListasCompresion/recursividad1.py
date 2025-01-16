def suma_recursiva(n):
    if n==1:
        return 1
    else:
        return n+suma_recursiva(n-1)
if __name__=="__main__":
    n=int(input("Ingrese la cantidad de términos para la suma: n = "))
    resultado=suma_recursiva(n)
    print("La suma de los primeros", n, "números es:", resultado)