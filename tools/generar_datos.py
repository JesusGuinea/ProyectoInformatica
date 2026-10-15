"""Genera los ficheros JSON de prueba en data/ con datos realistas.

Uso (desde la raíz del proyecto): python tools/generar_datos.py
"""
import hashlib
import json
import math
import random
from datetime import datetime, timedelta
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data"
random.seed(14)

LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"


def dni(numero: int) -> str:
    return f"{numero:08d}{LETRAS[numero % 23]}"


def clave(texto: str) -> str:
    return hashlib.sha256(texto.encode()).hexdigest()


RESIDENTES = [
    ("Lucía", "Fernández Ortega", "A", "2.º B"), ("Antonio", "García Ruiz", "A", "3.º A"),
    ("Carmen", "López Serrano", "B", "1.º C"), ("Manuel", "Jiménez Torres", "B", "4.º A"),
    ("Rosa", "Martín Delgado", "C", "Bajo B"), ("Francisco", "Navarro Gil", "C", "2.º A"),
    ("Isabel", "Romero Castro", "A", "1.º A"), ("José", "Vázquez Molina", "B", "3.º B"),
    ("Pilar", "Sánchez Ramos", "C", "4.º C"),
]
SUPERVISORES = [
    ("Javier", "Morales Peña", "Administrador de comunidad"), ("Marta", "Fernández Gil", "Familiar"),
    ("Pilar", "Jiménez Ortiz", "Familiar"), ("Raúl", "Domínguez Vera", "Administrador de comunidad"),
]
ANALISTAS = [("Elena", "Ruiz Campos", "Técnica ambiental"), ("Sergio", "Herrera Prieto", "Técnico de eficiencia energética")]


def telefono() -> str:
    return random.choice("67") + "".join(random.choice("0123456789") for _ in range(8))


def correo(nombre: str, apellidos: str) -> str:
    base = f"{nombre[0]}.{apellidos.split()[0]}".lower()
    for a, b in zip("áéíóúñ", "aeioun"):
        base = base.replace(a, b)
    return base + "@correo.es"


usuarios = []
n = 30000000
for i, (nom, ape, bloque, piso) in enumerate(RESIDENTES, 1):
    n += random.randint(100000, 3000000)
    usuarios.append({"id": f"R{i:02d}", "rol": "residente", "nombre": nom, "apellidos": ape, "dni": dni(n),
                     "telefono": telefono(), "correo": correo(nom, ape), "clave": clave("agora123"),
                     "direccion": f"Paseo Marítimo 14, Bloque {bloque}, {piso}, 11010 Cádiz",
                     "supervisores": [], "analista": None})
for i, (nom, ape, tipo) in enumerate(SUPERVISORES, 1):
    n += random.randint(100000, 3000000)
    usuarios.append({"id": f"S{i:02d}", "rol": "supervisor", "tipo": tipo, "nombre": nom, "apellidos": ape,
                     "dni": dni(n), "telefono": telefono(), "correo": correo(nom, ape), "clave": clave("agora123")})
for i, (nom, ape, tipo) in enumerate(ANALISTAS, 1):
    n += random.randint(100000, 3000000)
    usuarios.append({"id": f"A{i:02d}", "rol": "analista", "tipo": tipo, "nombre": nom, "apellidos": ape,
                     "dni": dni(n), "telefono": telefono(), "correo": correo(nom, ape), "clave": clave("agora123")})

res = {u["id"]: u for u in usuarios if u["rol"] == "residente"}
# Supervisores: S01 tiene varios residentes; R01 y R04 tienen más de un supervisor.
asignacion = {"R01": ["S01", "S02"], "R02": ["S01"], "R03": ["S04"], "R04": ["S01", "S03"], "R05": ["S04"],
              "R06": ["S01"], "R07": ["S04"], "R08": ["S04"], "R09": ["S04"]}
for rid, sups in asignacion.items():
    res[rid]["supervisores"] = sups
    res[rid]["analista"] = "A01" if int(rid[1:]) % 2 else "A02"

TIPOS = {
    "temperatura_humedad": {"unidades": ["°C", "% HR"], "base": [21.5, 66], "amp": [2.0, 8]},
    "co2": {"unidades": ["ppm"], "base": [750], "amp": [260]},
    "consumo": {"unidades": ["kWh"], "base": [0.28], "amp": [0.18]},
}
sensores, medidas = [], []
inicio = datetime(2026, 10, 8)
k = 0
for rid in res:
    for tipo, cfg in TIPOS.items():
        k += 1
        sid = f"SEN{k:03d}"
        sensores.append({"id": sid, "tipo": tipo, "residente": rid, "ubicacion": random.choice(["Salón", "Dormitorio", "Cocina"]),
                         "unidades": cfg["unidades"]})
        # 4 días de medidas, una cada 2 horas
        for h in range(0, 24 * 4, 2):
            t = inicio + timedelta(hours=h)
            ciclo = math.sin((t.hour - 6) / 24 * 2 * math.pi)
            valores = [round(b + a * ciclo + random.uniform(-a, a) * 0.15, 2) for b, a in zip(cfg["base"], cfg["amp"])]
            medidas.append({"sensor": sid, "fecha": t.isoformat(timespec="minutes"), "valores": valores})

for nombre, datos in [("usuarios", usuarios), ("sensores", sensores), ("medidas", medidas), ("sugerencias", [])]:
    (DATA / f"{nombre}.json").write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"{len(usuarios)} usuarios, {len(sensores)} sensores, {len(medidas)} medidas")
