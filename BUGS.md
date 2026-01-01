# Bug report

## Bug ID
BUG-001

## Nombre del bug
Sistema permite registrar clientes con correos electrónicos inválidos.

## Descripcion
El sistema permite registrar un cliente ingresando un correo electrónico sin formato válido, sin mostrar mensajes de error ni impedir el registro.

## Pasos para reproducir
1. Iniciar el programa en el script "app.py" en el terminal.
2. Seleccionar la opcion "1.Realizar pedido" del menu.
3. Ingresar correo electronico sin "@" ejemplo: usuario123

## Resultado esperado
El sistema debería mostrar un mensaje de error indicando que el correo es inválido y no permitir el registro.

## Resultado actual
Mostrar el mensaje "Cliente registrado con exito, Nro. de orden X"

## Bug ID
BUG-002

## Nombre del bug
Menu de administrador en bucle infinito.

## Descripcion
No permite volver al menu principal una vez dentro del menu de administrador.

## Pasos para reproducir
1. Iniciar el programa en el script "app.py" en el terminal.
2. Seleccionar la opcion "5.Opciones de administrador" del menu.
3. Ingresar clave de administrador.
4. Seleccionar la opcion "4.Salir" del menu admin.

## Resultado esperado
Volver al menu principal

## Resultado actual
Vuelvo al menu de administrador

## Nota
Existen múltiples validaciones pendientes en el sistema.
En este documento se reportan bugs representativos para demostrar el proceso de detección, documentación y corrección.