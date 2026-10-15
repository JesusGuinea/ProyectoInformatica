"""Punto de entrada de Ágora Hábitat. Ejecutar desde PyCharm o con: python main.py"""
import flet as ft

from app.controller.app_controller import AppController


def main(page: ft.Page):
    page.title = "Ágora Hábitat"
    page.padding = 0
    page.bgcolor = "#FBF8F1"
    AppController(page).ir_login()


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
