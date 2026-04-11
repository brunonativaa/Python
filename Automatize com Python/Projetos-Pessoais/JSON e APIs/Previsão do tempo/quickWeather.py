# quickWeather.py – Exibe a previsão do tempo para uma localidade obtida na linha de comando e envia um SMS.

from twilio.rest import Client # Oficial do Twilio para interagir com o serviço SMS

import credenciais # Um modulo local, para manter chaves seguras
import json # Biblioteca converte "string" que vem da internet em Dicionário/Lista Python
import requests # Request muito importante para consumo de APIs
import sys # usada aqui para ler argumentos passadas pelo terminal (sys.argv)



# --- FASE 1: ENTRADA DE DADOS ---
# sys.argv armazena o nome do script e os argumentos passados no console.
# Se você digitar: python quickWeather.py "Itapecerica da Serra"
# sys.argv[0] é o nome do script, sys.argv[1:] é a cidade.
if len(sys.argv) < 2: 
    print("Usage: quickWeather.py  Itapecerica da Serra, BR")
    sys.exit()

location = ' '.join(sys.argv[1:]).strip()


# --- FASE 2: COMUNICAÇÃO COM API (OPENWEATHER) ---
# Montamos a URL dinâmica usando f-strings para injetar a cidade e a chave enviando um pedido ao servidor

url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=3&appid={credenciais.chave_openweather}&units=metric&lang=pt_br'
response = requests.get(url) 
 

try:  # Verifica se o servidor respondeu com sucesso ou erro, # Se der erro 404 ou 500, ele pula para o 'except'
    response.raise_for_status()
except Exception as exc:
    print(f"Houve um problema com o download: {exc}")   
    sys.exit() 

# --- FASE 3: TRANSFORMAÇÃO DE DADOS ---
# O response.text é apenas uma string longa. json.loads() transforma isso 
# em um DICIONÁRIO Python, permitindo acessar dados por chaves: weatherData['list']
weatherData = json.loads(response.text)

# A API retorna uma lista de previsões (de 3 em 3 horas).
# w[0] = Agora, w[1] = Próximo período, w[2] = Depois.
w = weatherData['list']

# --- FASE 4: LÓGICA DE NEGÓCIO (ANÁLISE DO TEMPO) ---
# Guarda a descrição de hoje em minúsculas para facilitar a verificação
descricao_hoje = w[0]['weather'][0]['description'].lower()

print(f"Condições metereológicas atuais em: {location}")
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print("Amanhã:")
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print()
print('Depois de amanhã:')
print( w[ 2]['weather'][ 0]['main'], '-', w[ 2]['weather'][ 0]['description'])

# Verificamos palavras-chave na descrição para personalizar o aviso
if "chuva" in descricao_hoje:
    mensagem_customizada = f"Previsao em {location}: {descricao_hoje.title()}. Nao esqueça o guarda-chuva Bruno ☔  "

elif "sol" in descricao_hoje or "limpo" in descricao_hoje:
    mensagem_customizada = f"Previsao em {location}: {descricao_hoje.title()}. Aproveite o sol Bruno 🌞!"  

else:
    mensagem_customizada = f"Previsao em {location} hoje: {descricao_hoje.title()}. Bruno ☁️"

print("\nEnviando SMS para celular...")


# --- FASE 5: SAÍDA DE DADOS (TWILIO SMS) ---
# Autenticamos no serviço da Twilio usando as credenciais do seu arquivo externo
twilioCli = Client(credenciais.accountSID, credenciais.authToken)



# enviando o objeto de mensagem
mensagem = twilioCli.messages.create(
    body=mensagem_customizada,
    from_=credenciais.meuNumeroTwilio,
    to=credenciais.meuCelular
)

print(f"SMS enviado com sucesso! Status: {mensagem.status}")