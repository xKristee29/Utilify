from nicegui import ui
import recommend
import search
import downloads

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
            recommend.initRecommendPage()
        with ui.tab_panel('Căutare'):
            search.initSearchPage()
        with ui.tab_panel('Descărcare'):
            downloads.initDownladPage()
        with ui.tab_panel('Istoric'):
            ui.label('Work in progress')
            ui.spinner(size='lg')
        with ui.tab_panel('Despre'):
            ui.label('Work in progress')
            ui.spinner(size='lg')

ui.run(port=8000, title='Utilify', favicon='favicon.ico', dark=True, window_size=(680, 1000),
        viewport='width=device-width, initial-scale=1.0')