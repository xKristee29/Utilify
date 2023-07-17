import flet as ft

def NavBar(page: ft.Page):
    
    routes = [
        '/'
    ]
    
    def on_tab_change(e):
        page.go(routes[nav_bar.selected_index])
    
    nav_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.SEARCH_OUTLINED, selected_icon=ft.icons.SEARCH, label="Caută")
        ],
        selected_index=0,
        on_change=on_tab_change,
    )
    return nav_bar