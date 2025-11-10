import sys, os, subprocess
import flet as ft
from ASSETS import design as ds

def save_theme_and_restart(theme_name):
    from ASSETS import design as ds
    # Сохраняем выбранную тему в файл
    with open(ds.SETTINGS_FILE, "w") as f:
        f.write(theme_name)
    # Корректно перезапускаем приложение
    if getattr(sys, 'frozen', False):  # Программа собрана в exe (PyInstaller)
        # Запускаем новый exe-процесс
        subprocess.Popen([sys.executable])
    else:
        # Обычный python-скрипт
        subprocess.Popen([sys.executable] + sys.argv)
    sys.exit(0)  # Завершаем текущий процесс, чтобы не было двойных окон

def view():

    settingsText = ft.Text(
        value="ОБРАТИ ТЕМУ:",
        width=200,
        color=ds.accent,
        size=25,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    themeDropdown = ft.Dropdown(
        options=[ft.dropdown.Option(name) for name in ds.THEME_MAP.keys()],
        value=ds.current_theme_name,
        width=300,
        bgcolor=ds.white,
        border=ds.white,
        color=ds.white

    )

    apply_button = ft.ElevatedButton(
        text="ЗБЕРЕГТИ ЗМІНИ",
        bgcolor=ds.light,
        color=ds.white,
        width=200,
        on_click=lambda e: save_theme_and_restart(themeDropdown.value)
    )

    return ft.Container(
        content=ft.Column(
            [
                settingsText, 
                themeDropdown,  # dropdown выбора темы
                apply_button,   # кнопка применить
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        ),
        padding=20,
        bgcolor=ds.dark,
        alignment=ft.alignment.center,
    )
