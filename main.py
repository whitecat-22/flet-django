import flet as ft
import requests

input_form = ft.TextField(hint_text='give some text')
screen_mode = ft.Icon(ft.icons.TRIP_ORIGIN_ROUNDED),

def main(page: ft.Page):

    def toggle_icon(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        toggle_dark_light_icon.selected = not toggle_dark_light_icon.selected
        page.update()

    toggle_dark_light_icon = ft.IconButton(
        icon="light_mode",
        selected_icon = "dark_mode",
        tooltip=f"switch light / dark mode",
        on_click=toggle_icon,
    )


    def get(e):
        r = requests.get("http://127.0.0.1:8000/").json()
        for i in range(len(r)):
            page.add(ft.Text(r[i]['text']))
        page.update()

    def post(e):
        requests.post("http://127.0.0.1:8000/", data={'text': str(input_form.value)})
        page.update()


    page.title = "Flet example app, API with Django REST Framework"
    page.theme_mode = "light"

    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.APPS),
        leading_width=40,
        title=ft.Text("Flet example app"),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            toggle_dark_light_icon,
        ],
    )

    page.add(
        ft.Column(controls=[
            input_form,
            ft.FloatingActionButton(text='get', on_click=get),
            ft.FloatingActionButton(text='post', on_click=post),
        ])
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
