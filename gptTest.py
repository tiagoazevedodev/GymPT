import requests
import json

headers = {"Authorization": f"Bearer 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", "Content-Type": "application/json" }
id_modelo = "gpt-3.5-turbo"
link = "https://api.openai.com/v1/chat/completions"

body_mensagem = {
        "model": id_modelo,
        "messages": [{"role": "user",
                      "content": """Crie um treino de musculação personalizado baseado nos dados a seguir, o treino deve incluir todos os grupos musculares de modo a dividi-los entre os dias disponiveis, sem mostrar os dias de descanso:
Nome: Tiago
Experiencia de treinamento: 3 anos
Idade: 19
Sexo: Masculino
Altura: 1.74
Peso: 76
Dias disponiveis por semana para treinar: 2
Tempo disponivel por treino: 60 minutos
Objetivo final com o treinamento: Ganhar musculos"""}]
}

body_mensagem = json.dumps(body_mensagem)
requisicao = requests.post(link, headers=headers, data=body_mensagem)
resposta = requisicao.json()
treino = resposta["choices"][0]["message"]["content"]