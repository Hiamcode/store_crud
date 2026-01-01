from database.connection import get_connection
import os
import time

def ver_pedidos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT o.orders_id, u.email, p.product_name, p.product_price, os.status_name
        FROM orders o
        JOIN users u ON o.user_id = u.user_id
        JOIN order_products op ON o.orders_id = op.order_id
        JOIN products p ON op.product_id = p.product_id
        JOIN order_status os ON o.order_status_id = os.order_status_id
        ORDER BY o.orders_id""")
    pedidos = cursor.fetchall()
    if not pedidos:
        print("\nAún no hay pedidos registrados por clientes")
        time.sleep(2)
    else:
        print("\n--- 📦 PEDIDOS REGISTRADOS ---\n")
        for pedido in pedidos:
            print(f"ID Pedido: {pedido[0]}")
            print(f"Correo Usuario: {pedido[1]}")
            print(f"Producto: {pedido[2]}")
            print(f"Precio: ${pedido[3]}")
            print(f"Estado del Pedido: {pedido[4]}")
            print("-" * 40)
        input("\nPresione enter para continuar")
    cursor.close()
    conn.close()


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
                break

            id_product = int(entrada)
            cursor.execute(
                "SELECT p.product_id, p.product_name, p.product_description, p.product_price, p.category_id, i.quantity "
                "FROM products p "
                "JOIN inventory i ON p.product_id = i.product_id "
                "WHERE p.product_id = %s",(id_product,))
            producto_actual = cursor.fetchone()

            if not producto_actual:
                print("\n❌ Producto no encontrado con ese ID")
                time.sleep(2)
                continue
            else:
                print("\n📦 Producto encontrado:")
                print(f"ID: {producto_actual[0]}")
                print(f"Nombre: {producto_actual[1]}")
                print(f"Descripción: {producto_actual[2]}")
                print(f"Precio: {producto_actual[3]}")
                print(f"Categoría ID: {producto_actual[4]}")
                print(f"Cantidad actual: {producto_actual[5]}")

                confirmar = input("\n¿Desea actualizar el stock de este producto? (s/n): ").lower()
                if confirmar != 's':
                    print("\n❌ Operación cancelada. Volviendo a menú anterior.")
                    time.sleep(2)
                    on = False
                    break

                while True:
                    nueva_cantidad_str = input("Ingrese la nueva cantidad de stock (o '*' para cancelar):\n")
                    if nueva_cantidad_str == '*':
                        print("❌ Operación cancelada. Volviendo a menú anterior.")
                        time.sleep(2)
                        on = False
                        break
                    else:
                        try:
                            nueva_cantidad = int(nueva_cantidad_str)
                            if nueva_cantidad == producto_actual[5]:
                                print("⚠️ El producto ya tiene esta cantidad de stock. Indique otra cantidad o cancele con '*'\n")
                                time.sleep(4)
                            else:
                                cursor.execute(
                                    "UPDATE inventory SET quantity = %s WHERE product_id = %s",
                                    (nueva_cantidad, id_product)
                                )
                                conn.commit()
                                print("\n✅ Stock actualizado correctamente")
                                time.sleep(2)
                                on = False
                                break
                        except ValueError:
                            print("Ingrese un número entero válido.\n")
                            time.sleep(2)

        except ValueError:
            print("Ingrese un número entero válido para el ID o '*' para cancelar.\n")
            time.sleep(2)

    cursor.close()
    conn.close()
    input("\nPresione Enter para continuar")