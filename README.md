# Ágora Hábitat

Sistema IoT de monitorización de viviendas en una zona residencial costera. Aplicación de escritorio en **Python + Flet** con patrón **Modelo-Vista-Controlador**. Los datos se guardan en ficheros **JSON**.

*Vivir en comunidad, a pie de playa.*

## Equipo

Héctor Muñoz · Hugo Rojo · Jesús Guinea · Pablo Molina

## Roles de usuario

| Rol | Quién es | Qué ve |
|---|---|---|
| Residente | Usuario principal (9 en los datos) | Sus sensores: temperatura y humedad, CO₂ y consumo eléctrico |
| Supervisor | Administrador de comunidad o familiar (4) | Los residentes a su cargo |
| Analista | Técnico que analiza los datos (2) | Comparativas e informes de las viviendas asignadas |

## Cómo ejecutarlo

1. Abre la carpeta del proyecto en PyCharm.
2. Crea un intérprete virtual e instala las dependencias: `pip install -r requirements.txt`.
3. Ejecuta `main.py`.

Usuarios de prueba (contraseña `agora123`):

- Residente: `l.fernandez@correo.es`
- Supervisor: `j.morales@correo.es`
- Analista: `e.ruiz@correo.es`

Para regenerar los datos de prueba: `python tools/generar_datos.py`.

## Estructura

```
main.py                 Punto de entrada
app/model/              Acceso a los JSON y validaciones (DNI, teléfono, correo)
app/view/               Vistas Flet: login, registro y una vista por rol
app/controller/         Navegación por rol, inicio de sesión y registro
data/                   usuarios.json, sensores.json, medidas.json, sugerencias.json
assets/                 Logo
docs/                   Diagrama de Gantt y mockups
tools/                  Generador de datos de prueba
```

Todas las rutas son relativas al proyecto, así que funciona en cualquier equipo.

## Datos de prueba

- 9 residentes, 4 supervisores y 2 analistas.
- Un residente con más de un supervisor y un supervisor con varios residentes.
- 3 sensores por residente (3 tipos distintos), con medidas cada 2 horas durante 4 días.
- DNI con letra válida y teléfonos de 9 cifras.

## Planificación

Scrum con sprints de 2 semanas. Ver [docs/Gantt_Agora_Habitat.png](docs/Gantt_Agora_Habitat.png) y los [mockups](docs/Mockups_Agora_Habitat.pdf).
