"""Vista del analista: viviendas asignadas para análisis."""
import flet as ft

from app.view.componentes import cabecera


class AnalistaView:
    def __init__(self, controller):
        self.c = controller

    def construir(self) -> ft.Control:
        u = self.c.usuario
        residentes = self.c.repo.residentes_de(u)
        lista = ft.ListView([ft.ListTile(title=ft.Text(f"{r['nombre']} {r['apellidos']}"), subtitle=ft.Text(r.get("direccion", "")),
                                         leading=ft.Icon(ft.Icons.HOME)) for r in residentes], expand=True)
        return ft.Column([
            cabecera("Panel de análisis", u, self.c.ir_login),
            ft.Container(padding=20, expand=True, content=ft.Column([ft.Text(f"{len(residentes)} viviendas asignadas"), lista], expand=True)),
            # TODO Sprint 3: comparativa de sensores e informes
        ], expand=True)
