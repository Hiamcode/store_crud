from admin_functions import ver_pedidos, ver_inventario, ajustar_stock
from my_utils import pausa_limpia

def salir():
    print("Haz salido del menu admin")
    pausa_limpia()
    return False

def menu_administrador(CLAVE_ADMIN):
    clave_admin = input("Ingrese la contraseña:\n")
    if clave_admin == CLAVE_ADMIN:
        print("\t\t--- ACCESO CONCEDIDO ---\n")
        pausa_limpia()
        on = True
        while on:
            pausa_limpia()
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
                    pausa_limpia()
            except ValueError:
                print("Ingrese solo caracteres numéricos\n")
                input("Presione Enter para continuar...")
                continue
    else:
        print ("--- ACCESO DENEGADO ---\n")
        input("Presione Enter para continuar...")