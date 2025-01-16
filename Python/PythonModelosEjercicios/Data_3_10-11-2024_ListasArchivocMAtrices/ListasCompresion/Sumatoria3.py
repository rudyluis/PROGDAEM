def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
def sumatoria(n):
    sum=0
    for i in range (1,n+1):
        num=(factorial(i))**2
        den=((2**(n**2)))
        sum+=num/den
        print(f"Para n = {i} = [{num}]/[{den}]\n")
    return sum
n=int(input("Ingrese un término n = "))
val_sum=sumatoria(n)
print("La sumatoria es >>> ",val_sum)