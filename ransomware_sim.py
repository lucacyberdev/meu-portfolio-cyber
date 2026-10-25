import os

print("=== SIMULADOR DE RANSOMWARE (DEFESA CIBERNÉTICA) ===")
print("(Este script simula o travamento e destravamento de arquivos)\n")

arquivo_alvo = "documento.txt"
chave_secreta = 10  # A nossa chave para trancar e destrancar

while True:
    print("O que você deseja fazer?")
    print("1 - Trancar o arquivo (Simular Ataque)")
    print("2 - Destrancar o arquivo (Simular Defesa/Vacina)")
    print("3 - Sair")
    
    opcao = input("Escolha (1, 2 ou 3): ")
    
    if opcao == '3':
        print("\nSistema encerrado.")
        break
        
    if opcao in ['1', '2']:
        if not os.path.exists(arquivo_alvo):
            print(f"❌ Erro: O arquivo '{arquivo_alvo}' não foi encontrado nesta pasta!\n")
            continue
            
        with open(arquivo_alvo, "r", encoding="utf-8") as f:
            conteudo = f.read()
            
        conteudo_alterado = ""
        
        for caractere in conteudo:
            if opcao == '1':
                conteudo_alterado += chr(ord(caractere) + chave_secreta)
            else:
                conteudo_alterado += chr(ord(caractere) - chave_secreta)
                
        with open(arquivo_alvo, "w", encoding="utf-8") as f:
            f.write(conteudo_alterado)
            
        if opcao == '1':
            print(f"🚨 ATAQUE CONCLUÍDO! O arquivo '{arquivo_alvo}' foi criptografado e está ilegível.\n")
        else:
            print(f"🟢 DEFESA CONCLUÍDA! O arquivo '{arquivo_alvo}' foi restaurado com sucesso.\n")
            
    else:
        print("❌ Opção inválida!\n")
