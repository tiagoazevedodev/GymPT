from graphics import *
import requests
import json

LARGURA = 1920
ALTURA = 1080
tela_inicial = True
tela_login = True
tela_erro_login = False
tela_criar_login = False
tela_dados = False
tela_loading = True
tela_treino = False
tela_escolher_aluno = False
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

# Tela de escolher Aluno ou Professor
while tela_inicial:
    mouse = window.getMouse()
    if botao_professor.getP1().getX() < mouse.getX() < botao_professor.getP2().getX() and botao_professor.getP1().getY() < mouse.getY() < botao_professor.getP2().getY():
        botao_aluno = False
        tela_inicial = False
        tela_loading = False
    elif botao_aluno.getP1().getX() < mouse.getX() < botao_aluno.getP2().getX() and botao_aluno.getP1().getY() < mouse.getY() < botao_aluno.getP2().getY():
        botao_aluno = True
        tela_inicial = False


botao_login = Rectangle(Point(790, 637), Point(1129, 773))
botao_criar_login = Rectangle(Point(840, 798), Point(1080, 850))
erro = False
#Login dos Alunos
if botao_aluno:
    desenhar_background("img/telainicial.png", "img/tela_login.png")
    usuario_temporario = criar_input(1040, 483, 40, 166, 166, 166)
    senha_temporario = criar_input(1040, 561, 40, 166, 166, 166)
    while tela_login:
        mouse = window.checkMouse()
        if mouse is not None and botao_login.getP1().getX() < mouse.getX() < botao_login.getP2().getX() and botao_login.getP1().getY() < mouse.getY() < botao_login.getP2().getY():
            usuario_input = usuario_temporario.getText()
            senha_input = senha_temporario.getText()
            #Testa se o Usuario é válido
            if usuario_input in login_alunos and senha_input == login_alunos[usuario_input]:
                tela_login = False
                tela_loading = False
                tela_treino = True
                usuario_temporario.undraw()
                senha_temporario.undraw()
            #PopUp caso as credenciais estejam erradas
            else:
                desenhar_background("img/tela_login.png", "img/erro_tela_login.png")
                erro = True
        #Tela de Cadastrar Novo Usuário
        else:
            if mouse is not None and botao_criar_login.getP1().getX() < mouse.getX() < botao_criar_login.getP2().getX() and botao_criar_login.getP1().getY() < mouse.getY() < botao_criar_login.getP2().getY():
                tela_dados = True
                tela_criar_login = True
                #Testa se Houve o PopUp para apagar a tela Anterior
                if erro:
                    desenhar_background("img/erro_tela_login.png", "img/criarlogin.png")
                else:
                    desenhar_background("img/tela_login.png", "img/criarlogin.png")
                tela_login = False
                usuario_temporario.undraw()
                senha_temporario.undraw()
#Login dos Instrutores
else:
    desenhar_background("img/telainicial.png", "img/login_instrutor.png")
    usuario_temporario = criar_input(1040, 483, 40, 166, 166, 166)
    senha_temporario = criar_input(1040, 561, 40, 166, 166, 166)
    while tela_login:
        mouse = window.checkMouse()
        if mouse is not None and botao_login.getP1().getX() < mouse.getX() < botao_login.getP2().getX() and botao_login.getP1().getY() < mouse.getY() < botao_login.getP2().getY():
            usuario_input = usuario_temporario.getText()
            senha_input = senha_temporario.getText()
            #Testa se o Instrutor é valido
            if usuario_input in login_instrutores and senha_input == login_instrutores[usuario_input]:
                tela_dados = False
                tela_login = False
                usuario_temporario.undraw()
                senha_temporario.undraw()
            #Mostra PopUp avisando que as credenciais estão erradas
            else:
                desenhar_background("img/tela_login.png", "img/tela_erro_instrutor.png")
                erro = True
                tela_criar_login = False
                tela_dados = False
#Inputs para criar login
if tela_criar_login:
    cadastro_usuario_temporario = criar_input(1040, 483, 40, 166, 166, 166)
    cadastro_senha_temporario = criar_input(1040, 561, 40, 166, 166, 166)
    botao_enviar_login = Rectangle(Point(741, 638), Point(1178, 773))


while tela_criar_login:
    mouse = window.checkMouse()
    #Clicou em enviar, e guardou os dados de usuário
    if mouse is not None and botao_enviar_login.getP1().getX() < mouse.getX() < botao_enviar_login.getP2().getX() and botao_enviar_login.getP1().getY() < mouse.getY() < botao_enviar_login.getP2().getY():
        cadastro_senha_input = cadastro_senha_temporario.getText()
        cadastro_usuario_input = cadastro_usuario_temporario.getText()
        #Testa se já existe um usuário com mesmo nome
        if cadastro_usuario_input not in login_alunos.keys():
            with open("db/alunos.csv", "a") as arquivo:
                string = f"{cadastro_usuario_input};{cadastro_senha_input}\n"
                arquivo.write(string)
            cadastro_usuario_temporario.undraw()
            cadastro_senha_temporario.undraw()
            tela_criar_login = False
            tela_dados = True
        else:
            desenhar_background("img/criarlogin.png", "img/erro_usuario_login.png")
#Tela de preencher os campos
if tela_dados:
    desenhar_background("img/telainicial.png", "img/cadastro-1.png")
    idade = criar_input(389, 412, 13, 166, 166, 166)
    sexo = criar_input(399, 519, 20, 166, 166, 166)
    altura = criar_input(427, 624, 12, 166, 166, 166)
    peso = criar_input(383, 730, 17, 166, 166, 166)
    dias_disponiveis = criar_input(669, 842, 10, 166, 166, 166)
    tempo_disponivel = criar_input(1685, 301, 15, 166, 166, 166)
    objetivo = criar_input(1608, 393, 52, 166, 166, 166)
    nome = criar_input(611, 304, 59, 166, 166, 166)
    botao_enviar = Rectangle(Point(1447, 920), Point(1781, 1003))
    campos = [nome, idade, sexo, altura, peso,
                  dias_disponiveis, tempo_disponivel, objetivo]
    dados_true = {}

#Adiciona os textos dos campos à uma lista, removendo se for apagado
while tela_dados:
    mouse = window.checkMouse()
    for i, campo in enumerate(campos):
        valor = campo.getText()
        if valor != "":
            dados_true[i] = valor
        elif i in dados_true:
            del dados_true[i]

    #Com base nos campos preenchidos, troca a imagem dizendo quantos campos faltam
    campos_preenchidos = len(dados_true)
    desenhar_background(f"img/cadastro{campos_preenchidos - 2}.png", f"img/cadastro{campos_preenchidos - 1}.png")

    #Clicou em enviar e limpou os inputs
    if mouse is not None:
        if botao_enviar.getP1().getX() < mouse.getX() < botao_enviar.getP2().getX() and botao_enviar.getP1().getY() < mouse.getY() < botao_enviar.getP2().getY() and campos_preenchidos == 8:
            for input in campos:
                input.undraw()
            break

#Salva os dados do usuário no arquivo
if tela_dados:
    with open("db/dados_alunos.csv", "a") as arquivo:
        arquivo.write(f"{cadastro_usuario_input}:")
        string = ";".join(dados_true.values())
        arquivo.write(f"{string}\n")
    treino = ""

#Tela de carregamento de treino, aqui está acontecendo a requisição da IA
while tela_loading:
    desenhar_background("img/cadastro7.png", "img/loading.png")
    mouse = window.checkMouse()
    dados_split = string.split(";")
    headers = {"Authorization": f"Bearer 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",
               "Content-Type": "application/json"}
    id_modelo = "gpt-3.5-turbo"
    link = "https://api.openai.com/v1/chat/completions"

    body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user",
                      "content": f"""monte um treino, apenas com agrupamento do dia, exercícios com suas series e repetições.
Ao trocar de dia (treino), crie a próxima linha com apenas o caractere ' ; '
Sem textos supérfluos 
idade:{dados_split[1]}
sexo: {dados_split[2]}
peso:{dados_split[4]}
altura:{dados_split[3]}
dias da semana disponíveis para treino: {dados_split[5]}

-> Por exemplo:
Dia 1 (Segunda-feira) - Treino de Peito e Tríceps:

Supino Reto: 4x10
Supino Inclinado com Halteres: 3x12
Crucifixo na Máquina: 3x12
Tríceps Testa: 4x10
Tríceps Corda no Pulley: 3x12
;

Dia 2 (Terça-feira) - Treino de Pernas:

Agachamento Livre: 4x10
Leg Press: 3x12
Cadeira Extensora: 3x12
Flexora deitado: 4x10
Panturrilha no Leg Press: 4x15
;
...
"""}]
    }
    body_mensagem = json.dumps(body_mensagem)
    requisicao = requests.post(link, headers=headers, data=body_mensagem)
    resposta = requisicao.json()
    treino = resposta["choices"][0]["message"]["content"]

    #Quando treino receber uma string, ela será formatada em dois blocos para ser mostrado na tela
    if treino != "":
        listaTreino = treino.split(";")
        blocosTexto = len(listaTreino)
        primeiroPrintLista = []
        treino_salvar = ""
        for i in range(blocosTexto//2):
            primeiroPrintLista.append(listaTreino[i])
            primeiroPrint = " ".join(primeiroPrintLista)
        treino_salvar = primeiroPrint+";"
        segundoPrintLista = []
        for i in range(blocosTexto//2, blocosTexto):
            segundoPrintLista.append(listaTreino[i])
            segundoPrint = " ".join(segundoPrintLista)
        treino_salvar += segundoPrint
        with open("db/treinos.csv", "a") as arquivo:
            arquivo.write(f"{cadastro_usuario_input}${treino_salvar}>")
        break

#Mostra o treino na tela
if tela_loading:
    output1 = Text(Point(LARGURA//3, ALTURA//1.95), primeiroPrint)
    output1.setSize(15)
    output1.setFill(color_rgb(225, 225, 225))
    output1.setStyle("bold")
    output1.setFace("courier")
    output2 = Text(Point(LARGURA//3*2, ALTURA//1.95), segundoPrint)
    output2.setSize(15)
    output2.setFill(color_rgb(225, 225, 225))
    output2.setStyle("bold")
    output2.setFace("courier")

    desenhar_background("img/loading.png", "img/tela_treino.png")
    output1.draw(window)
    output2.draw(window)

#Quando o usuário já tiver login, Essa parte do código faz o seu treino já salvo ser mostrado
while tela_treino:
    desenhar_background("img/tela_login.png", "img/tela_treino.png")
    with open("db/treinos.csv", "r") as arquivo:
        arquivo = arquivo.read()
        arquivo = arquivo[:-1]
        arquivo = arquivo[1:]
        listaAlunos = []
        listaTreinos = []
        listaAlunosBruta = arquivo.split(">")
        for i in listaAlunosBruta:
            aluno, treino = i.split("$")
            listaAlunos.append(aluno)
            listaTreinos.append(treino)
        for aluno in listaAlunos:
            if aluno == usuario_input:
                index = listaAlunos.index(aluno)
                treino = listaTreinos[index]
                break
    listaTreino = treino.split(";")
    blocosTexto = len(listaTreino)
    primeiroPrintLista = []
    for i in range(blocosTexto // 2):
        primeiroPrintLista.append(listaTreino[i])
        primeiroPrint = " ".join(primeiroPrintLista)
    segundoPrintLista = []
    for i in range(blocosTexto // 2, blocosTexto):
        segundoPrintLista.append(listaTreino[i])
        segundoPrint = " ".join(segundoPrintLista)

    output1 = Text(Point(LARGURA // 3, ALTURA // 1.95), primeiroPrint)
    output1.setSize(15)
    output1.setFill(color_rgb(225, 225, 225))
    output1.setStyle("bold")
    output1.setFace("courier")
    output2 = Text(Point(LARGURA // 3 * 2, ALTURA // 1.95), segundoPrint)
    output2.setSize(15)
    output2.setFill(color_rgb(225, 225, 225))
    output2.setStyle("bold")
    output2.setFace("courier")
    break

if tela_treino:
    output1.draw(window)
    output2.draw(window)

#Mostrando os alunos já cadastrados para o instrutor escolher um e ver seu treino salvo
if botao_aluno is False:
    desenhar_background("img/login_instrutor.png", "img/escolher_aluno.png")
    tela_escolher_aluno = True
    aluno_escolhido_temporario = criar_input(882, 980, 40, 250, 250, 250)
    with open("db/alunos.csv", "r") as arquivo:
        lista_alunos = []
        for linha in arquivo:
            nome_aluno = linha.split(";")[0]
            lista_alunos.append(nome_aluno)

        quantidade_de_alunos = len(lista_alunos)
        primeiroPrintAlunos = []
        for i in range(quantidade_de_alunos//2):
            primeiroPrintAlunos.append(lista_alunos[i])
            primeiroPrintAlunos_STR = "\n".join(primeiroPrintAlunos)
        segundoPrintAlunos = []
        for i in range(quantidade_de_alunos//2, quantidade_de_alunos):
            segundoPrintAlunos.append(lista_alunos[i])
            segundoPrintAlunos_STR = "\n".join(segundoPrintAlunos)
        output1_escolher_aluno = Text(Point(LARGURA // 3, ALTURA // 1.80), primeiroPrintAlunos_STR)
        output1_escolher_aluno.setSize(24)
        output1_escolher_aluno.setFill(color_rgb(225, 225, 225))
        output1_escolher_aluno.setStyle("bold")
        output1_escolher_aluno.setFace("courier")

        output2_escolher_aluno = Text(Point(LARGURA // 3 * 2, ALTURA // 1.80), segundoPrintAlunos_STR)
        output2_escolher_aluno.setSize(24)
        output2_escolher_aluno.setFill(color_rgb(225, 225, 225))
        output2_escolher_aluno.setStyle("bold")
        output2_escolher_aluno.setFace("courier")
        output1_escolher_aluno.draw(window)
        output2_escolher_aluno.draw(window)
    
#Mostra o treino do aluno escolhido
while tela_escolher_aluno:
    mouse = window.getMouse()
    botao_enviar = Rectangle(Point(1079.0, 953.0), Point(1239.0, 1003.0))
    aluno_escolhido = aluno_escolhido_temporario.getText()
    with open("db/treinos.csv", "r") as arquivo:
        arquivo = arquivo.read()
        arquivo = arquivo[:-1]
        arquivo = arquivo[1:]
        listaAlunos = []
        listaTreinos = []
        listaAlunosBruta = arquivo.split(">")
        for i in listaAlunosBruta:
            aluno, treino = i.split("$")
            listaAlunos.append(aluno)
            listaTreinos.append(treino)
        for aluno in listaAlunos:
            if aluno == usuario_input:
                index = listaAlunos.index(aluno)
                treino = listaTreinos[index]
                break
    listaTreino = treino.split(";")
    blocosTexto = len(listaTreino)
    primeiroPrintLista = []
    for i in range(blocosTexto // 2):
        primeiroPrintLista.append(listaTreino[i])
        primeiroPrint = " ".join(primeiroPrintLista)
    segundoPrintLista = []
    for i in range(blocosTexto // 2, blocosTexto):
        segundoPrintLista.append(listaTreino[i])
        segundoPrint = " ".join(segundoPrintLista)

    output1 = Text(Point(LARGURA // 3, ALTURA // 1.95), primeiroPrint)
    output1.setSize(15)
    output1.setFill(color_rgb(225, 225, 225))
    output1.setStyle("bold")
    output1.setFace("courier")
    output2 = Text(Point(LARGURA // 3 * 2, ALTURA // 1.95), segundoPrint)
    output2.setSize(15)
    output2.setFill(color_rgb(225, 225, 225))
    output2.setStyle("bold")
    output2.setFace("courier")
    aluno_escolhido_temporario.undraw()
    desenhar_background("img/escolher_aluno.png","img/instrutor_treino_do_aluno.png")
    output1.draw(window)
    output2.draw(window)
while True:
    mouse = window.checkMouse()