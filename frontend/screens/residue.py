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
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.IconButton(icon=ft.Icons.HOME, on_click=lambda e: go_to_route("/home", e)),
                                    title=ft.Text(
                                        value="@usuario",
                                        style=ft.TextStyle(
                                            color=ft.Colors.WHITE
                                        )
                                    ),
                                    subtitle=ft.Text(
                                        value="Joe Doe",
                                        style=ft.TextStyle(
                                            color=ft.Colors.WHITE
                                        )
                                    ),
                                    trailing=ft.IconButton(
                                        icon=ft.Icons.LOGOUT,
                                        on_click=logout,
                                        style=ft.ButtonStyle(
                                            color=ft.Colors.WHITE
                                        )
                                    )
                                )
                            ]
                        ),
                        border_radius=ft.border_radius.only(
                            bottom_left=20,
                            bottom_right=20
                        ),
                        bgcolor=ft.Colors.GREEN_600
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.TextField(
                                    value="",
                                    prefix_icon=ft.Icons.SEARCH,
                                    border_radius=ft.border_radius.all(10)
                                )
                            ],
                        ),
                        padding=ft.padding.symmetric(
                            vertical=5, horizontal=25
                        )
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                scroll=ft.ScrollMode.ALWAYS
            )
        ]
    )