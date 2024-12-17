import os

index_global = 4

lista_de_productos = {1:{"nombre":"Coca Cola","precio":3000, "stock":40, "categoria":"gaseosa"},
                      2:{"nombre":"Heineken","precio":1800, "stock":20, "categoria":"cerveza"},
                      3:{"nombre":"villavicencio","precio":900, "stock":35, "categoria":"agua"},
                      4:{"nombre":"Stella Artois","precio":2100, "stock":9, "categoria":"cerveza"}}


def registrar_producto(datos_producto):
    # Registra el producto en la lista.
    lista_de_productos.update({index_global+1:datos_producto})
    os.system("cls")
   

def mostrar_productos():
    # Muestra todos los productos de la lista.
    os.system("cls")
    print("<----- Lista de Productos ------>")
    print(f"INDEX      |       Datos")
    for key in lista_de_productos:        
        print(f"{key}: {lista_de_productos[key]}")
    input("")


def actualizar_producto(key_producto):
    # Muestra la lista de todos los productos, selecciona uno y lo modifica.
    if key_producto in lista_de_productos:
        print(f"Seleccionaste el producto:{lista_de_productos[key_producto]}")
        nombre = input("Ingrese el nuevo nombre: ")
        precio = int(input("Ingrese el nuevo precio: $"))
        stock = int(input("Ingrese el nuevo stock: "))
        categoria = input("Ingrese la nueva categoria: ")
        lista_de_productos[key_producto] = {"nombre":nombre,"precio":precio,"stock":stock,"categoria":categoria}

    else:
        print(f"\n-----> Producto no encontrado")
        print("")
        input()


def buscar_producto(index):
    # Busca un producto especifico y lo muestra.
    if index in lista_de_productos:
        print(f'''
                Datos del producto:
                
                Nombre:{lista_de_productos[index]["nombre"]}
                Precio:{lista_de_productos[index]["precio"]}
                Stock:{lista_de_productos[index]["stock"]}
                Categoria:{lista_de_productos[index]["categoria"]}
                ''')
        input()
    else:
        print(f"\n-----> Producto no encontrado")
        print("")
        input()


def eliminar_producto( index ):
    # Elimina un producto especifico
    if index in lista_de_productos:
        print(f"Producto Eliminado: {lista_de_productos.pop(index)}")
        input()
    else:
        print(f"Producto no encontrado")
        input()


def reporte_bajo_stock( limite ):
    # Busca productos con stock determinado por el usuario, o menor.
    os.system("cls")
    print(f"Producto con stock menor o igual a: {limite}")
    for producto in lista_de_productos.values():
        if producto["stock"] <= limite:
            print(producto)
    input()


# Menu
opcion = ""

while opcion != "7":
    print("\n----- Sistema Stock de Bebidas -----")
    print("")
    opcion = input(f'''Ingrese la opcion: 
                        1) Agregar producto 
                        2) Mostrar lista de productos 
                        3) Eliminar Producto 
                        4) Actualizar un Producto
                        5) Buscas un producto por id
                        6) Alerta Stock
                        7) Salir
                        
                        Ingrese su opcion: ''')

    if opcion == "1":
        nombre = input("Ingrese el  nombre: ")
        precio = int(input("Ingrese el precio: "))        
        stock = int(input("Ingrese el stock: "))
        categoria = input("Ingrese la categoria: ")
        if precio > 0 and stock > 0:
            datos_producto = {"nombre":nombre,"precio":precio,"stock":stock,"categoria":categoria}
            registrar_producto(datos_producto)
            index_global = index_global + 1
        else:
            print("\n-----> DATOS INCORRECTOS")
            print("")
    
    elif opcion == "2":
        mostrar_productos()
    
    elif opcion == "3":
        mostrar_productos()
        ingreso_usuario = int(input("Ingrese el id del producto que desea eliminar: "))
        eliminar_producto(ingreso_usuario)
    
    elif opcion == "4":
        mostrar_productos()
        ingreso_usuario = int(input("Ingrese el id del producto que desea actualizar: "))
        actualizar_producto(ingreso_usuario)
    
    elif opcion == "5":
        ingreso_usuario = int(input("Ingrese el id del producto que desea buscar: "))
        buscar_producto(ingreso_usuario)
    
    elif opcion == "6":
        ingreso_usuario = int(input("Ingrese el limite de stock a consultar: "))
        reporte_bajo_stock(ingreso_usuario)
    
    elif opcion == "7":
        print("\nGracias por usar el sistema")
        print("")
    
    else:
        print("\n-----> OPCION NO ENCONTRADA")
        print("")