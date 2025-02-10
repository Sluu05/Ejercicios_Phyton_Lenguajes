def fibonacci(n):
    fib_secuencia = [0, 1]
    for _ in range (2, n):
        fib_secuencia.append(fib_secuencia[-1] + fib_secuencia[-2])
    return fib_secuencia

n = 15
resultado = fibonacci(n)
print ("Los primeros 15 numeros de la suseción de Fibonacci son: ", resultado)    