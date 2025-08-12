listaProductos=[]

def agregarProducto():
    while True:
        producto = input("¿Cuál producto desea agregar para comprar?: ").strip().lower()
        if not producto:
            print("⚠ Ingrese un nombre válido.")
            continue

        if producto in listaProductos:
            print(f"⚠ '{producto}' ya está en la lista.")
            resp = input("¿Desea intentar con otro producto? (s/n): ").strip().lower()
            if resp not in ("s", "y"):  # acepta 's' (sí) o 'y' (yes)
                break
            continue  # vuelve a pedir otro producto

        listaProductos.append(producto)
        print(f"✅ '{producto}' fue agregado a la lista.")
        resp = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
        if resp not in ("s", "y"):
            break



    

def eliminarProducto():
    if not listaProductos:
        print("🪣 No hay productos para eliminar.")
        return
    mostrarProductos()
    producto = input("¿Cuál producto desea eliminar?: ").strip().lower()
    if producto in listaProductos:
        listaProductos.remove(producto)
        print(f"🗑 '{producto}' ha sido eliminado")
    else:
        print(f"❌ '{producto}' no está en la lista")

def mostrarProductos():
    if not listaProductos:
        print("🪣 La lista está vacía.")
    else:
        for producto in listaProductos:
            print(producto)


def productoestaenlista(lista):
    producto=input('Que producto desea buscar').strip().lower()
    if producto in lista:
        print('Si esta')
    else:
        print('no esta')


def menu():
        while True:

            opcion=input('Bienvenido a tu lista de productos a comprar\n'
            'Que deseas hacer?\n' \
            '1.Agregar Producto\n'
            '2.Eliminar Producto\n' \
            '3. Buscar Producto\n' \
            '4. Mostrar lista\n' \
            '5. Salir')

            if opcion == "1":
                agregarProducto()
            elif opcion =='2':
                eliminarProducto()
            elif opcion == '3':
                productoestaenlista(listaProductos)
            elif opcion== '4':
                mostrarProductos()
            else:
                print('Hasta pronto 👋') 
                break

menu()