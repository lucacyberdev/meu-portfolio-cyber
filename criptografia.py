print("=== CRIPTOGRAFADOR DE MENSAGENS INDESTRUTÍVEL ===")
print("(Baseado na Cifra de César - Proteção Total)\n")

while True:
    print("O que você deseja fazer?")
    print("[1] Criptografar uma mensagem")
    print("[2] Descriptografar uma mensagem")
    print("[3] Sair do programa")
    
    opcao = input("Escolha uma opção (1, 2 ou 3): ")
    
    if opcao == '3':
        print("\nSistema encerrado. Suas mensagens estão seguras!")
        break
        
    if opcao not in ['1', '2']:
        print("\n❌ Opção inválida! Digite apenas 1, 2 ou 3.\n")
        continue
        
    mensagem = input("\nDigite a mensagem: ")
    
    try:
        chave = int(input("Digite a chave secreta (um número de 1 a 25): "))
    except ValueError:
        print("\n❌ Erro: A chave deve ser um número inteiro!\n")
        continue
        
    # Se o usuário escolheu descriptografar, a gente inverte o sentido da chave
    if opcao == '2':
        chave = -chave
        
    mensagem_final = ""
    
    # Lógica de Hacker para andar no alfabeto
    for letra in mensagem:
        if letra.isalpha(): # Verifica se é uma letra (ignora espaços e números)
            maiuscula = letra.isupper()
            letra = letra.lower()
            
            # Código mágico que faz a letra pular as casas do alfabeto e voltar para o 'A' se passar do 'Z'
            codigo = ord(letra) + chave
            if codigo > ord('z'):
                codigo -= 26
            elif codigo < ord('a'):
                codigo += 26
                
            letra_cripto = chr(codigo)
            
            # Devolve a letra para maiúscula se ela era maiúscula antes
            if maiuscula:
                letra_cripto = letra_cripto.upper()
                
            mensagem_final += letra_cripto
        else:
            mensagem_final += letra # Se for espaço ou símbolo, deixa igual
            
    if opcao == '1':
        print(f"\n🔒 MENSAGEM CRIPTOGRAFADA: {mensagem_final}")
    else:
        print(f"\n🔓 MENSAGEM REVELADA: {mensagem_final}")
        
    print("--------------------------------------------------\n")
