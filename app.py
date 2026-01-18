from database.connection import get_connection
from menu_admin import menu_administrador
from users_functions import realizar_pedido, pagar_pedido, ver_estado_pedidos, cancelar_pedidos
from my_utils import pausa_limpia

def salir():
    print("Gracias por usar el sistema. Hasta luego 👋\n")
    pausa_limpia(1)
    return False

def menu():
    on = True
    CLAVE_ADMIN= "123admin"
    fondos_usuarios = 99_999_999
    while on:
        pausa_limpia(1)
        print("\t\t--- WELCOME TO CODE STORE ---\n")
        print("\t\t-- Menú principal --\n")
        print("1 - Realizar pedido") 
        print("2 - Pagar pedido")
        print("3 - Ver estado de mi pedido")
        print("4 - Cancelar pedido")
        print("5 - Opciones de administrador")
        print("6 - Salir del sistema\n")
        opcion_str = input("Seleccione una opcion:\n").strip()

        if not opcion_str.isdigit():
            print("\nOpcion invalida, ingrese solo caracteres numericos\n")
            continue
        opcion = int(opcion_str)
        if opcion == 1:
            realizar_pedido()

        elif opcion == 2:
            pagar_pedido(fondos_usuarios)

        elif opcion == 3:
            ver_estado_pedidos()

        elif opcion == 4:
            cancelar_pedidos()

        elif opcion == 5:
            menu_administrador(CLAVE_ADMIN)

        elif opcion == 6:
            on = salir()

        else:
            print(f"❌Opción {opcion} aún no implementada. Elige una opcion entre 1 y 6.\n")
            pausa_limpia()

if __name__ == "__main__":
    menu()