import flet as ft
import base64
import os
import sys
from ASSETS import design as ds

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

FILES = [
    ("Реквизиты.docx", "docs/requsits.docx"),
    ("Выписка.pdf", "docs/vypyska.pdf"),
    ("Вытяг.pdf", "docs/Vytag.pdf"),
]

def load_base64(filepath):
    with open(resource_path(filepath), "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

DOCS_B64 = {name: load_base64(path) for name, path in FILES}

def save_file_to_desktop(filename, b64str):
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    full_path = os.path.join(desktop, filename)
    with open(full_path, "wb") as f:
        f.write(base64.b64decode(b64str))
    return full_path

def view():
    def save_file(filename):
        def handler(e):
            path = save_file_to_desktop(filename, DOCS_B64[filename])
            e.page.update()
        return handler

    docsText = ft.Text(
        value="ДОКУМЕНТИ:",
        width=200,
        color=ds.white,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    reqButton = ft.ElevatedButton(
        "ЗАВАНТАЖИТИ РЕКВІЗИТИ",
        width=230,
        height=30,
        on_click=save_file("Реквизиты.docx"),
    )
    vypButton = ft.ElevatedButton(
        "ЗАВАНТАЖИТИ ВИПИСКУ",
        width=230,
        height=30,
        on_click=save_file("Выписка.pdf"),
    )
    vytButton = ft.ElevatedButton(
        "ЗАВАНТАЖИТИ ВИТЯГ",
        width=230,
        height=30,
        on_click=save_file("Вытяг.pdf"),
    )
    return ft.Column(
        [docsText, reqButton, vypButton, vytButton],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )
