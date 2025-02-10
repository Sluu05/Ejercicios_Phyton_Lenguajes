def agrup_por_ciudad(data):
    resumen_ventas = {}
    for ciudad, venta in zip(data['Ciudad'], data['Ventas']):
        if ciudad in resumen_ventas:
            resumen_ventas[ciudad] += venta
        else:
            resumen_ventas[ciudad] = venta
    return resumen_ventas

data = {
    'Ciudad': ['Nueva York', 'Los Angeles', 'Nueva York', 'Chicago'],
    'Ventas': [100, 150, 200, 50]
}

resultado = agrup_por_ciudad(data)
print("Ventas por ciudad: ", resultado)