senha = "145544"
tentativas = 0

pedir_senha = input("Digite a senha: ")
tentativas += 1

while pedir_senha != senha:
    print("Senha inválida, tente novamente.")

    pedir_senha = input("Digite a senha: ")
    tentativas += 1

print("Você acertou!")
print("Tentativas:", tentativas)
