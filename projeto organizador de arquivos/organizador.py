import os
import shutil
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Busca o caminho definido no .env ou usa o padrão se estiver vazio
CAMINHO_ALVO = os.getenv("CAMINHO_ORGANIZAR")

MAPA_EXTENSOES = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg"],
    "Instaladores": [".exe", ".msi"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Videos": [".mp4", ".mkv", ".mov"]
}

def organizar():
    if not CAMINHO_ALVO:
        print("❌ Erro: CAMINHO_ORGANIZAR não definido no arquivo .env")
        return

    print(f"🚀 Automação iniciada em: {CAMINHO_ALVO}")
    
    arquivos = os.listdir(CAMINHO_ALVO)
    
    for arquivo in arquivos:
        caminho_antigo = os.path.join(CAMINHO_ALVO, arquivo)
        
        if os.path.isdir(caminho_antigo):
            continue
            
        _, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        
        for pasta_destino, extensoes in MAPA_EXTENSOES.items():
            if extensao in extensoes:
                caminho_pasta_nova = os.path.join(CAMINHO_ALVO, pasta_destino)
                
                if not os.path.exists(caminho_pasta_nova):
                    os.makedirs(caminho_pasta_nova)
                
                shutil.move(caminho_antigo, os.path.join(caminho_pasta_nova, arquivo))
                print(f"✅ MOVIMENTADO: {arquivo} -> {pasta_destino}")
                break

if __name__ == "__main__":
    organizar()
    print("✨ Organização concluída!")