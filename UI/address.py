import sys, os, json
import flet as ft
from ASSETS import design as ds

def resource_path(relative_path):
    # PyInstaller
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Путь к дефолтному JSON как части сборки
DEFAULT_JSON = resource_path(os.path.join("ASSETS", "address_data.json"))

# Путь для сохранения пользовательских данных (в profile пользователя)
USER_JSON = os.path.join(os.path.expanduser("~"), "address_data_user.json")

def load_data():
    # Если пользовательский файл существует — используем его
    if os.path.exists(USER_JSON):
        with open(USER_JSON, encoding="utf-8") as f:
            return json.load(f)
    # Иначе — берем дефолтный из папки с exe 
    if os.path.exists(DEFAULT_JSON):
        with open(DEFAULT_JSON, encoding="utf-8") as f:
            return json.load(f)
    # Если нет ни одного — дефолтные пустые
    return {
        "office_np": "",
        "office": "",
        "repair": "",
        "sand": ""
    }

def save_data(data):
    # ВСЕГДА сохраняем только в user-json!
    with open(USER_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def view():
    # Загружаем значения
    data = load_data()

    office_NP_Text = ft.Text(
        value="НОВА ПОШТА ОФІСУ:",
        width=200,
        color=ds.accent,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    office_NP_Address = ft.TextField(
        width=290,
        bgcolor=ds.white,
        value=data["office_np"],
        text_size=14
    )
    def save_np(e):
        data["office_np"] = office_NP_Address.value
        save_data(data)

    office_NP_EditButton = ft.IconButton(
        icon=ft.Icons.EDIT,
        icon_color=ds.accent,
        icon_size=30,
        on_click=save_np
    )
    office_NP_Row = ft.Row(
        [office_NP_Address, office_NP_EditButton],
        alignment=ft.MainAxisAlignment.CENTER
    )

    office_Text = ft.Text(
        value="АДРЕСА ОФІСУ:",
        width=200,
        color=ds.accent,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    office_Address = ft.TextField(
        width=290,
        bgcolor=ds.white,
        value=data["office"],
        text_size=14
    )
    def save_office(e):
        data["office"] = office_Address.value
        save_data(data)

    office_EditButton = ft.IconButton(
        icon=ft.Icons.EDIT,
        icon_color=ds.accent,
        icon_size=30,
        on_click=save_office
    )
    office_Row = ft.Row(
        [office_Address, office_EditButton],
        alignment=ft.MainAxisAlignment.CENTER
    )

    repair_Text = ft.Text(
        value="АДРЕСА НА РЕМОНТ",
        width=200,
        color=ds.accent,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    repair_Address = ft.TextField(
        width=290,
        bgcolor=ds.white,
        value=data["repair"],
        text_size=14
    )
    def save_repair(e):
        data["repair"] = repair_Address.value
        save_data(data)
    repair_EditButton = ft.IconButton(
        icon=ft.Icons.EDIT,
        icon_color=ds.accent,
        icon_size=30,
        on_click=save_repair
    )
    repair_Row = ft.Row(
        [repair_Address, repair_EditButton],
        alignment=ft.MainAxisAlignment.CENTER
    )

    sand_Text = ft.Text(
        value="ЮР.АДРЕСА ПІСКУ",
        width=200,
        color=ds.accent,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    sand_Address = ft.TextField(
        width=290,
        bgcolor=ds.white,
        value=data["sand"],
        text_size=14
    )
    def save_sand(e):
        data["sand"] = sand_Address.value
        save_data(data)
    sand_EditButton = ft.IconButton(
        icon=ft.Icons.EDIT,
        icon_color=ds.accent,
        icon_size=30,
        on_click=save_sand
    )
    sand_Row = ft.Row(
        [sand_Address, sand_EditButton],
        alignment=ft.MainAxisAlignment.CENTER
    )

    return ft.Container(
        content=ft.Column(
            [
                office_NP_Text, office_NP_Row,
                office_Text, office_Row,
                repair_Text, repair_Row,
                sand_Text, sand_Row
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        padding=20,
        bgcolor=ds.dark,
        alignment=ft.alignment.center,
    )
