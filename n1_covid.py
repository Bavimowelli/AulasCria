""" Province_State[2],Country_Region[3]
Confirmed[6],Deaths[7]
0. Estabelecer 3 questões de pesquisa sobre os dados
1. Carregar Dados
2. Explorar dados
3. Responder questões de pesquisa
4. Responder questões gráficamente
"""
import os
import matplotlib.pyplot as plt
import numpy as np
def clear():
    os.system('cls||clear')

def pause():
    input("Aperte enter para continuar...")

def sobre():
    clear()
    print("O programa tem como objetivo auxiliar na busca de dados sobre a covid 19\n")
    pause()

def buscaDados(file):
    clear()
    country = input("Digite o país que você deseja pesquisar: ")
    deaths = []
    confirmed = 0
    for line in file:
        dados = line.split(",")
        if (dados[3] == country):
            deaths.append(int(dados[8]))
            confirmed += int(dados[7])
    print("O país pesquisado:", country,
          "\nNúmero de mortes:", np.sum(deaths, axis=0),
           "\nNúmero de casos confirmados:", confirmed)
    pause()
    graph(deaths, country)
    file.seek(0)

def graph(deaths, country):
    fig, ax = plt.subplots()
    ax.bar(country, deaths)
    ax.set_title(f"Quantidade de mortes no(a) {country}")
    fig.savefig(f"Grafico_{country}.pdf")

    plt.show()


def opening(file):
    opt=0
    while(opt!=3):
        clear()
        opt = int(input("1 - Sobre"
                        "\n2 - Dados"
                        "\n3 - Sair\n"))
        if (opt==1):
            sobre()
        elif (opt==2):
            buscaDados(file)

f = open("covid-03-31-2022.csv", "r")
opening(f)
f.close()
