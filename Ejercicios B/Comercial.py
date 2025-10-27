# Eres un comercial trabajando para una compañía que vende diversos productos. Quieres crear un
# programa para realizar un seguimiento de los productos que has vendido y el valor total de las
# ventas. Supongamos que hay un total de 10 productos.
# Tú has vendido 5 de estos productos en las siguientes cantidades:
# Producto 1: 3 unidades
# Producto 2: 1 unidad
# Producto 5: 7 unidades
# Producto 6: 2 unidades
# Producto 9 : 4 unidades
# Los precios de cada uno de estos productos son como siguen:
# Producto 1: 30.0 EU	 	 Producto 6: 44.0 EU
# Producto 2: 9.8 EU	 	 Producto 7: 21.2 EU
# Producto 3: 42.5 EU	 	 Producto 8: 53.2 EU
# Producto 4: 32.6 EU	 	 Producto 9: 25.3 EU
# Producto 5: 71.5 EU	 	 Producto 10: 57.8 EU
# Crea un script que dada una lista con los productos, sus precios y las unidades vendidas, imprima
# la cantidad total de ventas, el dinero facturado por producto y el dinero total. 

# Lista de cada uno de los productos[(Numero de unidades, Precio del producto)]
Cantidad_Productos = [3,1,0,0,7,2,0,0,4,0]
Productos_Precio = [30.00,9.80,42.50,32.60,71.50,44.00,21.20,53.20,25.30,57.80]
Cantidad_Total = []

# Bucle para la cantidad total de ventas
for ventas in range(len(Productos_Precio)):
    Total_Producto = Cantidad_Productos[ventas] * Productos_Precio[ventas] 
    Cantidad_Total.append(Total_Producto)

# Variable del dinero total y la facturación del dinero
Dinero_Total = sum(Cantidad_Total)

# Recorremos un bucle para calcular El dinero facturado por producto y el dinero total de cada producto
for i in range(len(Productos_Precio)):
    if Cantidad_Productos[i] > 0:
        print(f"Producto {i+1}: {Cantidad_Productos[i]} unidades x {Productos_Precio[i]}€ = {Cantidad_Total[i]:.2f}€")

print(f"TOTAL FACTURADO: {Dinero_Total:.2f}€")