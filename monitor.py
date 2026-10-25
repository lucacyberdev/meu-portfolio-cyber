import urllib.request
import time

print("=== UPTIME BOT: MONITOR DE SITES ===")
print("(Digite 'sair' no endereço para fechar o monitor)\n")

# Pede o site que você quer monitorar
site_alvo = input("Digite o site (ex: https://google.com): ")

if site_alvo.lower() != 'sair':
    # Garante que o endereço começa com http se o usuário esquecer
    if not site_alvo.startswith("http://") and not site_alvo.startswith("https://"):
        site_alvo = "https://" + site_alvo

    print(f"\n[!] Monitorando o alvo: {site_alvo}")
    print("[!] O robô vai checar o status a cada 5 segundos. Pressione CTRL + C no CMD para forçar a parada.\n")

    while True:
        try:
            print(f"[{time.strftime('%H:%M:%S')}] Checando servidor...")
            
            # O robô tenta abrir o site na internet com um tempo limite de 3 segundos
            resposta = urllib.request.urlopen(site_alvo, timeout=3)
            
            # Código 200 na internet significa 'OK / Sucesso'
            if resposta.getcode() == 200:
                print(f"🟢 STATUS: ONLINE! O site está respondendo perfeitamente.\n")
                
        except Exception as e:
            # Se der qualquer erro (como falta de internet ou site fora do ar), o alarme toca!
            print(f"🚨 ALERTA: SITE FORA DO AR OU INSTÁVEL!")
            print(f"❌ Motivo do erro: {e}\n")
            
        # Faz o robô esperar 5 segundos antes de testar o site novamente
        time.sleep(5)
