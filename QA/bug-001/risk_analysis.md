# Risk Analysis – Bug-001

## Bug ID
- BUG-001

## Risk Summary
- El registro de clientes con datos inválidos impide el correcto seguimiento de las ventas y afecta la visibilidad del negocio sobre las transacciones realizadas.

## Affected Area
- Flujo de registro de clientes y seguimiento de ventas.

## Impact
- Business impact: No es posible asociar ventas a clientes válidos, lo que afecta el control y análisis de las ventas.

- User impact: Los clientes no quedan correctamente registrados o no aparecen de forma adecuada en el sistema.

- Data / system impact: Se almacenan datos inválidos o inconsistentes en la base de datos.

## Probability
- Alta

## Severity
- Alta

## Risk Level
- Crítica

## Detection
- Pruebas de QA manual y reportes de usuarios.

## Mitigation
- Implementación de validaciones en la entrada de datos durante el registro de clientes.

## Residual Risk
- Ninguno

## Status
- Cerrado
