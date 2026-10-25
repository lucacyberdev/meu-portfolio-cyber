import time

print("=== SISTEMA DE LOGS DE DEFESA CIBERNÉTICA ===")
print("(Digite 'sair' no nome do usuário para fechar)\n")

# O robô cria ou abre um arquivo de texto real para salvar os registros
with open("seguranca_log.txt", "a", encoding="utf-8") as arquivo_log:
    arquivo_log.write(f"--- SESSÃO DE MONITORAMENTO INICIADA EM {time.strftime('%d/%m/%Y %H:%M:%S')} ---\n")

while True:
    usuario = input("Digite o nome do usuário que tentou acessar o sistema: ")
    
    if usuario.lower() == 'sair':
        print("\nMonitoramento de logs encerrado. Verifique o arquivo 'seguranca_log.txt'!")
        break
        
    print("\nQual foi o status do login?")
    print("1 - Sucesso (Acesso permitido)")
    print("2 - Falha (Senha incorreta)")
    print("3 - Suspeito (Tentativa de invasão detectada)")
    
    status_opcao = input("Escolha o status (1, 2 ou 3): ")
    
    horario_atual = time.strftime('%H:%M:%S')
    
    # Define a mensagem com base no que aconteceu
    if status_opcao == '1':
        evento = f"[{horario_atual}] ✅ USUÁRIO: {usuario} | STATUS: Login efetuado com sucesso."
    elif status_opcao == '2':
        evento = f"[{horario_atual}] ⚠️ USUÁRIO: {usuario} | STATUS: Falha de login (Senha incorreta)."
    elif status_opcao == '3':
        evento = f"[{horario_atual}] 🚨 ALERTA MÁXIMO: {usuario} tentou burlar o sistema! IP Bloqueado pelo Firewall."
    else:
        print("❌ Opção inválida! Registro cancelado.\n")
        continue
        
    # Mostra na tela preta do CMD
    print(f"\n{evento}")
    
    # SALVA DE VERDADE no arquivo de texto do seu computador!
    with open("seguranca_log.txt", "a", encoding="utf-8") as arquivo_log:
        arquivo_log.write(evento + "\n")
        
    print("📌 Registro salvo no arquivo 'seguranca_log.txt'.\n----------------------------------------\n")
