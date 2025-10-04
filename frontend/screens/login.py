import flet as ft
import requests
import json

from .constants import WIDTH_SCREEN, API_URI

def login_view(page: ft.Page):

    page.title = "Inicio de Sesión"
    page.bgcolor = ft.Colors.WHITE
    username = ft.TextField(value="", width=WIDTH_SCREEN, text_style=ft.TextStyle(color=ft.Colors.BLACK))
    password = ft.TextField(value="", password=True, width=WIDTH_SCREEN, text_style=ft.TextStyle(color=ft.Colors.BLACK))
    title = ft.Text(style=ft.TextStyle(
            size=20,
            weight=ft.FontWeight.W_700,
            color=ft.Colors.BLACK
        )
    )

    dlg_authentication = ft.AlertDialog(
        content=ft.Column(
            [
                ft.ProgressRing(),
                ft.Text("Autenticando")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    def get_data():
        try:
            r = requests.get(f"{API_URI}/greeting")
            data = r.json()
            print(data)
            title.value = data["message"]
        except Exception as ex:
            title.value = f"Error al conectar con la API: {ex}"
        page.update()

    async def authenticate(e): 
        print(username.value)
        print(password.value)
        print("iniciamos sesión")
        credentials = {"username": username.value, "password": password.value}
        try:
            r = requests.post(f"{API_URI}/login", json=credentials)
            data = r.json()
            page.session.set("user_loged", json.dumps(data))
            print(data)
            page.go("/home")
        except Exception as e:
            print(str(e))
            page.open(ft.SnackBar(ft.Text(value="Saliendo del aplicativo")))
    
    get_data()

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
                            title
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

