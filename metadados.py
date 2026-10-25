import os
import time

print("=== EXTRATOR DE METADADOS DE SEGURANÇA ===")
print("(Digite 'sair' para fechar o programa)\n")

while True:
    # Pede o nome ou o caminho do arquivo (ex: seguranca_log.txt ou imagem.jpg)
    nome_arquivo = input("Digite o nome do arquivo com a extensão (ou 'sair'): ")
    
    if nome_arquivo.lower() == 'sair':
        print("\nSistema de perícia encerrado. Até mais!")
        break
        
    # Verifica se o arquivo realmente existe na pasta
    if os.path.exists(nome_arquivo):
        print("\n🔍 [ANALISANDO ARQUIVO...] Arquivo encontrado!")
        print("----------------------------------------")
        
        # 1. Tamanho do arquivo
        tamanho = os.path.getsize(nome_arquivo)
        print(f"📦 Tamanho: {tamanho} bytes")
        
        # 2. Data de criação
        criacao = os.path.getctime(nome_arquivo)
        data_criacao = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(criacao))
        print(f"📅 Criado em: {data_criacao}")
        
        # 3. Data da última modificação
        modificacao = os.path.getmtime(nome_arquivo)
        data_modificacao = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime(modificacao))
        print(f"✏️ Última modificação: {data_modificacao}")
        
        # 4. Localização absoluta (onde ele está escondido no HD)
        caminho_real = os.path.abspath(nome_arquivo)
        print(f"📍 Caminho no sistema: {caminho_real}")
        
        print("----------------------------------------\n")
        
    else:
        print("❌ Erro: Arquivo não encontrado! Garanta que ele está na mesma pasta que este script.\n")
