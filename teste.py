from graphics import *

LARGURA = 1920
ALTURA = 1080
tela_inicial = True
tela_cadastro = True

window = GraphWin("Chat GymPT", LARGURA, ALTURA,)
window.setBackground("Black")
treino = """É ótimo saber que você está interessado em criar um treino de musculação personalizado para Tiago com base em suas informações. Vamos criar um programa que visa ajudá-lo a ganhar músculos de maneira eficaz. Este treino será dividido em 5 dias de treinamento por semana, sem incluir os dias de descanso. Certifique-se de que Tiago esteja se alimentando adequadamente para apoiar seu objetivo de ganhar músculos e considere consultar um profissional de fitness ou um personal trainer antes de iniciar qualquer novo programa de treinamento.

Dia 1 - Treino de Peito e Tríceps:

Supino reto: 4 séries de 8-10 repetições
Supino inclinado: 3 séries de 8-10 repetições
Crucifixo: 3 séries de 10-12 repetições
Tríceps corda na polia alta: 4 séries de 10-12 repetições
Tríceps testa: 3 séries de 10-12 repetições
Dia 2 - Treino de Costas e Bíceps:

Pull-ups: 4 séries de 6-8 repetições
Barra fixa: 3 séries de 8-10 repetições
Puxada alta na polia: 3 séries de 10-12 repetições
Rosca direta com barra: 4 séries de 10-12 repetições
Rosca martelo alternada: 3 séries de 10-12 repetições
Dia 3 - Treino de Pernas:

Agachamento livre: 4 séries de 8-10 repetições
Leg press: 3 séries de 10-12 repetições
Extensora de pernas: 3 séries de 10-12 repetições
Cadeira flexora: 4 séries de 10-12 repetições
Panturrilha no smith: 4 séries de 12-15 repetições
Dia 4 - Treino de Ombros e Trapézio:

Desenvolvimento com halteres: 4 séries de 8-10 repetições
Elevação lateral com halteres: 3 séries de 10-12 repetições
Remada alta: 3 séries de 10-12 repetições
Encolhimento de ombros: 4 séries de 10-12 repetições
Dia 5 - Treino de Pernas e Abs:

Afundo com halteres: 4 séries de 8-10 repetições (cada perna)
Stiff: 3 séries de 10-12 repetições
Abdominais crunch: 4 séries de 15-20 repetições
Prancha: 3 séries de 30-60 segundos
Lembre-se de que a técnica é fundamental. Certifique-se de que Tiago esteja executando os exercícios com a forma correta para evitar lesões. Também é importante aumentar gradualmente a carga ao longo do tempo para continuar progredindo."""

metade = len(treino)
metade_texto = treino[:metade]
outra_metade_texto = treino[metade::]
print(metade_texto)
print("---------------------------------------------------------------------------")
print(outra_metade_texto)

output = Text(Point(LARGURA//2, ALTURA//2.1), treino)
output.setSize(14)
output.setFill(color_rgb(255, 255, 255))
output.setStyle("bold")
output.setFace("courier")
output.draw(window)


while True:
    mouse = window.checkMouse()
