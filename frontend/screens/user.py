from  .constants import WIDTH_SCREEN, PRIMARY_COLOR, ASSETS_DIR
import flet as ft

def user_view(page: ft.Page):
    def back(e):
        print("volviendo a home")
        page.go('/home')
    
    
    return ft.View(
        "/user",
        controls=[
            ft.Column(
                [
                    ft.ListTile(
                        leading=ft.IconButton(icon=ft.Icons.ARROW_BACK, on_click=back),
                        title=ft.Text(
                            value="Administración de Clientes",
                            style=ft.TextStyle(
                                color=ft.Colors.BLUE_900
                            )
                        ),
                    ),
                    ft.Divider(),
                    ft.Row(
                        [
                            ft.Icon(name=ft.Icons.SEARCH),
                            ft.TextField(
                                value="Busca Usuarios",

                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                scroll=ft.ScrollMode.ALWAYS
            )
        ]
    )