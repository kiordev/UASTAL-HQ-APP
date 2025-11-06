import flet as ft
from ASSETS import design as ds
from UI import vat, address, docs, scripts

def main(page: ft.Page):
    page.title = "UASTAL HQ build 0.9"
    page.bgcolor = "#090040"
    page.window.resizable = False
    page.window.width = 380
    page.window.height = 530
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    body = ft.Container()

    def on_nav_change(e):
        selected = e.control.selected_index
        if selected == 0:
            body.content = vat.view()
        elif selected == 1:
            body.content = address.view()
        elif selected == 2:
            body.content = docs.view()
        elif selected == 3:
            body.content = scripts.view()
        page.update()

    page.navigation_bar = ft.NavigationBar(
        on_change=on_nav_change,
        bgcolor=ds.light,
        indicator_color=ds.accent,
        overlay_color=ds.accent_light,
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.ATTACH_MONEY, label="ПДВ"),
            ft.NavigationBarDestination(icon=ft.Icons.EXPLORE, label="Адреси"),
            ft.NavigationBarDestination(icon=ft.Icons.FILE_PRESENT_ROUNDED, label="Документи"),
            ft.NavigationBarDestination(icon=ft.Icons.DESCRIPTION, selected_icon=ft.Icons.BOOKMARK, label="Скрипти"),
        ]
    )

    body.content = vat.view()
    page.add(body)

ft.app(target=main)
