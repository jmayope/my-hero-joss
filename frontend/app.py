import flet as ft

from screens.login import login_view
from screens.home import home_view
from screens.user import user_view
from screens.constants import WIDTH_SCREEN

def main(page: ft.Page):

    # page.bgcolor = ft.Colors.WHITE
    page.theme_mode = ft.ThemeMode.LIGHT
    # page.theme=ft.Theme(color_scheme_seed=ft.Colors.WHITE,) #aquí el verde es el color base
    page.window.width = WIDTH_SCREEN
    page.window.height = 800
    page.window.resizable = False

    def route_change(route):
        page.views.clear()

        if page.route == '/':
            page.views.append(login_view(page))
        elif page.route == '/home':
            page.views.append(home_view(page))
        elif page.route == '/user':
            page.views.append(user_view(page))
        

        page.update()
    
    page.on_route_change = route_change
    page.go(page.route)


ft.app(main)