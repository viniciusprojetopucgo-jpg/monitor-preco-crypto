import os
import requests
import time
from dotenv import load_dotenv

# 1. CARREGAR AS CONFIGURAÇÕES (Onde o Python lê o seu arquivo .env)
load_dotenv()
MOEDA = os.getenv("SIMBOLO_MOEDA")
LIMITE = float(os.getenv("LIMITE_ALERTA"))

# 2. DEFINIR A FUNÇÃO DE BUSCA (O "trabalhador" que vai na internet buscar o dado)
def buscar_preco():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={MOEDA}&vs_currencies=usd"
    try:
        # Faz a requisição HTTP (igual ao nó de HTTP Request do n8n)
        resposta = requests.get(url)
        dados = resposta.json()
        
        # Extrai o valor do JSON recebido
        preco_atual = dados[MOEDA]['usd']
        return preco_atual
    except Exception as e:
        print(f"Erro ao conectar na API: {e}")
        return None

# 3. EXECUÇÃO E LOOP DE MONITORAMENTO
print(f"🚀 Sistema iniciado! Monitorando {MOEDA}...")
print(f"🔔 Alerta configurado para: ${LIMITE}")

while True:
    # Chama a função que criamos acima
    preco_agora = buscar_preco()
    
    if preco_agora:
        # Lógica de decisão
        if preco_agora > LIMITE:
            print(f"🚨 ALERTA: O {MOEDA} subiu! Preço atual: ${preco_agora} (Limite: ${LIMITE})")
        else:
            print(f"✅ Tudo ok. {MOEDA} está em ${preco_agora}. Monitorando...")
    
    # Pausa de 30 segundos (Essencial para não ser bloqueado pela API e economizar CPU)
    time.sleep(30)