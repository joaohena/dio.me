'''
Título: Desafio - As duas torres
Autor: João Henrique
Data: 27/09/2022

Desafio
Saruman, o Branco, um grande mago da Terra-média, traiu os bons costumes e se filiou ao lorde do mal, Sauron. Sauron comanda a torre de Minas Morgul, que abriga um dos seus mais temidos servos, o Rei Bruxo de Angmar, um dos Nazgûl (antigos reis humanos que foram corrompidos pelos poderes dos anéis de Sauron). Saruman comanda a torre de Orthanc, onde cria seus servos Uruk-hai, orcs mais terríveis que os convencionais. Para comunicação, eles utilizam as relíquias esféricas chamadas Palantír, que ficam no topo de suas torres.
A Terra-média avança cada vez mais em tecnologia, muito impulsionada pelas guerras que a acometem diariamente. Um dos problemas que tem atrapalhado sua população é a Interferência de Comunicação Mágica (ICM). Os estudiosos de Minas Tirith, grande cidadela de Gondor, concluíram que para calcular o ICM para Palantír’s, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos. Gandalf, o Cinza, chegou a questionar essa conclusão, alegando que ela não fazia muito sentido, mas ele mesmo concluiu que dar sentido às coisas não faz sentido.
Saruman e Sauron precisam de uma comunicação estável, pois têm medo que Frodo e seus amigos consigam atrapalhar seus planos, portanto, querem saber quanto de ICM há na comunicação de seus Palantír’s, para que saibam quanto de magia devem empregar na comunicação.

Entrada
A entrada é composta por 3 inteiros, N(0 < N < 10000), X e Y(0 < X, Y < 100), que indicam, respectivamente, a distância entre os Palantír, o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.

Saída
Um valor real indicando o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais.
'''

print("""
    ---------------------------------------------------
              :: DESAFIO - AS DUAS TORRES::
    ---------------------------------------------------
""")

# ENTRADA DAS INFORMAÇÕES COM TRATAMENTO
while True:
    distancia_entre_palantir = input("Informe a distância entre os Palantír: ")

    if distancia_entre_palantir.isnumeric() == False:
        print("O valor deverá ser um númerio inteiro!!!\n")
    else:
        n_distancia_entre_palantir = int(distancia_entre_palantir)
        
        if n_distancia_entre_palantir <= 0 or n_distancia_entre_palantir >= 10000:
            print("O valor deverá ser maior que zero ou menor que 10000!!!")
        else:
            break

while True:
    diametro_palantir_Sauron = input("Informe o diâmetro do Palantír de Sauron: ")

    if diametro_palantir_Sauron.isnumeric() == False:
        print("O valor deverá ser um númerio inteiro!!!\n")
    else:
        x_diametro_palantir_Sauron = int(diametro_palantir_Sauron)

        if x_diametro_palantir_Sauron <= 0 or x_diametro_palantir_Sauron >= 100:
            print("O valor deverá ser maior que zero ou menor que 100!!!")
        else:
            break

while True:
    diametro_palantir_Saruman = input("Informe o diâmetro do Palantír de Saruman: ")

    if diametro_palantir_Saruman.isnumeric() == False:
        print("O valor deverá ser um númerio inteiro!!!\n")
    else:
        y_diametro_palantir_Saruman = int(diametro_palantir_Saruman)
        
        if y_diametro_palantir_Saruman <= 0 or y_diametro_palantir_Saruman >= 100:
            print("O valor deverá ser maior que zero ou menor que 100!!!")
        else:
            break

#CALCULO DO ICM

valor_icm = n_distancia_entre_palantir / (x_diametro_palantir_Sauron + y_diametro_palantir_Saruman)

print(f"O ICM é: {valor_icm:.2f}")