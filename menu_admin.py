from admin_functions import ver_pedidos, ver_inventario, ajustar_stock
from my_utils import pausa_limpia

def salir():
    print("Has salido del menu admin")
    pausa_limpia()
    return False

def menu_administrador(CLAVE_ADMIN):
    clave_admin = input("Ingrese la contraseña:\n")

    if clave_admin == CLAVE_ADMIN:
        print("\t\t--- ACCESO CONCEDIDO ---\n")
        pausa_limpia(1)

        on = True
        while on:
            pausa_limpia(1)
            print ("\t\t--- ADMIN MENU ---\n")
            print ("1 - Ver todos los pedidos")
            print ("2 - Ver inventario")
            print ("3 - Ajustar stock")
            print ("4 - Salir\n")
            opcion_str = input("Seleccione una opcion:\n")

            if not opcion_str.isdigit():
                print("\nOpcion invalida, ingrese solo carecteres numericos")
                continue

            opcion = int(opcion_str)   
            if opcion == 1:
                ver_pedidos()

            elif opcion == 2:
                ver_inventario()

            elif opcion == 3:
                ajustar_stock()

            elif opcion == 4:
                on = salir()

            else:
                print(f"Opción {opcion} invalida. Ingrese una opcion entre 1 y 4.")
    else:
        print ("\t\n--- ACCESO DENEGADO ---\n")
        pausa_limpia(1)