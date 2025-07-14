from database.connection import get_connection
import os
import time

def ver_pedidos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM orders")
    pedidos = cursor.fetchall()
    if not pedidos:
        print("\nAun no hay pedidos registrados por clientes")
    else:
        for pedido in pedidos:
            print(pedido)
    cursor.close() 
    conn.close()
    input("\nPresione enter para continuar")

def ver_inventario():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM inventory")
    inventario = cursor.fetchall()
    if not inventario:
        print("\nEl inventario esta vacio")
    else:
        print("\nID\tCantidad\tFecha Actualización")
        print("-" * 50)
        for item in inventario:
            id_producto = item[0]
            cantidad = item[1]
            fecha = item[2]
            print(f"{id_producto}\t{cantidad}\t\t{fecha}")
    cursor.close() 
    conn.close()
    input("\nPresione enter para continuar")


def ajustar_stock():
    conn = get_connection()
    cursor = conn.cursor()
    on = True
    while on:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')

            entrada = input("Ingrese el ID del producto que desea actualizar (o '*' para salir):\n")
            if entrada == '*':
                print("❌ Operación cancelada. Volviendo a menú anterior.")
                time.sleep(2)
                on = False
            else:
                id_product = int(entrada)
                cursor.execute(
                    "SELECT product_id, product_name, product_description, product_price, category_id FROM products WHERE product_id = %s",
                    (id_product,)
                )
                producto_actual = cursor.fetchone()

                if not producto_actual:
                    print("\n❌ Producto no encontrado con ese ID")
                    time.sleep(2)
                else:
                    print("\n📦 Producto encontrado:")
                    print(f"ID: {producto_actual[0]}")
                    print(f"Nombre: {producto_actual[1]}")
                    print(f"Descripción: {producto_actual[2]}")
                    print(f"Precio: {producto_actual[3]}")
                    print(f"Categoría ID: {producto_actual[4]}")

                    confirmar = input("\n¿Desea actualizar el stock de este producto? (s/n): ").lower()
                    if confirmar == 's':
                        nueva_cantidad = int(input("Ingrese la nueva cantidad de stock:\n"))
                        cursor.execute(
                            "UPDATE inventory SET quantity = %s WHERE product_id = %s",
                            (nueva_cantidad, id_product)
                        )
                        conn.commit()
                        print("\n✅ Stock actualizado correctamente")
                        on = False
                    else:
                        print("\n❌ Operación cancelada. Volviendo a menú anterior.")
                        on = False
                    time.sleep(2)

        except ValueError:
            print("Ingrese valores numéricos enteros\n")
            time.sleep(2)

    cursor.close()
    conn.close()
    input("\nPresione Enter para continuar")
