import flet as ft

from .constants import WIDTH_SCREEN

def login_view(page: ft.Page):

    page.title = "Inicio de Sesión"
    page.bgcolor = ft.Colors.WHITE
    username = ft.TextField(value="", width=WIDTH_SCREEN, text_style=ft.TextStyle(color=ft.Colors.BLACK))
    password = ft.TextField(value="", password=True, width=WIDTH_SCREEN, text_style=ft.TextStyle(color=ft.Colors.BLACK))

    def authenticate(e): 
        print(username.value)
        print(password.value)
        print("iniciamos sesión")
        page.go("/home")
        

    return ft.View(
        "/",
        controls=[
            ft.Column(
                [
                    ft.Image(
                        src=f"imgs/background.png",
                        width=WIDTH_SCREEN,
                        height=WIDTH_SCREEN,
                        fit=ft.ImageFit.COVER
                    ),
                    ft.Row(
                        [
                            ft.Text(
                                "Inicio de Sesión",
                                style=ft.TextStyle(
                                    size=20,
                                    weight=ft.FontWeight.W_700,
                                    color=ft.Colors.BLACK
                                )
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Text(
                    "Nombre de Usuario",
                    style=ft.TextStyle(
                        size=13,
                        weight=ft.FontWeight.W_400,
                        color=ft.Colors.BLACK
                    ) 
                    ),
                    username,
                    ft.Text(
                    "Contraseña",
                    style=ft.TextStyle(
                        size=13,
                        weight=ft.FontWeight.W_400,
                        color=ft.Colors.BLACK
                    ) 
                    ),
                    password,
                    ft.Row(
                        [
                            ft.ElevatedButton(
                                text="Iniciar Sesión",
                                on_click=authenticate,
                                style=ft.ButtonStyle(
                                    bgcolor=ft.Colors.BLUE_900,
                                    color=ft.Colors.WHITE
                                )
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.START
            )
        ]
    )

