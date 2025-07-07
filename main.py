import os
import time
from menu_admin import menu_admin

def salir():
    print("Gracias por usar el sistema. Hasta luego 👋\n")
    time.sleep(2)
    return False

def menu():
    on = True
    CLAVE_ADMIN= "123admin"
    while on:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\t\t--- WELCOME TO CODE STORE ---\n")
        print("\t\t-- Menú principal --\n")
        print("1 - Realizar pedido (registro de cliente + armar pedido)")
        print("2 - Ver estado de mi pedido (buscar pedido por ID o por datos del cliente)")
        print("3 - Pagar pedido (seleccionar método de pago, validar que tenga pedido pendiente)")
        print("4 - Cancelar pedido (buscar pedido y eliminarlo si está pendiente)")
        print("5 - Opciones de administrador (pides clave o password simple)")
        print("6 - Salir del sistema\n")
        try:
            opcion = int(input("Seleccione una opcion:\n"))
            if opcion == 1:
                print ("a")
            elif opcion == 2:
                print ("a")
            elif opcion == 3:
                print ("a")
            elif opcion == 4:
                print ("a")
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