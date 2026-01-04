# Post Fix – Bug-002

## Bug ID
- BUG-002

## Fix Summary
- Se corrigió la lógica de control del menú administrador, permitiendo su apertura y cierre adecuados.

## Root Cause
- Flujo lógico incorrecto en la gestión del estado del menú administrador.

## Fix Implementation
- Se ajustó la variable de control del menú para asegurar una transición correcta entre estados.

## Validation
- Se validó el ingreso y salida del menú administrador mediante la selección de opciones correspondientes.
- Se confirmó que no se generan bucles infinitos ni bloqueos del flujo principal.

## Status
- Cerrado

