import flet as ft

page = None

def init(page_instance: ft.Page):
    global page
    page = page_instance

def notify(text):
    global page
    page.snack_bar = ft.SnackBar(ft.Text(text))
    page.snack_bar.open = True
    page.update()