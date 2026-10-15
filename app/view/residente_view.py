"""Vista del residente: valor actual de sus sensores."""
import flet as ft

from app.view.componentes import cabecera, tarjeta

NOMBRES = {"temperatura_humedad": "Temperatura y humedad", "co2": "Calidad del aire (CO₂)", "consumo": "Consumo eléctrico"}


class ResidenteView:
    def __init__(self, controller):
        self.c = controller

    def construir(self) -> ft.Control:
        u = self.c.usuario
        tarjetas = []
        for s in self.c.repo.sensores_de(u["id"]):
            medidas = self.c.repo.medidas_de(s["id"])
            if not medidas:
                continue
            ultima = medidas[-1]["valores"]
            valor = " · ".join(f"{v:g} {un}" for v, un in zip(ultima, s["unidades"]))
            tarjetas.append(tarjeta(f"{NOMBRES[s['tipo']]} · {s['ubicacion']}", valor))
        return ft.Column([
            cabecera("Mi vivienda", u, self.c.ir_login),
            ft.Container(padding=20, content=ft.Column([
                ft.Text(u.get("direccion", ""), color="#5E7180"),
                ft.Row(tarjetas, wrap=True, spacing=16, run_spacing=16),
                # TODO Sprint 2: gráfica histórica (al menos 3 días) y alertas
            ], spacing=16)),
        ], expand=True)
