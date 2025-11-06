import sys, os
import flet as ft
from ASSETS import design as ds

def view():
    office_NP_Text = ft.Text(
        value="Адреса Нової Пошти:",
        width=200,
        color=ds.white,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    office_NP_Address = ft.TextField(
        width=290,
        bgcolor=ds.white,
        read_only=True,
        value="ТОВ СТОРОЖУК, 32849298, Київ, НП 193",
        text_size=14
    )
    office_Text = ft.Text(
        value="Адреса офісу:",
        width=200,
        color=ds.white,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    office_Address = ft.TextField(
        width=290,
        bgcolor=ds.white,
        read_only=True,
        value="м.Дарниця, провулок Будівельників 18",
        text_size=14
    )
    repair_Text = ft.Text(
        value="Адреса на ремонт:",
        width=200,
        color=ds.white,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    repair_Address = ft.TextField(
        width=290,
        bgcolor=ds.white,
        read_only=True,
        value="с.Красилівка, Нова Пошта №1",
        text_size=14
    )
    sand_Text = ft.Text(
        value="Юр.адреса піску:",
        width=200,
        color=ds.white,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    sand_Address = ft.TextField(
        width=290,
        bgcolor=ds.white,
        read_only=True,
        value="провулок Промисловий, буд.2 с.Красилівка, Броварський район, Київська область",
        text_size=14
    )
    return ft.Container(
        content=ft.Column(
            [
                office_NP_Text, office_NP_Address,
                office_Text, office_Address,
                repair_Text, repair_Address,
                sand_Text, sand_Address
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        padding=20,
        bgcolor=ds.dark,
        shadow=ft.BoxShadow(blur_radius=15, color=ft.colors.BLACK26, spread_radius=1),
        alignment=ft.alignment.center,
    )
