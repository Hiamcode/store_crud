import os
import time
from database.connection import get_connection
from menu_admin import menu_admin
from users_functions import realizar_pedido, pagar_pedido, ver_estado_pedidos, cancelar_pedidos


def salir():
    print("Gracias por usar el sistema. Hasta luego 👋\n")
    time.sleep(2)
    return False

def menu():
    on = True
    CLAVE_ADMIN= "123admin"
    fondos_usuarios = 99_999_999
    while on:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t--- WELCOME TO CODE STORE ---\n")
        print("\t\t-- Menú principal --\n")
        print("1 - Armar pedido") 
        print("2 - Pagar pedido")
        print("3 - Ver estado de mi pedido")
        print("4 - Cancelar pedido")
        print("5 - Opciones de administrador")
        print("6 - Salir del sistema\n")
        try:
            opcion = int(input("Seleccione una opcion:\n"))
            if opcion == 1:
                realizar_pedido()
            elif opcion == 2:
                pagar_pedido(fondos_usuarios)
            elif opcion == 3:
                ver_estado_pedidos()
            elif opcion == 4:
                cancelar_pedidos()
            elif opcion == 5:
                menu_admin(CLAVE_ADMIN)
            elif opcion == 6:
                on = salir()
            else:
                print(f"Opción {opcion} aún no implementada. Elige una opcion entre 1 y 6.\n")
                time.sleep(2)
        except ValueError:
            print("Ingrese solo caracteres numéricos\n")
            input("Presione Enter para continuar...")
            continue
if __name__ == "__main__":
    menu()