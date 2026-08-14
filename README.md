#Calculo de sensores

#Etapa 1: Registrar informações

print("Os sensores de Bradley registram três valores.\n"
      "Os sensores A e B registram números para atravessar um corredor de uma ponta a outra para a direita, sendo:\n"
        "Sensor A 5m\n"
        "Sensor B 8m.\n"
      "Já o Sensor C registra o retorno do robô, calculando um valor de 3m.\n"
        "Quantos metros Bradley percorreu?")

valor_1 = int(input("Digite o valor registrado no Sensor A: "))
valor_2 = int(input("Digite o valor registrado no Sensor B: "))
valor_3 = int(input("Digite o valor registrado no Sensor C: "))

#Calculo

soma = valor_1 + valor_2 - valor_3

#Resposta

print("O valor do cálculo é justamente {}".format(soma))

#Fim do cálculo
