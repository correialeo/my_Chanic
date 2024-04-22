import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

superaquecimento = pd.read_csv('superaquecimento.csv')
trinca_bloco = pd.read_csv('trinca_de_bloco.csv')
barulho_motor = pd.read_csv('barulho_no_motor.csv')
vazamento_oleo = pd.read_csv('vazamento_oleo.csv')

# print(superaquecimento.head())
# print(trinca_bloco.head())
# print(barulho_motor.head())
# print(vazamento_oleo.head())
# print('-----------------')
#
# print(superaquecimento.dtypes)
# print(trinca_bloco.dtypes)
# print(barulho_motor.dtypes)
# print(vazamento_oleo.dtypes)
# print('-----------------')
#
# print(superaquecimento.describe())
# print(trinca_bloco.describe())
# print(barulho_motor.describe())
# print(vazamento_oleo.describe())
# print('-----------------')
#
# print(superaquecimento.isnull().sum())
# print(trinca_bloco.isnull().sum())
# print(barulho_motor.isnull().sum())
# print(vazamento_oleo.isnull().sum())

if superaquecimento.isnull().sum().any() or trinca_bloco.isnull().sum().any() or barulho_motor.isnull().sum().any() or vazamento_oleo.isnull().sum().any():
    print('Valores ausentes encontrados')

var_cat_superaquecimento = superaquecimento.select_dtypes(include='object')
var_cat_trinca_bloco = trinca_bloco.select_dtypes(include='object')
var_cat_barulho_motor = barulho_motor.select_dtypes(include='object')
var_cat_vazamento = vazamento_oleo.select_dtypes(include='object')

from sklearn.preprocessing import OneHotEncoder

encoder_superaquecimento = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoder_trinca_bloco = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoder_barulho_motor = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoder_vazamento = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

encoder_superaquecimento.fit(var_cat_superaquecimento)
encoder_trinca_bloco.fit(var_cat_trinca_bloco)
encoder_barulho_motor.fit(var_cat_barulho_motor)
encoder_vazamento.fit(var_cat_vazamento)

var_cat_sup_encoded = pd.DataFrame(encoder_superaquecimento.transform(var_cat_superaquecimento))
var_cat_trinca_encoded = pd.DataFrame(encoder_trinca_bloco.transform(var_cat_trinca_bloco))
var_cat_barulho_motor_encoded = pd.DataFrame(encoder_barulho_motor.transform(var_cat_barulho_motor))
var_cat_vazamento_encoded = pd.DataFrame(encoder_vazamento.transform(var_cat_vazamento))

var_cat_sup_encoded.columns = [f"cat_{i}" for i in range(var_cat_sup_encoded.shape[1])]
var_cat_trinca_encoded.columns = [f'cat_{i}' for i in range(var_cat_trinca_encoded.shape[1])]
var_cat_barulho_motor_encoded.columns = [f'cat_{i}' for i in range(var_cat_barulho_motor_encoded.shape[1])]
var_cat_vazamento_encoded.columns = [f'cat_{i}' for i in range(var_cat_vazamento_encoded.shape[1])]

superaquecimento_preproc = pd.concat([superaquecimento.select_dtypes(exclude='object'), var_cat_sup_encoded], axis=1)
trinca_preproc = pd.concat([trinca_bloco.select_dtypes(exclude='object'), var_cat_trinca_encoded], axis=1)
barulho_preproc = pd.concat([barulho_motor.select_dtypes(exclude='object'), var_cat_barulho_motor_encoded], axis=1)
vazamento_preproc = pd.concat([vazamento_oleo.select_dtypes(exclude='object'), var_cat_vazamento_encoded], axis=1)

var_num_superaquecimento = superaquecimento_preproc.select_dtypes(include='number')
var_num_trinca = superaquecimento_preproc.select_dtypes(include='number')
var_num_barulho = barulho_preproc.select_dtypes(include='number')
var_num_vazamento = vazamento_preproc.select_dtypes(include='number')

from sklearn.preprocessing import StandardScaler

scaler_superaquecimento = StandardScaler()
scaler_trinca = StandardScaler()
scaler_barulho = StandardScaler()
scaler_vazamento = StandardScaler()

scaler_superaquecimento.fit(var_num_superaquecimento)
scaler_trinca.fit(var_num_trinca)
scaler_barulho.fit(var_num_barulho)
scaler_vazamento.fit(var_num_vazamento)

var_num_sup_scaled = pd.DataFrame(scaler_superaquecimento.transform(var_num_superaquecimento))
var_num_trinca_scaled = pd.DataFrame(scaler_trinca.transform(var_num_trinca))
var_num_barulho_scaled = pd.DataFrame(scaler_barulho.transform(var_num_barulho))
var_num_vazamento_scaled = pd.DataFrame(scaler_vazamento.transform(var_num_vazamento))

var_num_sup_scaled.columns = [f'cat_{i}' for i in range(var_num_sup_scaled.shape[1])]
var_num_trinca_scaled.columns = [f'cat_{i}' for i in range(var_num_trinca_scaled.shape[1])]
var_num_barulho_scaled.columns = [f'cat_{i}' for i in range(var_num_barulho_scaled.shape[1])]
var_num_vazamento_scaled.columns = [f'cat_{i}' for i in range(var_num_vazamento_scaled.shape[1])]

superaquecimento_final = pd.concat([var_cat_sup_encoded, var_num_sup_scaled], axis=1)
trinca_final = pd.concat([var_cat_trinca_encoded, var_num_trinca_scaled], axis=1)
barulho_final = pd.concat([var_cat_barulho_motor_encoded, var_num_barulho_scaled], axis=1)
vazamento_final = pd.concat([var_cat_vazamento_encoded, var_num_vazamento_scaled], axis=1)

citroen_dados = pd.concat([superaquecimento_final, trinca_final, barulho_final, vazamento_final], axis=1)
print(citroen_dados.head())
print(citroen_dados.shape)
print(citroen_dados.describe())
print(citroen_dados.dtypes)

target_variable = citroen_dados['solucao']
features = citroen_dados.drop('solucao', axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(features, target_variable, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)
