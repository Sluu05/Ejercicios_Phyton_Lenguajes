def suma_lista(numero):
    total = 0
    for num in numero:
        total += num
    return total

lita = [12, 10, 8, 5]
resultado = suma_lista(lita)
print("La suma es: ", resultado)