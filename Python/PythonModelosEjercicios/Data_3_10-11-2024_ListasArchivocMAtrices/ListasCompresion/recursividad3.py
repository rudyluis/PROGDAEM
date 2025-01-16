def fib(n):
    if n == 0:
        return 0
    if n == 1:
        print(n)
    return fib(n-1) + fib(n-2)

def fibonacci2(n, current_term=0, next_term=1, count=0):
    if count <= n:
        print(current_term)  # Muestra el término actual
        return fibonacci2(n, next_term, current_term + next_term, count + 1)
    
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_sequence = [0, 1]  # Inicializa la secuencia con los primeros dos términos.
        for i in range(2, n + 1):
            next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
            fib_sequence.append(next_term)
        return fib_sequence

if __name__ == '__main__':
    fibonacci = fibonacci2(int(input("ingrese un numero")))
    print('Fibonacci de orden n :')
    print(fibonacci)
    