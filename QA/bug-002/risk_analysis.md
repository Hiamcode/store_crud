# Risk Analysis – Bug-002

## Bug ID
- BUG-002

## Risk Summary
- La imposibilidad de salir del menú de administrador genera un riesgo crítico al exponer funciones administrativas y bloquear el flujo normal de compras del sistema.

## Affected Area
- Flujo logico del programa.
- Gestión y control de funciones administrativas.

## Impact
- Business impact: Exposición de funciones administrativas que comprometen la operación normal del negocio y afectan directamente la capacidad de generar ventas.

-User impact: Los usuarios no pueden completar compras y, en escenarios maliciosos o accidentales, pueden alterar información sensible del sistema (stock, estado de productos, configuraciones).

-Data / system impact: Riesgo de alteración de datos, uso indebido de funciones críticas y comportamiento inconsistente del sistema debido a un flujo lógico incorrecto.

## Probability
- Alta

## Severity
- Alta

## Risk Level
- Crítica

## Detection
- Pruebas de QA manual enfocadas en validación de flujo y comportamiento del sistema.

## Mitigation
- Implementacion de validacion de flujo logico y correcto cierre de menu.

## Residual Risk
- Ninguno

## Status
- Cerrado