# quickWeather.py – Exibe a previsão do tempo para uma localidade obtida na linha de comando.
from twilio.rest import Client 
import credenciais 
import json 
import requests
import sys



# Processa a localidade a partir dos argumentos da linha de comando

if len(sys.argv) < 2: 
    print("Usage: quickWeather.py  Itapecerica da Serra, BR")
    sys.exit()

location = ' '.join(sys.argv[1:])

# TODO: Faz download dos dados JSON a partir da API de OpenWeatherMap.org. # 
# TODO: Carrega dados JSON em uma variável Python.



url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&cnt=3&appid={credenciais.chave_openweather}&units=metric&lang=pt_br'

response = requests.get(url) 
  # Carrega os dados em uma variavel Python - Faz a requisição para API


try:
    response.raise_for_status()
except Exception as exc:
    print(f"Houve um problema com o download: {exc}")   
    sys.exit() 

if response.status_code == 401: # Verifica se a chave barrou a entrada
    print("\n--- AVISO DO GUICHÊ ---")
    print("A chave da API (2740) ainda não está ativa no servidor.")
    
    sys.exit()


print("Sucesso! Liberada a entrada")
    

weatherData = json.loads(response.text)

# Exibe as descrições da previsão do tempo



w = weatherData['list']

print(f"Current weather in {location}")
print(w[0]['weather'][0]['main'],'-',w[0]['weather'][0]['description'])
print()
print("Tomorrow:")
print(w[1]['weather'][0]['main'],'-',w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print( w[ 2]['weather'][ 0]['main'], '-', w[ 2]['weather'][ 0]['description'])


# 1. Guarda a descrição de hoje em minúsculas para facilitar a verificação
descricao_hoje = w[0]['weather'][0]['description'].lower()

if "chuva" in descricao_hoje:
    mensagem_customizada = f"Previsao em {location}: {descricao_hoje.title()}. Nao esqueça o guarda-chuva Bruno! "

elif "sol" in descricao_hoje or "limpo" in descricao_hoje:
    mensagem_customizada = f"Previsao em {location}: {descricao_hoje.title()}. Aproveite o dia sem chuva Bruno!"  

else:
    mensagem_customizada = f"Previsao em {location} hoje: {descricao_hoje.title()}."

print("\nEnviando SMS para celular...")


twilioCli = Client(credenciais.accountSID, credenciais.authToken)




mensagem = twilioCli.messages.create(
    body=mensagem_customizada,
    from_=credenciais.meuNumeroTwilio,
    to=credenciais.meuCelular
)

print(f"SMS enviado com sucesso! Status: {mensagem.status}")