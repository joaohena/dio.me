'''
Título: Desafio - Cálculo de viagem
Autor: João Henrique
Data: 27/09/2022

Desafio
Rubens quer calcular e mostrar a quantidade de litros de combustível gastos em uma viagem de carro, sendo que seu carro faz 12 KM/L. Como ele não sabe fazer um programa que o auxilie nessa missão, ele te pede ajuda. Para efetuar o cálculo, deve-se fornecer o tempo gasto em horas na viagem e a velocidade média durante a mesma em km/h. Assim, você conseguirá passar para Rubens qual a distância percorrida e, em seguida, calcular quantos litros serão necessários para a viagem que ele quer fazer. Mostre o valor com 3 casas decimais após o ponto.

Entrada
O arquivo de entrada contém dois inteiros. O primeiro é o tempo gasto na viagem em horas e o segundo é a velocidade média durante a mesma em km/h.

Saída
Imprima a quantidade de litros necessária para realizar a viagem, com três dígitos após o ponto decimal
'''

print("""
    ---------------------------------------------------
              :: DESAFIO - CALCULO DE VIAGEM::
    ---------------------------------------------------
""")

consumo = 12

# ENTRADA DAS INFORMAÇÕES COM TRATAMENTO
while True:
    tempo_gasto_viagem = input("Informe o tempo gasto na viagem em horas: ")

    if tempo_gasto_viagem.isnumeric() == False:
        print("O valor deverá ser um númerio inteiro!!!\n")
    else:
        n_tempo_gasto_viagem = int(tempo_gasto_viagem)
        
        if n_tempo_gasto_viagem <= 0:
            print("O valor deverá ser maior que zero!!!")
        else:
            break

while True:
    velocidade_media = input("Informe a velocidade média durante a mesma em km/h: ")

    if velocidade_media.isnumeric() == False:
        print("O valor deverá ser um númerio inteiro!!!\n")
    else:
        n_velocidade_media = int(velocidade_media)
        
        if n_velocidade_media <= 0:
            print("O valor deverá ser maior que zero!!!")
        else:
            break

#CALCULO DA QUANTIDADE EM LITROS

litros = (n_tempo_gasto_viagem * n_velocidade_media) / consumo

print(f"A quantidade de litros necessária para realizar a viagem é: {litros:.3f}")