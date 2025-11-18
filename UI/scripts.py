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
    optical_text = (
        "Також хотіли б вас попередити:\n\n"
        "Наша компанія не здійснює обмін або повернення комплектуючих, які мають оптичні елементи.\n\n"
        "До цього відносяться: фокусні та коліматорні лінзи, дзеркала, захисне скло, захисні конектори.\n\n"
        "Тому просимо вас дуже уважно перевірити габаритні параметри, фокусну відстань, розраховану потужність відповідних комплектуючих\n\n"
        "Ми турбуємось про безпеку ваших коштів!\n\n"
    )
    consumables_text = (
        "Вітаю! \n\n"
        "Для виставлення рахунку будь ласка надішліть:\n\n"
        " - Назву компанії\n\n"
        " - Код ЄДРПОУ\n\n"
        " - Потрібні вам позиції та кількість\n\n"
        " - Адресу відправки нової пошти\n\n"
        " - Замовлення буде надіслано одразу після підтвердження оплати від бухгалтерії"
    )
    promua_text = (
        "Вітаю отримали ваше замовлення на PROM UA! \n\n"
        "Нажаль післяплата або розрахунок на карту тимчасово недоступний\n\n"
        "Можу запропонувати оплатити по IBAN, оплата за ним приходить швидше\n\n"
    )
    def copy_emitter(e):
        e.page.set_clipboard(emitter_text)
        e.page.update()
    
    def copy_optical(e):
        e.page.set_clipboard(optical_text)
        e.page.update()

    def copy_consumables(e):
        e.page.set_clipboard(consumables_text)
        e.page.update()
    
    def copy_promua(e):
        e.page.set_clipboard(promua_text)
        e.page.update()

    RepairscriptsText = ft.Text(
        value="СКРИПТИ РЕМОНТУ:",
        width=200,
        color=ds.accent,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    emitterButton = ft.ElevatedButton(
        "ВИПРОМІНЮВАЧІВ",
        width=230,
        height=30,
        on_click=copy_emitter,
        bgcolor=ds.light,
        color=ds.white,
    )

    ConsumablesscriptsText = ft.Text(
        value="ПРОДАЖ РОЗХІДНИКІВ:",
        width=200,
        color=ds.accent,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    opticButton = ft.ElevatedButton(
        "ПОПЕРЕДЖЕННЯ ПРО ОПТИКУ",
        width=230,
        height=30,
        on_click=copy_optical,
        bgcolor=ds.light,
        color=ds.white,
    )

    clientDataButton = ft.ElevatedButton(
        "НАДІШЛІТЬ РЕКВІЗИТИ",
        width=230,
        height=30,
        on_click=copy_consumables,
        bgcolor=ds.light,
        color=ds.white,
    )

    promUaText = ft.Text(
        value="PROM.UA: ",
        width=200,
        color=ds.accent,
        size=15,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )

    clientPromUaButton = ft.ElevatedButton(
        "СКРИПТ PROM.UA",
        width=230,
        height=30,
        on_click=copy_promua,
        bgcolor=ds.light,
        color=ds.white,
    )

    return ft.Column(
        [
            RepairscriptsText,
            emitterButton,
            ConsumablesscriptsText,
            clientDataButton,
            opticButton,
            promUaText,
            clientPromUaButton
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )