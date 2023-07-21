import flet as ft

from modules.app_bar import AppBar
from modules.nav_bar import NavBar
from views.router import Router

import stores
import notifier

def main(page: ft.Page):

    page.title = "Utilify"

    page.appbar = AppBar(page)
    router = Router(page)
    page.navigation_bar = NavBar(page)

    notifier.init(page)

    page.on_route_change = router.on_route_change
    page.add(
        router.body
    )

    page.go('/recomandare')

    page.update()


ft.app(target=main, assets_dir="assets")