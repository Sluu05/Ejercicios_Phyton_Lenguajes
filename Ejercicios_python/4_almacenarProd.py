def almacenar_producto():
    productos = {}
    while True:
        nombre = input("Ingrese el nombre del producto (o 'salir' paea terminar): ")
        if nombre.lower() == 'salir':
            break
        precio = float(input("Ingrese el precio del producto: "))
        productos [nombre] = precio
    return productos

productos = almacenar_producto()
print("Lista de productos y precios: ", productos)