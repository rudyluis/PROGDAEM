import flet as ft

def main(page: ft.Page):
    txt_name = ft.TextField(label="Tu nombre")

    def btn_click(e):
        page.add(ft.Text(f"Hola, {txt_name.value}!"))

    page.add(txt_name, ft.ElevatedButton("Saludar", on_click=btn_click))

ft.app(target=main)