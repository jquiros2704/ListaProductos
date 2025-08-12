listaProductos=[]

def agregarProducto():
    while True:
        nombre = input("¿Cuál producto desea agregar?: ").strip().lower()
        if not nombre:
            print("⚠ Ingrese un nombre válido.")
            continue

        # Verificar si el producto ya existe
        for producto in listaProductos:
            if producto["nombre"] == nombre:
                print(f"⚠ '{nombre}' ya está en la lista con cantidad {producto['cantidad']}.")
                resp = input("¿Desea cambiar la cantidad? (s/n): ").strip().lower()
                if resp in ("s", "y"):
                    nueva_cantidad = input("Ingrese la nueva cantidad: ").strip()
                    if nueva_cantidad.isdigit():
                        producto["cantidad"] = int(nueva_cantidad)
                        print(f"✅ Cantidad actualizada para '{nombre}'.")
                    else:
                        print("⚠ Cantidad inválida.")
                break
        else:
            cantidad = input("Ingrese la cantidad: ").strip()
            if cantidad.isdigit():
                listaProductos.append({"nombre": nombre, "cantidad": int(cantidad)})
                print(f"✅ '{nombre}' agregado con cantidad {cantidad}.")
            else:
                print("⚠ Cantidad inválida.")
        
        resp = input("¿Desea agregar otro producto? (s/n): ").strip().lower()
        if resp not in ("s", "y"):
            break
    

def eliminarProducto():
    if not listaProductos:
        print("🪣 No hay productos para eliminar.")
        return

    nombre = input("¿Cuál producto desea eliminar?: ").strip().lower()

    # Buscar por nombre y eliminar la primera coincidencia
    idx = next((i for i, p in enumerate(listaProductos) if p["nombre"] == nombre), None)
    if idx is not None:
        eliminado = listaProductos.pop(idx)
        print(f"🗑 Se eliminó '{eliminado['nombre']}' (cantidad: {eliminado['cantidad']}).")
    else:
        print(f"❌ '{nombre}' no está en la lista.")

def mostrarProductos():
    if not listaProductos:
        print("🪣 La lista está vacía.")
    else:
        print("\n📝 Lista de compras:")
        for producto in listaProductos:
            print(f"- {producto['nombre']} (Cantidad: {producto['cantidad']})")


def productoestaenlista(lista):
    nombre = input("¿Qué producto desea buscar?: ").strip().lower()
    if not nombre:
        print("⚠ Ingrese un nombre válido.")
        return

    prod = next((p for p in lista if p["nombre"] == nombre), None)
    if prod:
        print(f"✅ '{prod['nombre']}' está en la lista (cantidad: {prod['cantidad']}).")
    else:
        print(f"❌ '{nombre}' no está en la lista.")


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