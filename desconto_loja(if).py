resposta1 = input("Você tem o cartão da loja? (s/n): ")
resposta2 = input("Você tem o programa de validação? (s/n): ")

resultado = resposta1 or resposta2 

if not resultado:
    print("Você não possui o desconto.")
else:
    print("Você possui o desconto")
