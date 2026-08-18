numeros = []
pares = 0

for c in range(5):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

print(f"lista {numeros}")

for numero in numeros:
    if numero % 2 == 0:
        pares += 1

print(f"Quantidade de números pares: {pares}")
