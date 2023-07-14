import flet as ft

from views.search import Search

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {
            '/': Search
        }
        self.body = ft.Container(expand=True, padding=10)

    def on_route_change(self, route):
        self.body.content = self.routes[route.route](self.page)
        self.body.update()