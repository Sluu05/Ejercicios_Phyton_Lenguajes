def elementos_unicos (lista):
    return list(set(lista))

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = elementos_unicos(lista)
print("Lista con elementos únicos: ", resultado)