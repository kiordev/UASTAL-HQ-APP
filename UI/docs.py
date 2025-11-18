import flet as ft
import base64
import os
import sys
from ASSETS import design as ds

# ФУНКЦИЯ ДЛЯ ПОДГРУЗКИ ФАЙЛОВ ВО ВРЕМЯ БИЛДА ПРОЕКТА
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# ФАЙЛИ
FILES = [
    ("Реквизиты.docx", "docs/requsits.docx"),
    ("Выписка.pdf", "docs/vypyska.pdf"),
    ("Вытяг.pdf", "docs/Vytag.pdf"),
]

# ФУНКЦИЯ ДЛЯ СОХРАНЕНИЯ ФАЙЛОВ НА РАБОЧИЙ СТОЛ
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

#IBANS
IBAN_SOBCHENKO_text = "UA473348510000000026008296939"
IBAN_VALIK_text = "UA573052990000026000026205280"

#ЄДРПОУ
EDRP_SOBCHENKO_text = "3342305349"
EDRP_STOROZHUK_text = "32849298"

# ФУНКЦИИ ДЛЯ КНОПОК
def copy_iban_sobchenko(e):
        e.page.set_clipboard(IBAN_SOBCHENKO_text)
        e.page.update()

def copy_iban_valik(e):
        e.page.set_clipboard(IBAN_VALIK_text)
        e.page.update()

def copy_edrp_sobchenko(e):
        e.page.set_clipboard(EDRP_SOBCHENKO_text)
        e.page.update()

def copy_edrp_storozhuk(e):
        e.page.set_clipboard(EDRP_STOROZHUK_text)
        e.page.update()


# РАЗМЕРЫ ВИДЖЕТОВ НА СТРАНИЦЕ
H_text_size = 14 # РАЗМЕР ЗАГОЛОВКОВ
documents_button_height = 25 # ШИРИНА КНОПОК
documents_button_width = 130 # ВЫСОТА КНОПОК

def view():
    def save_file(filename):
        def handler(e):
            path = save_file_to_desktop(filename, DOCS_B64[filename])
            e.page.update()
        return handler

    # ДОКУМЕНТИ --- ФАЙЛЫ СТОРОЖУК
    docsText = ft.Text(
        value="ДОКУМЕНТИ СТОРОЖУК:",
        width=200,
        color=ds.accent,
        size=H_text_size,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    reqButton = ft.ElevatedButton(
        "РЕКВІЗИТИ",
        width=documents_button_width,
        height=documents_button_height,
        on_click=save_file("Реквизиты.docx"),
        bgcolor=ds.light,
        color=ds.white,
    )
    vypButton = ft.ElevatedButton(
        "ВИПИСКА",
        width=documents_button_width,
        height=documents_button_height,
        on_click=save_file("Выписка.pdf"),
        bgcolor=ds.light,
        color=ds.white,
    )
    vytButton = ft.ElevatedButton(
        "ВИТЯГ",
        width=documents_button_width,
        height=documents_button_height,
        on_click=save_file("Вытяг.pdf"),
        bgcolor=ds.light,
        color=ds.white,
    )

    storozhukColumn = ft.Column([
        docsText, reqButton, vypButton, vytButton], 
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    # ДОКУМЕНТИ --- IBAN
    ibanText = ft.Text(
        value="КОДИ IBAN:",
        width=200,
        color=ds.accent,
        size=H_text_size,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    ibanSOBCHENKOButton = ft.ElevatedButton(
        "ФОП СОБЧЕНКО",
        width=documents_button_width,
        height=documents_button_height,
        on_click=copy_iban_sobchenko,
        bgcolor=ds.light,
        color=ds.white,
    )

    ibanValikButton = ft.ElevatedButton(
        "ФОП ВАЛІК",
        width=documents_button_width,
        height=documents_button_height,
        on_click=copy_iban_valik,
        bgcolor=ds.light,
        color=ds.white,
    )

    IBANColumn = ft.Column([
        ibanText, ibanSOBCHENKOButton, ibanValikButton], 
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    # ДОКУМЕНТИ --- РЕЗЕРВ
    reserveText = ft.Text(
        value="РЕЗЕРВНА КОЛОНКА:",
        width=200,
        color=ds.accent,
        size=H_text_size,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    ReserveColumn = ft.Column([
        reserveText],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    # ДОКУМЕНТИ --- ЭДРПОУ
    edprText = ft.Text(
        value="КОДИ ЭДРПОУ:",
        width=200,
        color=ds.accent,
        size=H_text_size,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    edrpSOBCHENKOButton = ft.ElevatedButton(
        "ФОП СОБЧЕНКО",
        width=documents_button_width,
        height=documents_button_height,
        on_click=copy_edrp_sobchenko,
        bgcolor=ds.light,
        color=ds.white,
    )

    edrpSTOROZHUKButton = ft.ElevatedButton(
        "ТОВ СТОРОЖУК",
        width=documents_button_width,
        height=documents_button_height,
        on_click=copy_edrp_storozhuk,
        bgcolor=ds.light,
        color=ds.white,
    )

    EDRPColumn = ft.Column([
        edprText, edrpSOBCHENKOButton, edrpSTOROZHUKButton],
        alignment=ft.MainAxisAlignment.START, 
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    
    # STOROZHUK + RESERVE
    FirstRow = ft.Row(
         [storozhukColumn, ReserveColumn], 
         alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    
    #IBAN + EDRP
    SecondRow = ft.Row(
         [IBANColumn, EDRPColumn], 
         alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    return ft.Column(
        [FirstRow, SecondRow],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )