import requests
import json

# URL da awesomeAPI

url = 'https://economia.awesomeapi.com.br/json/last/CAD-BRL'

try:
    print("Conectando ao mercado financeiro...")
    response = requests.get(url)
    response.raise_for_status() # Verifica se a internet está ok

    # Transforma o JSON em um dicionário Python
    data = json.loads(response.text)

    # Navega nos "vãos" do dicionário (como o fio dental)
    # A estrutura é data['CADBRL']['bid']
    cotacao = data['CADBRL']['bid']
    nome = data['CADBRL']['name']
    data_hora = data['CADBRL']['create_date']

    print(f"\n--- RELATÓRIO DE CÂMBIO (PLANO CANADÁ) ---")
    print(f"Moeda: {nome}")
    print(f"Valor de Compra: R$ {float(cotacao):.2f}")
    print(f"Última Atualização: {data_hora}")
    print("-" * 40)

    if float(cotacao) < 4.00: # Lógica de "Sentido para a Vida"
        print("SINAL VERDE: O dolar está baixando! Hora de guardar!")

    else:
        print("SINAL AMARELO: Continue estudando Python e economizando.")

except Exception as e:
    print(f"Erro ao buscar cotação: {e}")