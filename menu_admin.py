import os
import time
from admin_functions import ver_pedidos, ver_inventario, ajustar_stock

def salir():
    print("Haz salido del menu admin")
    time.sleep(2)
    return False

def menu_admin(CLAVE_ADMIN):
    clave_admin = input("Ingrese la contraseña:\n")
    if clave_admin == CLAVE_ADMIN:
        print("\t\t--- ACCESO CONCEDIDO ---\n")
        time.sleep(2)
        on = True
        while on:
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("\t\t--- ADMIN MENU ---\n")
            print ("1 - Ver todos los pedidos")
            print ("2 - Ver inventario")
            print ("3 - Ajustar stock")
            print ("4 - Salir\n")
            try:
                opcion = int(input("Seleccione una opcion:\n"))
                if opcion == 1:
                    ver_pedidos()
                elif opcion == 2:
                    ver_inventario()
                elif opcion == 3:
                    ajustar_stock()
                elif opcion == 4:
                    on = salir()
                else:
                    print(f"Opción {opcion} aún no implementada. Elige una opcion entre 1 y 4.")
                    time.sleep(2)
            except ValueError:
                print("Ingrese solo caracteres numéricos\n")
                input("Presione Enter para continuar...")
                continue
    else:
        print ("--- ACCESO DENEGADO ---\n")
        input("Presione Enter para continuar...")