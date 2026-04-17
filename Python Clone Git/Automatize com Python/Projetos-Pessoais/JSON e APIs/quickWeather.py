# quickWeather.py – Exibe a previsão do tempo para uma localidade obtida na linha de comando.

import json 
import requests
import sys

# Processa a localidade a partir dos argumentos da linha de comando

if len(sys.argv) < 2:
    print("Usage: quickWeather.py Itapecerica da Serra, BR")
    sys.exit()
location = ' '.join(sys.argv[1:])

# TODO: Faz download dos dados JSON a partir da API de OpenWeatherMap.org. # 
# TODO: Carrega dados JSON em uma variável Python.




# faz o download dos dados JSON a partir da api openweatherMap.org
chave_api = "93254b9b6cdaaf855031fecd61d250df"
url = f'http://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt=3&appid={chave_api}&units=metric&lang=pt_br'

response = requests.get(url) 
  # Carrega os dados em uma variavel Python - Faz a requisição

if response.status_code == 401: # Verifica se a chave barrou a entrada
    print("\n--- AVISO DO GUICHÊ ---")
    print("A chave da API (2740) ainda não está ativa no servidor.")
    print("Aguarde alguns minutos ou verifique seu e-mail de confirmação.")
    sys.exit()

elif not response.ok: # se não for o erro 401, ele avisa
    print(f"Erro inesperado: {response.status_code}")
    response.raise_for_status()
    sys.exit()

else: # se der tudo certo
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

