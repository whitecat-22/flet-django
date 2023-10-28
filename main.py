import flet as ft
import requests

input_form = ft.TextField(hint_text='give some text')

def main(page: ft.Page):
    page.title = "Flet example app, API with Django REST Framework"

    def get(e):
        r = requests.get("http://127.0.0.1:8000/").json()
        for i in range(len(r)):
            page.add(ft.Text(r[i]['text']))
        page.update()

    def post(e):
        requests.post("http://127.0.0.1:8000/", data={'text': str(input_form.value)})
        page.update()

    page.add(
        ft.Column(controls=[
            input_form,
            ft.FloatingActionButton(text='get', on_click=get),
            ft.FloatingActionButton(text='post', on_click=post),
        ])
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
