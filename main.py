from nicegui import ui
from recommend import initRecommendPage

with ui.header(elevated=True).classes('fixed top-0 left-0 right-0 z-0 p-0 justify-center'):
    with ui.tabs() as tabs:
        ui.tab('Recomandare', icon='star')
        ui.tab('Căutare', icon='search')
        ui.tab('Descărcare', icon='download')
        ui.tab('Istoric', icon='book')
        ui.tab('Despre', icon='info')

with ui.element('div').classes('m-0 top-0 left-0 right-0 z-0 justify-center min-h-screen').style('width: 100%;'):
    with ui.tab_panels(tabs, value='Recomandare'):
        with ui.tab_panel('Recomandare'):
            initRecommendPage()
        with ui.tab_panel('Căutare'):
            ui.label('This is the second tab This is the first tab This is the first tab This is the first tab')
        with ui.tab_panel('Descărcare'):
            ui.label('This is the second tab This is the first tab This is the first tab This is the first tab')
        with ui.tab_panel('Istoric'):
            ui.label('This is the first tab This is the first tab This is the first tab This is the first tab')
        with ui.tab_panel('Despre'):
            ui.label('This is the second tab This is the first tab This is the first tab This is the first tab')

ui.run(port=8000, title='Utilify', favicon='favicon.ico', dark=True, window_size=(663, 1000),
        viewport='width=device-width, initial-scale=1.0')