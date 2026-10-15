"""Controlador de acceso: inicio de sesión y registro."""
from app.model.repositorio import Repositorio, hash_clave
from app.model.validacion import correo_valido, dni_valido, telefono_valido


class AuthController:
    def __init__(self, repo: Repositorio):
        self.repo = repo

    def login(self, correo_o_dni: str, clave: str) -> dict:
        usuario = self.repo.buscar_usuario(correo_o_dni)
        if not usuario or usuario["clave"] != hash_clave(clave):
            raise ValueError("Correo, DNI o contraseña incorrectos.")
        return usuario

    def registrar(self, rol: str, nombre: str, apellidos: str, dni: str, telefono: str, correo: str, clave: str) -> dict:
        if not all([nombre, apellidos, dni, telefono, correo, clave]):
            raise ValueError("Rellena todos los campos.")
        if not dni_valido(dni):
            raise ValueError("El DNI debe tener 8 números y una letra correcta.")
        if not telefono_valido(telefono):
            raise ValueError("El teléfono debe tener 9 cifras.")
        if not correo_valido(correo):
            raise ValueError("El correo no es válido.")
        if self.repo.buscar_usuario(correo) or self.repo.buscar_usuario(dni):
            raise ValueError("Ya existe un usuario con ese correo o DNI.")
        usuario = {"id": self.repo.siguiente_id(rol), "rol": rol, "nombre": nombre.strip(), "apellidos": apellidos.strip(),
                   "dni": dni.strip().upper(), "telefono": telefono.replace(" ", ""), "correo": correo.strip().lower(),
                   "clave": hash_clave(clave)}
        if rol == "residente":
            usuario.update({"direccion": "", "supervisores": [], "analista": None})
        self.repo.anadir_usuario(usuario)
        return usuario
