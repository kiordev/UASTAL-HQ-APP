import sys, os
import flet as ft
from ASSETS import design as ds

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def view():
    # 🟡 не создаём page, просто возвращаем контейнер 

    click_audio = ft.Audio(
        src=resource_path("ASSETS/click.mp3"),
        autoplay=False
    )

    def play_sound():
        click_audio.play()
        click_audio.update()

    def spin_logo_plus(e=None):
        logo.rotate.angle += 12.56
        logo.update()

    def spin_logo_minus(e=None):
        logo.rotate.angle -= 12.56
        logo.update()

    def calculate_without_vat(e):
        play_sound()
        try:
            value = float(input_box.value)
            result = value / 1.2
            output.value = f"{result:.2f}"
        except Exception:
            output.value = "Помилка!"
        spin_logo_minus()
        output.update()

    def calculate_with_vat(e):
        play_sound()
        try:
            value = float(input_box.value)
            result = value * 1.2
            output.value = f"{result:.2f}"
        except Exception:
            output.value = "Помилка!"
        spin_logo_plus()
        output.update()

    input_box = ft.TextField(
        width=250,
        bgcolor=ds.white,
        text_style=ft.TextStyle(color=ft.colors.BLACK87),
        on_submit=calculate_without_vat
    )
    calc_button_no_vat = ft.ElevatedButton(
        text="ВИДАЛИТИ ПДВ",
        bgcolor=ds.semi,
        color=ds.white,
        on_click=calculate_without_vat,
    )
    calc_button_with_vat = ft.ElevatedButton(
        text="ДОДАТИ ПДВ",
        bgcolor=ds.light,
        color=ds.white,
        on_click=calculate_with_vat,
    )
    output = ft.Text(
        value="",
        width=200,
        color=ds.accent,
        size=22,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    logo = ft.Image(
        src=resource_path("ASSETS/vatPopuga.png"),
        width=80,
        height=80,
        fit=ft.ImageFit.CONTAIN,
        rotate=ft.Rotate(angle=0),
        animate_rotation=ft.Animation(duration=500, curve=ft.AnimationCurve.LINEAR)
    )
    title = ft.Text(
        "AMAZON PARROT ANDREW",
        size=18,
        weight=ft.FontWeight.BOLD,
        color=ds.accent,
    )

    # Возвращаем контейнер, добавляем аудио!
    return ft.Container(
        content=ft.Column(
            [
                logo,
                title,
                input_box,
                ft.Row(
                    [calc_button_no_vat, calc_button_with_vat],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                output,
                click_audio,  # аудио-компонент должен быть в дереве!
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        padding=20,
        bgcolor=ds.dark,
        alignment=ft.alignment.center,
    )