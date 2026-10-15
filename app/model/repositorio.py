"""Modelo: lectura y escritura de los ficheros JSON de data/ con rutas relativas al proyecto."""
import hashlib
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
DATA = RAIZ / "data"


def _leer(nombre: str) -> list:
    return json.loads((DATA / f"{nombre}.json").read_text(encoding="utf-8"))


def _guardar(nombre: str, datos: list) -> None:
    (DATA / f"{nombre}.json").write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")


def hash_clave(clave: str) -> str:
    return hashlib.sha256(clave.encode()).hexdigest()


class Repositorio:
    def usuarios(self) -> list[dict]:
        return _leer("usuarios")

    def buscar_usuario(self, correo_o_dni: str) -> dict | None:
        valor = correo_o_dni.strip().lower()
        return next((u for u in self.usuarios() if valor in (u["correo"].lower(), u["dni"].lower())), None)

    def usuario(self, uid: str) -> dict | None:
        return next((u for u in self.usuarios() if u["id"] == uid), None)

    def anadir_usuario(self, usuario: dict) -> None:
        datos = self.usuarios()
        datos.append(usuario)
        _guardar("usuarios", datos)

    def siguiente_id(self, rol: str) -> str:
        prefijo = {"residente": "R", "supervisor": "S", "analista": "A"}[rol]
        ids = [int(u["id"][1:]) for u in self.usuarios() if u["id"].startswith(prefijo)]
        return f"{prefijo}{max(ids, default=0) + 1:02d}"

    def residentes_de(self, usuario: dict) -> list[dict]:
        """Residentes que supervisa o analiza un usuario."""
        campo = "supervisores" if usuario["rol"] == "supervisor" else "analista"
        res = [u for u in self.usuarios() if u["rol"] == "residente"]
        if campo == "supervisores":
            return [r for r in res if usuario["id"] in r.get("supervisores", [])]
        return [r for r in res if r.get("analista") == usuario["id"]]

    def sensores_de(self, residente_id: str) -> list[dict]:
        return [s for s in _leer("sensores") if s["residente"] == residente_id]

    def medidas_de(self, sensor_id: str) -> list[dict]:
        return sorted((m for m in _leer("medidas") if m["sensor"] == sensor_id), key=lambda m: m["fecha"])

    def anadir_sugerencia(self, sugerencia: dict) -> None:
        datos = _leer("sugerencias")
        datos.append(sugerencia)
        _guardar("sugerencias", datos)
