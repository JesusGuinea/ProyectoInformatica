"""Vista de registro de usuario."""
import flet as ft

from app.view.componentes import ESPUMA, OCEANO


class RegistroView:
    def __init__(self, controller):
        self.c = controller

    def construir(self) -> ft.Control:
        rol = ft.Dropdown(label="Tipo de usuario", width=360, value="residente",
                          options=[ft.dropdown.Option("residente", "Residente"), ft.dropdown.Option("supervisor", "Supervisor"),
                                   ft.dropdown.Option("analista", "Analista")])
        campos = {k: ft.TextField(label=l, width=360) for k, l in [
            ("nombre", "Nombre"), ("apellidos", "Apellidos"), ("dni", "DNI (8 números y letra)"),
            ("telefono", "Teléfono (9 cifras)"), ("correo", "Correo electrónico")]}
        clave = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=360)
        mensaje = ft.Text("")

        def registrar(_):
            try:
                self.c.auth.registrar(rol.value, *(campos[k].value or "" for k in campos), clave.value or "")
                mensaje.value, mensaje.color = "Cuenta creada. Ya puedes iniciar sesión.", "green"
            except ValueError as e:
                mensaje.value, mensaje.color = str(e), "red"
            self.c.page.update()

        return ft.Container(
            bgcolor=ESPUMA, expand=True, alignment=ft.Alignment.CENTER,
            content=ft.Column(
                [ft.Text("Crear cuenta", size=26, weight=ft.FontWeight.BOLD, color=OCEANO), rol, *campos.values(), clave, mensaje,
                 ft.Button("Crear cuenta", on_click=registrar, width=360, bgcolor=OCEANO, color="white"),
                 ft.TextButton("Volver al inicio de sesión", on_click=self.c.ir_login)],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, scroll=ft.ScrollMode.AUTO, tight=True,
            ),
        )
