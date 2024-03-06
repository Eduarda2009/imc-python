        # módulo imc

import estado_imc as calcular

peso = 0
altura = 0.0
nome = ""

nome = input("qual o nome do paciente? ")


erro = True
while erro:
    try:
        peso = int(input("qual o peso do paciente? "))
        erro = False
    except:
        print("valor invalido!")


erro = True
while erro:
    try:
        altura = float(input("qual é a altura do paciente? "))
        erro = False
    except:
        print("valor invalido!")


calcular.calcular_imc(peso, altura)




















