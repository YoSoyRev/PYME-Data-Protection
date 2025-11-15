# Matriz de Evaluación de Riesgos

## Metodología
Se utiliza una matriz de 3x3 (Probabilidad vs. Impacto) para priorizar amenazas.

## Análisis de Amenazas

| Amenaza | Descripción | Probabilidad | Impacto | Nivel de Riesgo | Control Propuesto |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ransomware** | Cifrado malicioso de la BD de clientes. | Media (2) | Crítico (3) | **ALTO (6)** | Backups offline + Endpoint Protection. |
| **Phishing** | Robo de credenciales de correo. | Alta (3) | Alto (2) | **ALTO (6)** | MFA + Capacitación. |
| **Robo de Equipo** | Robo de laptop de ventas con Excel local. | Media (2) | Alto (2) | **MEDIO (4)** | Cifrado de disco (BitLocker). |
| **Fuga Interna** | Empleado copia base de datos a USB. | Baja (1) | Alto (2) | **BAJO (2)** | Bloqueo de puertos USB. |