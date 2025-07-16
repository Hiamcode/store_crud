from database.connection import get_connection
import os
import time

def realizar_pedido():
    on = True
    while on:
        os.system('cls' if os.name == 'nt' else 'clear')
        conn = get_connection()
        cursor = conn.cursor()

        print("\t\t--- REGISTRO DE USUARIO ---\n")
        email = input("Ingrese su correo electrónico:\n")
        cursor.execute("SELECT user_id FROM users WHERE email = %s", (email,))
        existe = cursor.fetchone()

        if existe:
            print("❌ El usuario ya existe. Intente con otro correo.")
            time.sleep(2)
            on = False
        else:
            nombre = input("Ingrese su nombre:\n")
            apellido = input("Ingrese su apellido:\n")
            try:
                edad = int(input("Ingrese su edad:\n"))
            except ValueError:
                edad = None
            telefono = input("Ingrese su número de teléfono:\n")
            direccion = input("Ingrese su dirección:\n")

            cursor.execute("""
                INSERT INTO users (name, last_name, age, email, phone, address, registration_date)
                VALUES (%s, %s, %s, %s, %s, %s, NOW())
            """, (nombre, apellido, edad, email, telefono, direccion))
            conn.commit()

            cursor.execute("SELECT user_id FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()

            if not user:
                print("❌ Error registrando usuario.")
                time.sleep(2)
                on = False
            else:
                cursor.execute("INSERT INTO orders (user_id, order_status_id, order_date, total) VALUES (%s, %s, NOW(), %s)", (user[0], 1, 0))
                conn.commit()
                cursor.execute("SELECT LAST_INSERT_ID()")
                order_id = cursor.fetchone()[0]

                total_pedido = 0
                seguir = True
                while seguir:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    cursor.execute("""
                        SELECT p.product_id, p.product_name, p.product_description, p.product_price, i.quantity
                        FROM products p
                        JOIN inventory i ON p.product_id = i.product_id
                    """)
                    productos = cursor.fetchall()

                    print("\n--- 📦 Productos disponibles ---\n")
                    for p in productos:
                        print(f"ID: {p[0]} | Nombre: {p[1]} | Descripción: {p[2]} | Precio: {p[3]} | Stock: {p[4]}")

                    try:
                        producto_id = int(input("\nIngrese el ID del producto que desea agregar:\n"))
                        cantidad = int(input("Ingrese la cantidad:\n"))

                        cursor.execute("SELECT product_price FROM products WHERE product_id = %s", (producto_id,))
                        precio = cursor.fetchone()
                        cursor.execute("SELECT quantity FROM inventory WHERE product_id = %s", (producto_id,))
                        stock = cursor.fetchone()

                        if precio and stock and cantidad <= stock[0]:
                            subtotal = precio[0] * cantidad
                            total_pedido += subtotal
                            cursor.execute("INSERT INTO order_products (order_id, product_id, quantity) VALUES (%s, %s, %s)", (order_id, producto_id, cantidad))
                            cursor.execute("UPDATE inventory SET quantity = quantity - %s WHERE product_id = %s", (cantidad, producto_id))
                            conn.commit()
                            print(f"✅ Producto agregado. Subtotal: {subtotal}")
                            time.sleep(2)
                        else:
                            print("❌ Stock insuficiente o producto no existe.")
                            time.sleep(2)
                    except ValueError:
                        print("❌ Entrada inválida.")
                        time.sleep(2)

                    otro = input("¿Desea agregar otro producto? (s/n)\n").lower()
                    if otro != "s":
                        seguir = False

                cursor.execute("UPDATE orders SET total = %s WHERE orders_id = %s", (total_pedido, order_id))
                conn.commit()
                print(f"\n✅ Pedido creado exitosamente con total: {total_pedido}")
                time.sleep(3)
                on = False

        cursor.close()
        conn.close()


    
def pagar_pedido(fondos_usuarios):
    on = True
    while on:
        print("\t\t--- BUSQUEMOS EL PEDIDO ---\n")
        conn = get_connection()
        cursor = conn.cursor()

        os.system('cls' if os.name == 'nt' else 'clear')
        registro = input("Ingrese correo asociado al pedido:\n")
        cursor.execute("SELECT email FROM users WHERE email = %s", (registro,))
        buscado = cursor.fetchone()

        if not buscado:
            print("No existen pedidos asociados a ese correo.\n")
            time.sleep(2)
            on = False
        else:
            print("\t\t--- 📦 PEDIDOS ENCONTRADOS ---\n")
            cursor.execute("""
                SELECT o.orders_id, p.product_id, p.name, p.description, p.price, op.quantity
                FROM users u 
                JOIN orders o ON u.user_id = o.user_id
                JOIN order_products op ON o.orders_id = op.orders_id
                JOIN product p ON op.product_id = p.product_id
                WHERE u.email = %s
            """, (registro,))
            pedidos = cursor.fetchall()

            for fila in pedidos:
                print("-"*50)
                print(f"ID.Pedido: {fila[0]}")
                print(f"ID.Producto: {fila[1]}")
                print(f"Nombre: {fila[2]}")
                print(f"Descripcion: {fila[3]}")
                print(f"Precio: {fila[4]}")
                print(f"Cantidad: {fila[5]}\n")

            entrada = input("Desea continuar con el método de pago?(s/n)\n").lower()
            if entrada == "s":
                onn = True
                while onn:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("\t\t--- SELECCIONE UN METODO DE PAGO ---\n")
                    print("1 - Credito")
                    print("2 - Debito")
                    print("3 - Transferencia Bancaria")
                    print("4 - Paypal\n")
                    try:
                        opcion = int(input("-"))
                        if opcion in (1,2,3,4):
                            fondos_usuarios -= fila[4]
                            if fondos_usuarios > 0:
                                cursor.execute("""
                                    UPDATE orders
                                    SET order_status_id = 2, payment_method_id = %s
                                    WHERE orders_id = %s""", (opcion, fila[0]))
                                conn.commit()
                                print("✅ Pedido marcado como 'Paid'")
                                time.sleep(2)
                                onn = False
                                on = False                        
                        else:
                            print(f"❌ La opción {opcion} no es válida. Seleccione una opción entre 1 y 4\n")
                            time.sleep(3)
                    except ValueError:
                        print("❌ Entrada inválida. Ingrese un número.")
                        time.sleep(2)
            else:
                print("❌ Operación cancelada. Volviendo al menú anterior.")
                time.sleep(2)
                on = False

        cursor.close()
        conn.close()

def ver_estado_pedidos():
    on = True
    while on:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t--- BUSQUEMOS EL PEDIDO ---\n")
        conn = get_connection()
        cursor = conn.cursor()

        registro = input("Ingrese correo asociado al pedido:\n")
        cursor.execute("SELECT email FROM users WHERE email = %s", (registro,))
        buscado = cursor.fetchone()

        if not buscado:
            print("No existen pedidos asociados a ese correo.\n")
            time.sleep(2)
            on = False
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\t\t--- 📦 PEDIDOS ENCONTRADOS ---\n")
            cursor.execute("""
                SELECT o.orders_id, p.name, p.price, os.status_name
                FROM orders o
                JOIN users u ON o.user_id = u.user_id
                JOIN order_products op ON o.orders_id = op.orders_id
                JOIN product p ON op.product_id = p.product_id
                JOIN order_status os ON o.order_status_id = os.order_status_id
                WHERE u.email = %s
            """, (registro,))

            vista = cursor.fetchall()
            
            for x in vista:
                print("-"*50)
                print(f"ID. pedido: {x[0]}")
                print(f"Nombre: {x[1]}")
                print(f"Precio: {x[2]}")
                print(f"Estado del pedido: {x[3]}")

            input("Presione Enter para salir\n")
            cursor.close()
            conn.close()
            on = False

def cancelar_pedidos():
    on = True
    while on:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t--- BUSQUEMOS EL PEDIDO ---\n")
        conn = get_connection()
        cursor = conn.cursor()

        registro = input("Ingrese correo asociado al pedido:\n")
        cursor.execute("SELECT email FROM users WHERE email = %s", (registro,))
        buscado = cursor.fetchone()

        if not buscado:
            print("No existen pedidos asociados a ese correo.\n")
            time.sleep(2)
            on = False
        else:
            cursor.execute("""
                SELECT o.orders_id, p.name, p.price, os.status_name
                FROM orders o
                JOIN users u ON o.user_id = u.user_id
                JOIN order_status os ON o.order_status_id = os.order_status_id
                JOIN order_products op ON o.orders_id = op.orders_id
                JOIN product p ON op.product_id = p.product_id
                WHERE u.email = %s
            """, (registro,))
            pedidos = cursor.fetchall()

            if pedidos:
                print("\t\t--- 📦 PEDIDOS ENCONTRADOS ---\n")
                for pedido in pedidos:
                    print("-"*40)
                    print(f"ID Pedido: {pedido[0]}")
                    print(f"Producto: {pedido[1]}")
                    print(f"Precio: {pedido[2]}")
                    print(f"Estado: {pedido[3]}")

                pedido_ids = [pedido[0] for pedido in pedidos]  # IDs válidos

                onn = True
                while onn:
                    try:
                        pedido_id = int(input("\nIngrese el ID del pedido que desea cancelar:\n"))
                        if pedido_id not in pedido_ids:
                            print("❌ Ese ID no está en la lista de pedidos mostrados.")
                            continue
                        confirmacion = input("Seguro que deseas cancelar el pedido? (Escribe 'CANCELAR PEDIDO' para confirmar)\n")
                        if confirmacion == "CANCELAR PEDIDO":
                            cursor.execute("UPDATE orders SET order_status_id = 5 WHERE orders_id = %s", (pedido_id,))
                            conn.commit()
                            print("✅ Pedido cancelado correctamente.")
                            onn = False
                            on = False
                        else:
                            print("❌ Operación cancelada. Volviendo al menú anterior.\n")
                            time.sleep(3)
                            onn = False
                            on = False
                    except ValueError:
                        print("❌ ID inválido. Ingrese valores enteros.")
                        time.sleep(2)
            else:
                print("❌ No hay pedidos para cancelar.")
                time.sleep(2)
                on = False

        cursor.close()
        conn.close()
