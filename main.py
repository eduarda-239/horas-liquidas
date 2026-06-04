import flet as ft

def main(page: ft.Page):

    # "page" janela do aplicativo.
    # estamo definindo o título da janela.
    page.title = "Horas Líquidas"

    # variável que guarda um componente visual.
    titulo = ft.Text(
        value="Cronômetro de Estudos",
        size=30
    )

    # cria um botão visual.
    def iniciar(e):
        titulo.value = "Estudando..."
        page.update()

    botao = ft.Button(
        content=ft.Text("Iniciar"),
        on_click=iniciar
    )
  
    # flet pega os componentes título e botão e renderiza na janela.
    page.add(titulo, botao)

# a função principal vai ser a "main"
ft.run(main)