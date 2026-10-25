import time

print("=== SIMULADOR DE ATAQUE DE FORÇA BRUTA (ETHICAL HACKING) ===")
print("(Digite 'sair' na senha para fechar o programa)\n")

# Nossa Wordlist: as senhas mais comuns e fracas do mundo que o robô já conhece
lista_senhas_comuns = [
    "123456", "senha", "123456789", "admin", "12345", 
    "password", "root", "luca123", "hackeme", "computador"
]

while True:
    # Você define uma senha secreta para ver se o robô consegue adivinhar
    senha_alvo = input("Defina uma senha para o teste de invasão: ")
    
    if senha_alvo.lower() == 'sair':
        print("\nSimulador encerrado. Mantenha suas senhas seguras!")
        break
        
    print(f"\n[{time.strftime('%H:%M:%S')}] Iniciando ataque de força bruta contra a senha...")
    print("--------------------------------------------------")
    
    quebrou = False
    tentativas = 0
    
    # O robô começa a testar cada palavra da lista dele em alta velocidade
    for senha_teste in lista_senhas_comuns:
        tentativas += 1
        print(f"[-] Tentativa {tentativas}: Testando a senha '{senha_teste}'...")
        time.sleep(0.3) # Simula o robô processando na rede
        
        if senha_teste == senha_alvo:
            quebrou = True
            break
            
    print("--------------------------------------------------")
    
    if quebrou:
        print(f"🚨 ALERTA DE VULNERABILIDADE! O robô QUEBROU a sua senha! ❌")
        print(f"🔑 Senha descoberta: '{senha_teste}' em apenas {tentativas} tentativas.")
        print("💡 DICA: Nunca use senhas óbvias ou palavras comuns de dicionário!\n")
    else:
        print(f"🛡️ SEGURA! O robô testou toda a lista e NÃO conseguiu quebrar sua senha. ✅")
        print("💡 Lembre-se: Senhas longas com números e símbolos barram ataques comuns.\n")
