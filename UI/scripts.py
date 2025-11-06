import flet as ft
from ASSETS import design as ds

def view():
    emitter_text = (
        "Надішліть фото або відео поломки, що саме не працює. Це інформація піде в інженерний відділ.\n\n"
        "Якщо ми беремо в роботу, то випромінювач проходить обов’язкову діагностику незалежно від того, що вказано у якості поломки.\n\n"
        "Ми встановлюємо всі причини поломки, якщо такі наявні, і прораховуємо вартість ремонту. Після цього надсилаємо вам суму та список робіт, які будуть проведені.\n\n"
        "Якщо ви погоджуєте ремонт, то діагностика входить у вартість ремонту, якщо ні - вам потрібно буде оплатити діагностику.\n\n"
        "Беремо випромінювач в ремонт після вашої письмової згоди на проведення ремонтних робіт.\n\n"
        "Вартості вказані нижче:"
    )
    def copy_emitter(e):
        e.page.set_clipboard(emitter_text)
        e.page.update()
    scriptsText = ft.Text(
        value="КОПІЮВАТИ СКРИПТ:",
        width=200,
        color=ds.white,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    emitterButton = ft.ElevatedButton(
        "ВИПРОМІНЮВАЧ",
        width=230,
        height=30,
        on_click=copy_emitter,
    )
    return ft.Column(
        [
            scriptsText,
            emitterButton,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )
