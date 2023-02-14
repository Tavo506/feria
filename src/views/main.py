import flet as ft


def main(page: ft.Page):
    page.title = "Lista Feria del Agricultor"
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.bgcolor = "#DDDDDD"

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


browser = ft.WEB_BROWSER
app = ft.FLET_APP

browser_mode = False
mode = browser if browser_mode else app

if __name__ == '__main__':
    ft.app(target=main, view=mode)
