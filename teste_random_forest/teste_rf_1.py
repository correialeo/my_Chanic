import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

problemas = pd.read_csv('problemas.csv')

if problemas.isnull().sum().any():
    print('Valores ausentes encontrados')

var_cat_problemas = problemas.select_dtypes(include='object')

from sklearn.preprocessing import OneHotEncoder

encoder_problemas = OneHotEncoder(handle_unknown='ignore', sparse_output=False)

encoder_problemas.fit(var_cat_problemas)

var_cat_prob_encoded = pd.DataFrame(encoder_problemas.transform(var_cat_problemas))

var_cat_prob_encoded.columns = [f"cat_{i}" for i in range(var_cat_prob_encoded.shape[1])]

problemas_preproc = pd.concat([problemas.select_dtypes(exclude='object'), var_cat_prob_encoded], axis=1)

var_num_problemas = problemas_preproc.select_dtypes(include='number')

from sklearn.preprocessing import StandardScaler

scaler_problemas = StandardScaler()

scaler_problemas.fit(var_num_problemas)

var_num_prob_scaled = pd.DataFrame(scaler_problemas.transform(var_num_problemas))

var_num_prob_scaled.columns = [f'cat_{i}' for i in range(var_num_prob_scaled.shape[1])]

problema_final = pd.concat([var_cat_prob_encoded, var_num_prob_scaled], axis=1)

target_variable = problema_final['solucao']
features = problema_final.drop('solucao', axis=1)

X_train, X_test, Y_train, Y_test = train_test_split(features, target_variable, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, Y_train)
