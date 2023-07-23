import flet as ft

from views.search import Search
from views.recommend import Recommend
from views.playlist import Playlist
from views.help import Help

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {
            '/recomandare': Recommend,
            '/cautare': Search,
            '/playlist': Playlist,
            '/ajutor': Help
        }
        self.body = ft.Container(expand=True, padding=10)

    def on_route_change(self, route):
        self.body.content = self.routes[route.route](self.page)
        self.body.update()