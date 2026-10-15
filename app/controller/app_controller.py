"""Controlador principal: navegación entre vistas según el rol."""
import flet as ft

from app.controller.auth_controller import AuthController
from app.model.repositorio import Repositorio
from app.view.analista_view import AnalistaView
from app.view.login_view import LoginView
from app.view.registro_view import RegistroView
from app.view.residente_view import ResidenteView
from app.view.supervisor_view import SupervisorView

VISTAS_POR_ROL = {"residente": ResidenteView, "supervisor": SupervisorView, "analista": AnalistaView}


class AppController:
    def __init__(self, page: ft.Page):
        self.page = page
        self.repo = Repositorio()
        self.auth = AuthController(self.repo)
        self.usuario = None

    def mostrar(self, control: ft.Control) -> None:
        self.page.controls.clear()
        self.page.add(control)

    def ir_login(self, _=None) -> None:
        self.usuario = None
        self.mostrar(LoginView(self).construir())

    def ir_registro(self, _=None) -> None:
        self.mostrar(RegistroView(self).construir())

    def entrar(self, correo_o_dni: str, clave: str) -> None:
        self.usuario = self.auth.login(correo_o_dni, clave)
        self.ir_inicio()

    def ir_inicio(self) -> None:
        vista = VISTAS_POR_ROL[self.usuario["rol"]](self)
        self.mostrar(vista.construir())
