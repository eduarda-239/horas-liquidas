import flet as ft   # Importei a classe flet e dei um apelido de ft.

# função principal do aplicativo
def main(page: ft.Page):

    # "page" representa a janela do aplicativo.
    # aqui definimos o título da janela.
    page.title = "Horas Líquidas"

    # variável que guarda um componente visual de texto.
    titulo = ft.Text(
        # conteúdo exibido na tela.
        value="Cronômetro de Estudos",

        # tamanho da fonte.
        size=30
    )

    materias = ft.Dropdown(
        label="Selecione a matéria",
        options=[
            ft.dropdown.Option("Português"),
            ft.dropdown.Option("T.I"),
            ft.dropdown.Option("Matemática"),
            ft.dropdown.Option("Conhecimentos Bancários")
        ]
    )

    # função de evento.
    # será executada quando o botão for clicado.
    def iniciar(e):

        # altera dinamicamente o texto do componente.
        titulo.value = "Estudando..."

        # atualiza/renderiza a interface gráfica.
        page.update()

    # cria um componente visual de botão.
    botao = ft.Button(

        # conteúdo interno do botão.
        content=ft.Text("Iniciar"),

        # conecta o clique do botão à função iniciar.
        on_click=iniciar
    )

    # adiciona os componentes na janela do aplicativo.
    page.add(titulo, materias, botao)

# inicia a aplicação executando a função principal.
ft.run(main)