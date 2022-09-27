'''
Título: Desafio - Cachorros-Quentes
Autor: João Henrique
Data: 27/09/2022

Desafio
Em 2012 foi alcançado um novo recorde mundial na famosa Competição de Cachorros-Quentes do Nathan: o campeão, Joey Chestnut, devorou 68 cachorros-quentes em dez minutos, um aumento incrível em relação aos 62 sanduíches devorados pelo mesmo Chestnut em 2011.

O restaurante Nathan’s Famous Corporation, localizado no Brooklyn, NY, é o responsável pela competição. Eles produzem deliciosos cachorros-quentes, mundialmente famosos, mas quando o assunto é matemática eles não são tão bons. Eles desejam ser listados no Livro de Recordes do Guinness, mas para isso devem preencher um formulário descrevendo os fatos básicos da competição. Em particular, eles devem informar o número médio de cachorros-quentes consumidos pelos participantes durante a competição.

Você pode ajudá-los? Eles prometeram pagá-lo com um dos seus saborosos cachorros-quentes. Dados o número total de cachorros-quentes consumidos e o número total de participantes na competição, você deve escrever um programa para determinar o número médio de cachorros-quentes consumidos pelos participantes.

Entrada
A entrada consiste de uma única linha que contém dois inteiros H e P (1 ≤ H, P ≤ 1000) indicando respectivamente o número total de cachorros-quentes consumidos e o número total de participantes na competição.

Saída
Seu programa deve produzir uma única linha com um número racional representando o número médio de cachorros-quentes consumidos pelos participantes. O resultado deve ser escrito como um número racional com exatamente dois dígitos após o ponto decimal, arredondado se necessário.
'''

print("""
    ---------------------------------------------------
            :: DESAFIO - CACHORROS QUENTES::
    ---------------------------------------------------
""")

# ENTRADA DAS INFORMAÇÕES COM TRATAMENTO
while True:
    total_cachorros_quentes_consumidos = input("Informe o número total de cachorros-quentes consumidos: ")

    if total_cachorros_quentes_consumidos.isnumeric() == False:
        print("O valor deverá ser um númerio inteiro!!!\n")
    else:
        n_total_cachorros_quentes_consumidos = int(total_cachorros_quentes_consumidos)
        
        if n_total_cachorros_quentes_consumidos <= 0 or n_total_cachorros_quentes_consumidos > 1000:
            print("O valor deverá ser maior que zero ou menor que 1000!!!")
        else:
            break

while True:
    total_participantes_competicao = input("Informe o número total de participantes na competição: ")

    if total_participantes_competicao.isnumeric() == False:
        print("O valor deverá ser um númerio inteiro!!!\n")
    else:
        n_total_participantes_competicao = int(total_participantes_competicao)
        
        if n_total_participantes_competicao <= 0 or n_total_participantes_competicao > 1000:
            print("O valor deverá ser maior que zero ou menor que 1000!!!")
        else:
            break

#CALCULO DA MÉDIA

media = n_total_cachorros_quentes_consumidos / n_total_participantes_competicao

print(f"O número médio de cachorros-quentes consumidos pelos participantes é de: {media:.2f}")