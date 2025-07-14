# store_crud

Sistema CRUD para una tienda que vende dispositivos, componentes y accesorios de computadoras; realizado con base de datos relacionales (MySQL) y backend en Python.
Entrega 2 experiencias, tanto de usuario como de adminstrador de tienda, donde como usuario puedes registrarte y realizar un pedido, ver estado de tus pedidos, metodos de pagos y cancelar tus pedidos. y como admin Permite gestionar productos, categorías, pedidos e inventarios, con control de stock y seguimiento de estados de pedidos.

## Tecnologías usadas

- MySQL
- Python
- Git

## Diagrama de la base de datos

![Database Diagram](./diagrams/database_diagram.svg)

## Instrucciones para ejecutar

1. Clona el repositorio
2. Ejecuta el script de base de datos en MySQL
3. Corre la aplicación backend con Python

## Estructura de la base de datos

El sistema está compuesto por las tablas principales:
- `Category`: Categorías de productos
- `Product`: Productos vinculados a categorías
- `Inventory`: Control de stock por producto
- `Order`: Registro de pedidos con estados y métodos de pago
- `Order_Product`: Tabla intermedia para productos en pedidos

## Contacto

Para consultas o sugerencias, puedes contactarme en: holasoyjesusavila@gmail.com