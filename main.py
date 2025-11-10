#Команда для билда pyinstaller main.py --windowed --add-data "ASSETS;ASSETS" --add-data "docs;docs" --icon ASSETS/icon.png
import sys, os
import flet as ft
from ASSETS import design as ds
from UI import vat, address, docs, scripts, settings

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def main(page: ft.Page):
    page.title = "UASTAL TECH HQ BUILD 1.3.5"
    page.window.resizable = False
    page.bgcolor = ds.dark
    page.window.width = 430
    page.window.height = 580
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    click_audio = ft.Audio(
        src=resource_path("ASSETS/navSound.mp3"),
        autoplay=False
    )

    def play_sound():
        click_audio.play()
        click_audio.update()

    body = ft.Container()

    def on_nav_change(e):
        selected = e.control.selected_index
        play_sound()
        if selected == 0:
            body.content = vat.view()
        elif selected == 1:
            body.content = address.view()
        elif selected == 2:
            body.content = docs.view()
        elif selected == 3:
            body.content = scripts.view()
        elif selected == 4:
            body.content = settings.view()
        page.update()

    page.navigation_bar = ft.NavigationBar(
        on_change=on_nav_change,
        bgcolor=ds.navigationbar,
        indicator_color=ds.accent,
        overlay_color=ds.accent_light,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.ATTACH_MONEY, label="ПДВ"),
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Адреси"),
            ft.NavigationBarDestination(icon=ft.Icons.FILE_PRESENT_ROUNDED, label="Документи"),
            ft.NavigationBarDestination(icon=ft.Icons.DESCRIPTION, label="Скрипти"),
            ft.NavigationBarDestination(icon=ft.Icons.COLOR_LENS_OUTLINED, label="Параметри"),
        ]
    )

    body.content = vat.view()
    page.add(body, click_audio)

ft.app(target=main)