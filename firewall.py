import time

print("=== SIMULADOR DE FIREWALL DE REDE ===")
print("(Digite 'sair' no endereço de IP para fechar)\n")

# Nossa lista negra de IPs de hackers conhecidos no mundo fictício
lista_negra_ips = ["192.168.1.50", "10.0.0.99", "200.150.30.40"]

print("[+] Firewall ATIVADO e monitorando tráfego de rede...")
print(f"[📌] IPs Bloqueados no banco de dados: {lista_negra_ips}\n----------------------------------------")

while True:
    ip_conexao = input("IP tentando se conectar à rede: ")
    
    if ip_conexao.lower() == 'sair':
        print("\nFirewall desativado de forma segura.")
        break
        
    print(f"[{time.strftime('%H:%M:%S')}] Analisando pacote de dados do IP {ip_conexao}...")
    time.sleep(1.5) # Simula o porteiro pensando e checando o livro de regras
    
    # Lógica do Firewall: Checa se o IP está na lista negra
    if ip_conexao in lista_negra_ips:
        print(f"🚨 ACESSO BLOQUEADO! O IP {ip_conexao} está na lista negra de hackers. Conexão derrubada! ❌\n")
    else:
        # Regra secundária: simula se o IP parece um IP válido ou texto aleatório
        if len(ip_conexao) < 7 or not ip_conexao.replace(".", "").isdigit():
            print("⚠️ PACOTE SUSPEITO: Formato de IP inválido. Bloqueado por precaução!\n")
        else:
            print(f"🟢 ACESSO PERMITIDO! IP {ip_conexao} seguro. Pacote enviado com sucesso. ✅\n")
            
    print("----------------------------------------")
