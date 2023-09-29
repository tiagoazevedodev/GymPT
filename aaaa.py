from graphics import *
LARGURA = 1920
ALTURA = 1080
tela_inicial = True
tela_login = True
tela_erro_login = False
tela_criar_login = False
tela_dados = True
tela_loading = True
login_alunos = {}
login_instrutores = {}

with open("db/alunos.csv", "r") as arquivo:
    for linha in arquivo:
        usuario, senha = linha.split(";")
        login_alunos[usuario] = senha[:-1]

with open("db/instrutores.csv", "r") as arquivo:
    for linha in arquivo:
        usuario, senha = linha.split(";")
        login_instrutores[usuario] = senha[:-1]

window = GraphWin("Chat GymPT", LARGURA, ALTURA)

botao_professor = Rectangle(Point(910, 785), Point(1325, 900))
botao_aluno = Rectangle(Point(590, 787), Point(880, 902))
imagemInicial = Image(Point(LARGURA // 2, ALTURA // 2), "img/telainicial.png")
imagemInicial.draw(window)


def desenhar_background(imagem_anterior, imagem_desejada):
    imagem_anterior = Image(Point(LARGURA // 2, ALTURA // 2), f"{imagem_anterior}")
    imagem_anterior.undraw()
    imagem = Image(Point(LARGURA // 2, ALTURA // 2), f"{imagem_desejada}")
    imagem.draw(window)

def criar_input(x, y, width, r, g, b):
    entrada = Entry(Point(x, y), width)
    entrada.setFill(color_rgb(r, g, b))
    entrada.draw(window)
    return entrada


while tela_inicial:
    mouse = window.checkMouse()
    if mouse is not None:
        print(mouse)
    if mouse is not None and botao_professor.getP1().getX() < mouse.getX() < botao_professor.getP2().getX() and botao_professor.getP1().getY() < mouse.getY() < botao_professor.getP2().getY():
        botao_aluno = False
        tela_inicial = False
    elif mouse is not None and botao_aluno.getP1().getX() < mouse.getX() < botao_aluno.getP2().getX() and botao_aluno.getP1().getY() < mouse.getY() < botao_aluno.getP2().getY():
        botao_aluno = True
        tela_inicial = False

desenhar_background("telainicial.png", "tela_login.png")
usuario_temporario = criar_input(1040, 483, 40, 166, 166, 166)
senha_temporario = criar_input(1040, 561, 40, 166, 166, 166)
botao_login = Rectangle(Point(790, 637), Point(1129, 773))

if botao_aluno:
    while tela_login:
        mouse = window.checkMouse()
        if mouse != None and botao_login.getP1().getX() < mouse.getX() < botao_login.getP2().getX() and botao_login.getP1().getY() < mouse.getY() < botao_login.getP2().getY():
            usuario_input = usuario_temporario.getText()
            senha_input = senha_temporario.getText()
            if usuario_input in login_alunos and senha_input == login_alunos[usuario_input]:
                tela_dados = True
                tela_login = False
                usuario_temporario.undraw()
                senha_temporario.undraw()
            else:
                desenhar_background("tela_login.png", "erro_tela_login.png")

else:
    while tela_login:
        mouse = window.checkMouse()
        if mouse != None and botao_login.getP1().getX() < mouse.getX() < botao_login.getP2().getX() and botao_login.getP1().getY() < mouse.getY() < botao_login.getP2().getY():
            usuario_input = usuario_temporario.getText()
            senha_input = senha_temporario.getText()
            if usuario_input in login_instrutores and senha_input == login_instrutores[usuario_input]:
                tela_dados = True
                tela_login = False
                usuario_temporario.undraw()
                senha_temporario.undraw()
            else:
                desenhar_background("tela_login.png", "erro_tela_login.png")
while tela_criar_login:
    mouse = window.checkMouse()

desenhar_background("telainicial.png","cadastro-1.png")
botao_enviar = Rectangle(Point(1447, 920), Point(1781, 1003))
desenhar = 0

nome_temporario = criar_input(611, 304, 59, 166, 166, 166)
idade_temporario = criar_input(389, 412, 13, 166, 166, 166)
sexo_temporario = criar_input(399, 519, 20, 166, 166, 166)
altura_temporario = criar_input(427, 624, 12, 166, 166, 166)
peso_temporario = criar_input(383, 730, 17, 166, 166, 166)
dias_disponiveis_temporario = criar_input(669, 842, 10, 166, 166, 166)
tempo_disponivel_temporario = criar_input(1685, 301, 15, 166, 166, 166)
objetivo_temporario = criar_input(1608, 393, 52, 166, 166, 166)

campos = [nome_temporario, idade_temporario, sexo_temporario, altura_temporario, peso_temporario,
              dias_disponiveis_temporario, tempo_disponivel_temporario, objetivo_temporario]
dados_true = {}


while tela_dados:
    mouse = window.checkMouse()

    for i, campo in enumerate(campos):
        valor = campo.getText()
        if valor != "":
            dados_true[i] = valor
        elif i in dados_true:
            del dados_true[i]

    campos_preenchidos = len(dados_true)
    desenhar_background(f"cadastro{campos_preenchidos - 2}.png", f"cadastro{campos_preenchidos - 1}.png")

    if mouse is not None:
        if botao_enviar.getP1().getX() < mouse.getX() < botao_enviar.getP2().getX() and botao_enviar.getP1().getY() < mouse.getY() < botao_enviar.getP2().getY() and campos_preenchidos == 8:
            tela_dados = False

for input in campos:
    input.undraw()
desenhar_background("cadastro7.png","loading.png")

while tela_loading:
    mouse = window.checkMouse()