"""Validaciones de datos de usuario."""
import re

LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"


def dni_valido(dni: str) -> bool:
    dni = dni.strip().upper()
    return bool(re.fullmatch(r"\d{8}[A-Z]", dni)) and LETRAS_DNI[int(dni[:8]) % 23] == dni[8]


def telefono_valido(telefono: str) -> bool:
    return bool(re.fullmatch(r"\d{9}", telefono.replace(" ", "")))


def correo_valido(correo: str) -> bool:
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[a-z]{2,}", correo.strip().lower()))
