"""Vista de inicio de sesión."""
import flet as ft

from app.view.componentes import ESPUMA, OCEANO


class LoginView:
    def __init__(self, controller):
        self.c = controller

    def construir(self) -> ft.Control:
        usuario = ft.TextField(label="Correo electrónico o DNI", width=360)
        clave = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=360)
        error = ft.Text("", color="red")

        def entrar(_):
            try:
                self.c.entrar(usuario.value or "", clave.value or "")
            except ValueError as e:
                error.value = str(e)
                self.c.page.update()

        return ft.Container(
            bgcolor=ESPUMA, expand=True, alignment=ft.Alignment.CENTER,
            content=ft.Column(
                [ft.Image(src="logo.png", width=90, height=90),
                 ft.Text("Ágora Hábitat", size=28, weight=ft.FontWeight.BOLD, color=OCEANO),
                 ft.Text("Iniciar sesión", size=18), usuario, clave, error,
                 ft.Button("Entrar", on_click=entrar, width=360, bgcolor=OCEANO, color="white"),
                 ft.TextButton("¿No tienes cuenta? Regístrate", on_click=self.c.ir_registro)],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER, tight=True,
            ),
        )
