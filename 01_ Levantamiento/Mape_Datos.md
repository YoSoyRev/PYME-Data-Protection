# Mapeo de Flujo de Datos Personales

## Ciclo de Vida del Dato
1. **Recolección:** Los datos ingresan vía formulario web (www.ejemplo-pyme.com) o por teléfono.
2. **Almacenamiento:** Se guardan en el Servidor `ACT-002` (Base de datos SQL) y respaldos en `NAS-01`.
3. **Uso:** El área de ventas consulta teléfonos para llamadas; Finanzas consulta RFC para facturar.
4. **Eliminación:** Datos de prospectos no cerrados se eliminan a los 12 meses (Política de Retención).

## Categorías de Datos Tratados
| Tipo de Dato | Ejemplos | Nivel de Protección |
| :--- | :--- | :--- |
| **Identificativos** | Nombre, Domicilio, Teléfono | MEDIO |
| **Fiscales** | RFC, Dirección Fiscal | MEDIO |
| **Patrimoniales** | No. Cuenta Bancaria, Historial Compras | ALTO (Requiere Cifrado) |