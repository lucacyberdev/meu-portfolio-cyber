import random
import string

print("=== GERADOR DE SENHAS INFINITO ===")
print("(Digite 'sair' para fechar o programa)\n")

# Nosso caldeirão de caracteres (letras, números e símbolos)
todos_os_caracteres = string.ascii_letters + string.digits + string.punctuation

while True:
    comando = input("Digite o tamanho da senha desejado: ")
    
    # Condição para sair do loop
    if comando.lower() == 'sair':
        print("Gerador fechado. Proteja bem suas senhas!")
        break
        
    # Proteção para o programa não quebrar se digitarem errado
    try:
        tamanho = int(comando) # Tenta transformar o texto em número
        
        if tamanho <= 0:
            print("❌ Erro: O tamanho deve ser maior que 0!\n")
            continue # Volta para o começo do loop
            
        # Sorteia os caracteres aleatórios e junta tudo numa senha
        senha_gerada = "".join(random.choice(todos_os_caracteres) for i in range(tamanho))
        
        print("\n🛡️ SENHA GERADA COM SUCESSO:")
        print(f"👉 {senha_gerada}")
        print("----------------------------------------\n")
        
    except ValueError:
        # Se a pessoa digitar letras em vez de números, o programa avisa e continua rodando
        print("❌ Erro: Por favor, digite apenas NÚMEROS inteiros (ex: 12) ou 'sair'.\n")
