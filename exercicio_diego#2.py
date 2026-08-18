# Variáveis para quantidade de vezes de repetições na lousa

frase = input("Digite a frase que o Bart terá que escrever na lousa: ")

quantidade = int(input("Digite a quantidade de vezes que ele terá que escrever: "))

# Análise das entradas

for i in range(quantidade):
    print(f"{frase}")
