import flet as ft

def residue_view(page: ft.Page):
    
    def go_to_route(route, e):
        print(route)

        page.go(route)
    
    def logout(e):
        print("Saliendo del sistema")
        page.open(ft.SnackBar(ft.Text(value="Saliendo del aplicativo")))
        page.update()
        page.go('/')
    
    return ft.View(
        "/residue",
        padding=0,
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