from database.connection import get_connection
from my_utils import pausa_limpia

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
        pausa_limpia()
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
            pausa_limpia(0)
            entrada = input("Ingrese el ID del producto que desea actualizar (o '*' para salir):\n").strip()

            if entrada == '*':
                print("❌ Operación cancelada. Volviendo a menú anterior.")
                pausa_limpia()
                return

            elif not entrada.isdigit():
                print("\n❌ ID inválido. Ingrese caracteres numéricos o '*' para salir.")
                pausa_limpia()
                continue
            
            id_product = int(entrada)

            if id_product < 1 or id_product > 10:
                print("\n❌ ID inválido. Ingrese ID de productos existentes (1 a 10).")
                pausa_limpia()
                continue
            
            else:
                cursor.execute(
                    "SELECT p.product_id, p.product_name, p.product_description, p.product_price, p.category_id, i.quantity "
                    "FROM products p "
                    "JOIN inventory i ON p.product_id = i.product_id "
                    "WHERE p.product_id = %s",(id_product,))
                producto_actual = cursor.fetchone()
                if not producto_actual:
                    print("\n❌ Producto no encontrado.")
                    pausa_limpia()
                    continue

                validacion_cambio_stock = True
                while validacion_cambio_stock:

                    print("\n📦 Producto encontrado:")
                    print(f"ID: {producto_actual[0]}")
                    print(f"Nombre: {producto_actual[1]}")
                    print(f"Descripción: {producto_actual[2]}")
                    print(f"Precio: {producto_actual[3]}")
                    print(f"Categoría ID: {producto_actual[4]}")
                    print(f"Cantidad actual: {producto_actual[5]}")
                    
                    confirmar = input("\n¿Desea actualizar el stock de este producto? (s/n): ").lower().strip()
                    if confirmar == 'n':
                        print("\n❌ Operación cancelada. Volviendo a menú anterior.")
                        pausa_limpia()
                        validacion_cambio_stock = False
                        on = False
                        
                    elif confirmar == 's':
                        print("\n✅ Confirma modificar stock.")
                        validacion_cambio_stock = False

                    else:
                        print("\n❌ Ingreso invalido, ingrese solo caracteres validos 's/n'")
                        pausa_limpia(3)
                        continue

                validacion_cantidad_stock = True
                while validacion_cantidad_stock:
                        
                    entrada = input("Ingrese la nueva cantidad de stock (o '*' para cancelar):\n").strip()
                    if entrada == '*':
                        print("❌ Operación cancelada. Volviendo a menú anterior.")
                        pausa_limpia()
                        return

                    elif not entrada.isdigit():
                        print("\n❌ Ingreso invalido, ingrese solo caracteres numericos enteros (o '*' para cancelar).")
                        pausa_limpia()
                        continue
                    
                    cantidad_actual = int(entrada)

                    if cantidad_actual < 0 or cantidad_actual > 200:
                        print("\n❌ Operacion imposible, ingrese stock entre 0 a 200.")
                        pausa_limpia()
                        continue

                    if cantidad_actual == producto_actual[5]:
                            print("⚠️ El producto ya tiene esta cantidad de stock. Indique otra cantidad o cancele con '*'\n")
                            pausa_limpia(4)
                    else:
                        cursor.execute(
                            "UPDATE inventory SET quantity = %s WHERE product_id = %s",
                            (cantidad_actual, id_product)
                        )
                        conn.commit()
                        print("\n✅ Stock actualizado correctamente.")
                        pausa_limpia()
                        on = False
                        return

    cursor.close()
    conn.close()
    input("\nPresione Enter para continuar")