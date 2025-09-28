from  .constants import WIDTH_SCREEN, PRIMARY_COLOR, ASSETS_DIR, HEIGHT_CARD_MENU_ITEM
import flet as ft

def home_view(page: ft.Page):
    
    
    def logout(e):
        print("Saliendo del sistema")
        page.open(ft.SnackBar(ft.Text(value="Saliendo del aplicativo")))
        page.update()
        page.go('/')
    
    def go_to_route(route, e):
        print(route)

        page.go(route)

    return ft.View(
        "/home",
        padding=0,
        controls=[
            ft.Column(
                [
                    ft.Container(
                        
                        content=ft.Column(
                            [
                                ft.ListTile(
                                    leading=ft.Icon(name=ft.Icons.ACCOUNT_CIRCLE, color=ft.Colors.WHITE),
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
                                ft.Text(
                                    value="Menu Principal",
                                    style=ft.TextStyle(
                                        size=20
                                    )
                                ),
                                ft.Card(
                                    content=ft.ListTile(
                                        leading=ft.Column(
                                            [
                                                ft.Icon(name=ft.Icons.LIST_ALT, color= ft.Colors.GREEN_600),
                                                ft.Text(
                                                    value="Residuos",
                                                    style=ft.TextStyle(
                                                        size=12,
                                                        color=ft.Colors.GREEN_600
                                                    )
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=1
                                        ),
                                        title=ft.Text(
                                            value="Mantenimiento de residuos sólidos",
                                            style=ft.TextStyle(
                                                color=ft.Colors.GREEN_600,
                                            )
                                        ),
                                        on_click=lambda e: go_to_route("/residue", e)
                                    ),
                                    margin=ft.Margin(bottom=5, left=0, right=0, top=0),
                                    elevation=0,
                                    color=ft.Colors.GREEN_50,
                                    height=HEIGHT_CARD_MENU_ITEM
                                ),
                                ft.Card(
                                    content=ft.ListTile(
                                        leading=ft.Column(
                                            [
                                                ft.Icon(name=ft.Icons.PERSON, color= ft.Colors.BLUE_600),
                                                ft.Text(
                                                    value="Usuarios",
                                                    style=ft.TextStyle(
                                                        size=12,
                                                        color=ft.Colors.BLUE_600
                                                    )
                                                )
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                            spacing=1
                                        ),
                                        title=ft.Text(
                                            value="Mantenimiento de Usuarios",
                                            style=ft.TextStyle(
                                                color=ft.Colors.BLUE_600,
                                            ),
                                        ),
                                        on_click=lambda e: go_to_route("/residue", e)
                                    ),
                                    margin=ft.Margin(bottom=5, left=0, right=0, top=0),
                                    elevation=0,
                                    color=ft.Colors.BLUE_50,
                                    height=HEIGHT_CARD_MENU_ITEM
                                ),
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