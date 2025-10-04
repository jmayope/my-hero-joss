from  .constants import WIDTH_SCREEN, PRIMARY_COLOR, ASSETS_DIR
import flet as ft
from typing import Dict, Optional
import json

def home_view(page: ft.Page):

    user_loged = {}
    username = ft.Text(style=ft.TextStyle(color=ft.Colors.WHITE))
    names = ft.Text(style=ft.TextStyle(color=ft.Colors.WHITE38))

    gridView = ft.GridView(
        expand=True,
        max_extent=150,
        child_aspect_ratio=1,
        spacing=10,
        run_spacing=10
    )



    def get_inititial_data():
        user_loged = json.loads(page.session.get("user_loged"))
        username.value = user_loged["username"]
        names.value = user_loged["names"]

        gridView.controls.append(
            ft.Container(
                on_click=lambda e : go_to_route("/residue", e),
                content=ft.Column(
                    [
                        ft.Icon(name=ft.Icons.LIST_ALT),
                        ft.Text(
                            value="Residuos",
                            style=ft.TextStyle(
                                weight=ft.FontWeight.BOLD,
                                size=14,
                            ),
                        ),
                        ft.Text(
                            value="Administra los residuos de tu empresa",
                            style=ft.TextStyle(
                                color=ft.Colors.GREY_900,
                                size=10
                            ),
                            text_align=ft.TextAlign.CENTER
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
                bgcolor=ft.Colors.GREY_200,
                border_radius=ft.border_radius.all(20),
            )
        )

        page.update()

    def logout(e):
        print("Saliendo del sistema")
        page.open(ft.SnackBar(ft.Text(value="Saliendo del aplicativo")))
        page.update()
        page.go('/')
    
    def go_to_route(route, e):
        print(route)

        page.go(route)

    get_inititial_data()

    return ft.View(
        "/home",
        controls=[
            ft.Column(
                [
                    ft.Container(
                        content=ft.ListTile(
                            leading=ft.Icon(name=ft.Icons.ACCOUNT_CIRCLE),
                            title=username,
                            subtitle=names,
                            trailing=ft.IconButton(
                                icon=ft.Icons.LOGOUT,
                                on_click=logout,
                                style=ft.ButtonStyle(
                                    color=ft.Colors.WHITE
                                )
                            )
                        ),
                        bgcolor=ft.Colors.BLUE_600,
                        border_radius=ft.border_radius.only(
                            bottom_left=40,
                            bottom_right=40
                        )
                    ),
                    ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(
                                    value="Menu Principal",
                                    style=ft.TextStyle(
                                        weight=ft.FontWeight.BOLD,
                                        size=20
                                    )
                                ),
                                gridView,
                                ft.Card(
                                    content=ft.ListTile(
                                        leading=ft.Icon(name=ft.Icons.LIST_ALT),
                                        title=ft.Text(
                                            value="Residuos"
                                        ),
                                        on_click=lambda e: go_to_route('/residue', e)
                                    ),
                                    margin=ft.Margin(bottom=5, left=0, right=0, top=0)
                                ),
                                ft.Card(
                                    content=ft.ListTile(
                                        leading=ft.Icon(name=ft.Icons.LIST_ALT),
                                        title=ft.Text(
                                            value="Usuarios"
                                        ),
                                        on_click=lambda e: go_to_route('/user', e)
                                    ),
                                    margin=ft.Margin(bottom=5, left=0, right=0, top=0)
                                ),
                            ]
                        ),
                        padding=ft.padding.symmetric(vertical=0, horizontal=20)
                    )
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                scroll=ft.ScrollMode.ALWAYS
            )
        ],
        padding=0
    )