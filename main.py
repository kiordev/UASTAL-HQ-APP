import flet as ft
from ASSETS import design as ds
from UI import vat, address, docs


def main(page: ft.Page):

    # PAGE SETTINGS - title
    page.title = "UASTAL HQ build 0.5"

    # PAGE SETTINGS - background color
    page.bgcolor = "#090040"

    # PAGE SETTINGS - size
    page.window.resizable = False
    page.window.width = 380
    page.window.height = 530

    # PAGE SETTINGS - aligment
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # MAIN UI
    body = ft.Container()

    # NAVIGATION FUNTION
    def on_nav_change(e):
        selected = e.control.selected_index
        if selected == 0:
            body.content = vat.view()
        elif selected == 1:
            body.content = address.view()
        elif selected == 2:
            body.content = docs.view()
        elif selected == 3:
            body.content = ft.Text("Скрипти (в разработке)", color=ds.accent)
        page.update()

    # PAGE NAVIGATION
    page.navigation_bar = ft.NavigationBar(
        on_change=on_nav_change,
        bgcolor=ds.light,
        indicator_color=ds.accent,
        overlay_color=ds.accent_light,
        destinations=[
            # Navigation to VAT
            ft.NavigationBarDestination
            (
                icon=ft.Icons.ATTACH_MONEY, 
                label="ПДВ",
            ),

            # Navigation to ADRESS
            ft.NavigationBarDestination
            (
                icon=ft.Icons.EXPLORE, 
                label="Адреси",
            ),

            # Navigation to DOCS
            ft.NavigationBarDestination
            (
                icon=ft.Icons.FILE_PRESENT_ROUNDED, 
                label="Документи"
            ),

            # Navigation to SCRIPTS
            ft.NavigationBarDestination
            (
                icon=ft.Icons.DESCRIPTION,
                selected_icon=ft.Icons.BOOKMARK,
                label="Скрипти",
            ),
        ]
    )

    # По умолчанию — вкладка VAT
    
    body.content = vat.view()

    
    page.add(body)

ft.app(target=main)