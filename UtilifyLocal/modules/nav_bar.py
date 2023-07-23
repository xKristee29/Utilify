import flet as ft

def NavBar(page: ft.Page):
    
    routes = [
        '/recomandare',
        '/cautare',
        '/playlist',
        '/descarcare',
        '/setari',
        '/ajutor'
    ]
    
    def on_tab_change(e):
        page.go(routes[nav_bar.selected_index])
    
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.STAR_OUTLINED, selected_icon=ft.icons.STAR, label="Recomandare"),
            ft.NavigationDestination(icon=ft.icons.SEARCH_OUTLINED, selected_icon=ft.icons.SEARCH, label="Caută"),
            ft.NavigationDestination(icon=ft.icons.LIBRARY_MUSIC_OUTLINED, selected_icon=ft.icons.LIBRARY_MUSIC, label="Playlist"),
            ft.NavigationDestination(icon=ft.icons.DOWNLOAD_OUTLINED, selected_icon=ft.icons.DOWNLOAD, label="Descărcări"),
            ft.NavigationDestination(icon=ft.icons.SETTINGS_OUTLINED, selected_icon=ft.icons.SETTINGS, label="Setări"),
            ft.NavigationDestination(icon=ft.icons.HELP_OUTLINED, selected_icon=ft.icons.HELP, label="Ajutor")
        ],
        selected_index=0,
        on_change=on_tab_change,
    )
    return nav_bar
