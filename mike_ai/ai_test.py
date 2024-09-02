import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

import pandas as pd
import re

problemas = pd.read_csv('../problemas_veiculares.csv')

#função para processar a mensagem de entrada
def processar_mensagem(mensagem, problemas):
    #remover pontuação e converter para minúsculas
    mensagem = re.sub(r'[^\w\s]', '', mensagem.lower())

    #tokenizar a mensagem
    tokens = mensagem.split()

    #procurar por causa ou sintoma na mensagem
    for index, row in problemas.iterrows():
        causa = row['causa'].lower()
        sintoma = row['sintoma'].lower()

        if causa in mensagem or sintoma in mensagem:
            problema = row['problema']
            solucao = row['solucao']
            return problema, solucao

    return None, "Nenhuma correspondência encontrada."


#teste
mensagem_exemplo = "Olá,meu carro está com uma luz de aviso no painel"
problema, solucao = processar_mensagem(mensagem_exemplo, problemas)

if problema:
    print(f"Olá, de acordo com minha análise, a solução para seu carro é {solucao.lower()}")
else:
    print(solucao)
