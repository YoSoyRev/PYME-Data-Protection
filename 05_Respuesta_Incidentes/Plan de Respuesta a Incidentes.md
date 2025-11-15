# Plan de Respuesta a Incidentes (IRP) - Ransomware y Fugas

Este documento define el procedimiento de actuación ante la detección de un ciberataque.

## Roles y Responsabilidades
* **Líder de Respuesta:** Admin de Sistemas (Toma decisiones).
* **Comunicación:** Gerente General (Habla con clientes/autoridades).
* **Soporte:** Técnico IT (Ejecuta acciones técnicas).

## Flujo de Respuesta (Fases)

### Fase 1: Detección e Identificación
**Señales de Alerta:**
* El equipo funciona extremadamente lento.
* Archivos cambian de extensión (ej. `.locked`, `.crypt`).
* Ventana emergente pidiendo rescate (Ransomware).
* Antivirus lanzando alertas múltiples.

### Fase 2: Contención (¡CRÍTICO!)
Si se confirma la infección:
1. **DESCONECTAR CABLE DE RED / WI-FI INMEDIATAMENTE.** (Aislar el equipo para que no infecte a otros).
2. **NO APAGAR EL EQUIPO.** (Apagarlo puede destruir evidencia en memoria RAM o impedir que expertos recuperen llaves de cifrado).
3. Desconectar discos duros externos y USBs.

### Fase 3: Erradicación y Recuperación
1. Formatear el equipo infectado (Reinstalación limpia).
2. Escanear la red para asegurar que no hay otros equipos afectados.
3. **Restaurar datos desde el Respaldo Seguro (Backup)** verificado previamente.
4. Cambiar todas las contraseñas del usuario afectado.

### Fase 4: Lecciones Aprendidas (Post-Incidente)
* Documentar: ¿Cómo entró el virus? (Correo, USB, Web).
* Ajustar controles: ¿Necesitamos mejor antivirus? ¿Más capacitación?
* Notificación: Si hubo fuga de datos personales, notificar a los titulares según la LFPDPPP.