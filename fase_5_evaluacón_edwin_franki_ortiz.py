#edwin franki otiz muñoz
#grupo: 213022_697
#programa: ingenieria de sistemas, fundamentos de programacion.
#ejercicio fase 5 evaluación final POA.

#Hacer la matriz con los datos.
matriz=[
    {"codigo articulo": "001","nombre": "parlante JBL", "stock actual": "20", "stock minimo": "10"},
    {"codigo articulo": "002","nombre": "smartphone Sansung", "stock actual": "15", "stock minimo": "10"},
    {"codigo articulo": "003","nombre": "auriculares Sony", "stock actual": "2", "stock minimo": "10"},
    {"codigo articulo": "004","nombre": "tablet Lg", "stock actual": "0", "stock minimo": "10"},
    {"codigo articulo": "005", "nombre": "smartwatch Huawei", "stock actual": "4", "stock minimo": "10"},
    {"codigo articulo": "006","nombre": "cargador generico", "stock actual": "10", "stock minimo": "10"},
    ]

#calcular si el stock actual es menor al stock minimo
#funcion para determinar la cantidad a pedir.
def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    elif stock_actual >= stock_minimo:
        return 0
    
#salida: imprimir lista de pedidos
def imprimir_lista_pedidos(matriz):
    print("Lista de pedidos:")
    print()
    for articulo in matriz:
        codigo = articulo["codigo articulo"]
        nombre = articulo["nombre"]
        stock_actual = int(articulo["stock actual"])
        stock_minimo = int(articulo["stock minimo"])
        
        cantidad_a_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        if cantidad_a_pedir > 0:
            print(f"Nombre: {nombre}. Cantidad a pedir: {cantidad_a_pedir}.")

imprimir_lista_pedidos(matriz)
print()