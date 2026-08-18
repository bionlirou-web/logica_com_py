# cadastro do nome

nome = input("Digite o seu nome: ")

nome = nome.strip()

print(nome)

# indica contagem de caracteres igual ou maior que cinco
if len((nome)) >= 5:
    print("Número com cinco caracteres ou mais.")
else:
    ("Número com menos de cinco caracteres.")

letra_a_nome = nome.count("a")

print(letra_a_nome)

# cadastro da idade

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("De maior.")
else:
    print("De menor.")

# cadastro da cidade

cidade = input("Digite a cidade: ")

cidade = cidade.strip()

print(cidade)

# cadastro palavra-chave

palavra_chave = input("Digite a palavra-chave: ")

if palavra_chave in nome:
    print("Há palavra-chave no nome.")
else:
    print("Não há palavra-chave no nome.")

if palavra_chave in cidade:
    print("Há palavra-chave na cidade.")
else:
    print("Não há palavra-chave na cidade.")

# encerrar programa: relatório final

print("Programa encerrado")
