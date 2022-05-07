""" Province_State[2],Country_Region[3]
Confirmed[7],Deaths[8]
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
    print("O programa busca no maximo 5 paises\n")
    pause()

def inputData():
    country = input("Digite o país que você deseja pesquisar: ")
    return country

def showData(country, confirmed, deaths):
   print("O país pesquisado:", country,
          "\nNúmero de mortes:", deaths,
           "\nNúmero de casos confirmados:", confirmed)
   pause()

def searchData(file, country):
    deaths = 0
    confirmed = 0
    for line in file:
        dados = line.split(",")
        if (dados[3] == country):
            deaths += int(dados[8])
            confirmed += int(dados[7])
    file.seek(0)
    return confirmed, deaths
    

def graph(country, deaths):
    fig, ax = plt.subplots()
    ax.bar(country, deaths)
    ax.set_xlabel("Países")
    ax.set_ylabel("Mortes")
    ax.set_title("Quantidade de mortes nos por países")
    fig.savefig("Grafico_paises.pdf")

    plt.show()


def opening(file):
    opt=0
    cont=0
    country = []
    deaths = []
    while(opt!=3):
        death = []
        clear()
        opt = int(input("1 - Sobre"
                        "\n2 - Dados"
                        "\n3 - Sair\n"))
        if (opt==1):
            sobre()
        elif (opt==2):
            country.append(inputData())
            confirmed, d1 = searchData(file, country[cont])
            showData(country[cont], confirmed, d1)
            deaths.append(d1)
            cont+=1
            if (cont==5):
                return country, deaths
        elif (opt==3):
            return country, deaths

f = open("covid-03-31-2022.csv", "r")
country = []
deaths = []
country, deaths = opening(f)
graph(country, deaths)
f.close()
