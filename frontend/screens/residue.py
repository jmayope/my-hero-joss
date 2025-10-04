import flet as ft
import json
def residue_view(page: ft.Page):

    page.title = "Administración de Residuos"
    page.bgcolor = ft.Colors.WHITE

    user_loged = {}

    username = ft.Text(
        style=ft.TextStyle(
            color=ft.Colors.WHITE
        )
    )

    names = ft.Text(
        style=ft.TextStyle(
            color=ft.Colors.WHITE
        )
    )

    def get_initial_data():
        user_loged = json.loads(page.session.get("user_loged"))
        username.value = user_loged["username"]
        names.value = user_loged["names"]
        print(user_loged)

    
    get_initial_data()

    return ft.View(
        "/residue",
        controls=[
            ft.Column(
                [
                    ft.Container(
                        content=ft.ListTile(
                            leading=ft.Icon(name=ft.Icons.ACCOUNT_CIRCLE),
                            title=username,
                            subtitle=names,
                        ),
                        bgcolor=ft.Colors.BLUE_900,
                        border_radius=ft.border_radius.only(
                            bottom_left=40,
                            bottom_right=40
                        )
                    ),
                    ft.Text(
                        value="Contenido"
                    )
                ],
            )
        ],
        padding=0
    )