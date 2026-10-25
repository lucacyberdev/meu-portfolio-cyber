import string

print("=== VERIFICADOR DE SENHAS 2.0: CAÇADOR DE SÍMBOLOS ===")
print("(Digite 'sair' para encerrar o programa)\n")

while True:
    senha = input("Digite uma senha para analisar o nível de força: ")
    
    if senha.lower() == 'sair':
        print("\nAnalisador encerrado. Mantenha suas contas seguras!")
        break
        
    tamanho = len(senha)
    
    # Se a senha for muito curta, o sistema barra na hora
    if tamanho < 8:
        print("❌ REJEITADA: Senhas precisam ter pelo menos 8 caracteres!\n----------------------------------------\n")
        continue

    # Nossas variáveis de checagem (começam como Falso)
    tem_maiuscula = any(char.isupper() for char in senha)
    tem_minuscula = any(char.islower() for char in senha)
    tem_numero = any(char.isdigit() for char in senha)
    
    # Checa se tem algum símbolo especial (como @, #, $, %, etc.)
    tem_simbolo = any(char in string.punctuation for char in senha)
    
    # Contagem de pontos (Nota de 0 a 4)
    pontos = sum([tem_maiuscula, tem_minuscula, tem_numero, tem_simbolo])
    
    print("\n🔍 [RELATÓRIO DE PERÍCIA DA SENHA]")
    print(f"🔠 Tem Letra Maiúscula? {'✅ Sim' if tem_maiuscula else '❌ Não'}")
    print(f"🔡 Tem Letra Minúscula? {'✅ Sim' if tem_minuscula else '❌ Não'}")
    print(f"🔢 Tem Número?           {'✅ Sim' if tem_numero else '❌ Não'}")
    print(f"🎨 Tem Símbolo (@,#,$)?  {'✅ Sim' if tem_simbolo else '❌ Não'}")
    
    # Classificação final com base nos pontos
    if pontos == 4:
        print("🛡️ STATUS: ULTRA-SEGURA! Essa senha é um escudo indestrutível.")
    elif pontos == 3:
        print("⚠️ STATUS: MÉDIA! Adicione o tipo de caractere que falta para proteger mais.")
    else:
        print("❌ STATUS: FRACA! Muito fácil de ser quebrada por robôs de força bruta.")
        
    print("----------------------------------------\n")
