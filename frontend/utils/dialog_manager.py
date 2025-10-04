import flet as ft

dialog = None  # Variable global compartida

def get_dialog():
    global dialog
    return dialog

def set_dialog(new_dialog):
    global dialog
    dialog = new_dialog
