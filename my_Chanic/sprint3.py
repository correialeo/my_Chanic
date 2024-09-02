import csv
import pandas as pd

def read_file(path_csv):
    with open(path_csv, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        dados = list(reader)
    return dados

data = read_file('../problemas_veiculares.csv')

def create(data):
    problema = input('Qual é o problema?')
    sintoma = input('Qual é o sintoma do problema?')
    causa = input('Qual é a causa do problema?')
    solucao = input('Qual é a solução para o problema descrito a cima?')

    new_problem = {'problema':problema, 'sintoma':sintoma, 'causa':causa, 'solucao':solucao}
    data.append(new_problem)
    print('Novo dado inserido com sucesso')

def read(data):
    for i in (len(data)):
        print(i)

# def update(data):
#     try:
#
#     except: