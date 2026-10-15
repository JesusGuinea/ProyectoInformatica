"""Componentes comunes de la interfaz: colores de marca y cabecera con nombre y rol."""
import flet as ft

OCEANO = "#0B6E99"
TURQUESA = "#2FB8B0"
CORAL = "#F0664A"
ARENA = "#F1E2C6"
MARINO = "#0B2A43"
ESPUMA = "#FBF8F1"

ROL_TEXTO = {"residente": "Residente", "supervisor": "Supervisor", "analista": "Analista"}


def cabecera(titulo: str, usuario: dict, al_salir) -> ft.Control:
    """Cabecera de todas las vistas: logo, título, nombre y rol del usuario y botón de salir."""
    rol = ROL_TEXTO[usuario["rol"]] + (f" · {usuario['tipo']}" if usuario.get("tipo") else "")
    return ft.Container(
        bgcolor=MARINO, padding=ft.Padding.symmetric(horizontal=20, vertical=12),
        content=ft.Row(
            [
                ft.Row([ft.Image(src="logo.png", width=40, height=40),
                        ft.Text(titulo, size=20, weight=ft.FontWeight.BOLD, color="white")], spacing=12),
                ft.Row([
                    ft.Column([ft.Text(f"{usuario['nombre']} {usuario['apellidos']}", color="white", weight=ft.FontWeight.BOLD),
                               ft.Text(rol, color=ARENA, size=12)], spacing=0, horizontal_alignment=ft.CrossAxisAlignment.END),
                    ft.IconButton(ft.Icons.LOGOUT, icon_color="white", tooltip="Salir", on_click=al_salir),
                ]),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN, wrap=True,
        ),
    )


def tarjeta(titulo: str, valor: str, unidad: str = "") -> ft.Control:
    return ft.Container(
        bgcolor="white", border_radius=12, padding=16, width=260,
        border=ft.Border.all(1, "#E7DFCF"),
        content=ft.Column([ft.Text(titulo, color="#5E7180", size=13),
                           ft.Row([ft.Text(valor, size=28, weight=ft.FontWeight.BOLD, color=MARINO),
                                   ft.Text(unidad, color="#5E7180")], vertical_alignment=ft.CrossAxisAlignment.END)]),
    )
