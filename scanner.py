import socket

print("=== MEU PRIMEIRO SCANNER DE PORTAS ===")
print("(Digite 'sair' no endereço para fechar)\n")

while True:
    # Pede o site ou IP que você quer escanear (ex: google.com ou localhost)
    alvo = input("Digite o site ou IP para escanear: ")
    
    if alvo.lower() == 'sair':
        print("Scanner desligado. Até mais!")
        break
        
    print("\n[!] Iniciando varredura... Isso pode levar alguns segundos.")
    print("----------------------------------------")
    
    # Lista das portas mais importantes e comuns da internet para testar
    portas_para_testar = [21, 22, 23, 25, 80, 443, 8080]
    
    try:
        # Resolve o nome do site para o IP real dele
        ip_alvo = socket.gethostbyname(alvo)
        print(f"Alvo traduzido para o IP: {ip_alvo}\n")
        
        for porta in portas_para_testar:
            # Cria a conexão de teste de rede (AF_INET = IP, SOCK_STREAM = TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Define um tempo limite de 1 segundo para não travar o programa
            s.settimeout(1.0)
            
            # Tenta se conectar na porta
            resultado = s.connect_ex((ip_alvo, porta))
            
            # Se o resultado for 0, significa que a porta respondeu e está ABERTA!
            if resultado == 0:
                print(f"🔓 Porta {porta}: ABERTA (Alerta de Segurança se não for usada!)")
            else:
                print(f"🔒 Porta {porta}: Fechada / Protegida")
                
            s.close() # Fecha o teste daquela porta
            
        print("----------------------------------------")
        print("Varredura concluída com sucesso.\n")
        
    except socket.gaierror:
        print("❌ Erro: Não consegui encontrar esse site. Digite corretamente (ex: google.com).\n")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}\n")
