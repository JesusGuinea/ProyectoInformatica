"""Vista del supervisor: residentes a su cargo."""
import flet as ft

from app.view.componentes import cabecera


class SupervisorView:
    def __init__(self, controller):
        self.c = controller

    def construir(self) -> ft.Control:
        u = self.c.usuario
        filas = [ft.DataRow(cells=[ft.DataCell(ft.Text(f"{r['nombre']} {r['apellidos']}")), ft.DataCell(ft.Text(r["dni"])),
                                   ft.DataCell(ft.Text(r["telefono"])), ft.DataCell(ft.Text(r.get("direccion", "")))])
                 for r in self.c.repo.residentes_de(u)]
        tabla = ft.DataTable(columns=[ft.DataColumn(ft.Text(t)) for t in ("Residente", "DNI", "Teléfono", "Dirección")], rows=filas)
        return ft.Column([
            cabecera("Viviendas supervisadas", u, self.c.ir_login),
            ft.Container(padding=20, content=ft.Column([ft.Text(f"{len(filas)} residentes a tu cargo"), ft.Row([tabla], scroll=ft.ScrollMode.AUTO)])),
            # TODO Sprint 2: detalle de residente con sus sensores y notas
        ], expand=True)
