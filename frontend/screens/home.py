from  .constants import WIDTH_SCREEN, PRIMARY_COLOR, ASSETS_DIR
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
        controls=[
            ft.Column(
                [
                    ft.ListTile(
                        leading=ft.Icon(name=ft.Icons.ACCOUNT_CIRCLE),
                        title=ft.Text(
                            value="@usuario",
                            style=ft.TextStyle(
                                color=ft.Colors.BLUE_900
                            )
                        ),
                        subtitle=ft.Text(
                            value="Joe Doe",
                        ),
                        trailing=ft.IconButton(
                            icon=ft.Icons.LOGOUT,
                            on_click=logout,
                            style=ft.ButtonStyle(
                                color=ft.Colors.RED_900
                            )
                        )
                    ),
                    ft.Text(
                        value="Menu Principal"
                    ),
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
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                scroll=ft.ScrollMode.ALWAYS
            )
        ]
    )