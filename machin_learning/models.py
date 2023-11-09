import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import requests

def get_data_frame_api(url):
    urlData = requests.get(req).content
    data = pd.read_csv(io.StringIO(urlData.decode('utf-8')))
    return data 

def hist_vol(data):
    # volatilité historique
    data['Volatilite'] = data['Prix'].rolling(window=24).std()
    return data

def create_model(data):
    # pars data
    X = data['Prix'].values
    y = data['Volatilite'].shift(-1).values  # La volatilité de l'heure suivante est la cible

    X_train, X_test, y_train, y_test = train_test_split(X[:-1], y[:-1], test_size=0.2, shuffle=False)

    # Create the modèle
    model = keras.Sequential()
    model.add(keras.layers.LSTM(50, input_shape=(24, 1)))
    model.add(keras.layers.Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    # Entraînez le modèle
    X_train = X_train.reshape(-1, 24, 1)  # Mettez en forme les données pour le modèle LSTM
    model.fit(X_train, y_train, epochs=50, batch_size=32)
    # Évaluez le modèle
    X_test = X_test.reshape(-1, 24, 1)
    predictions = model.predict(X_test)

def main():
    url = 'http://127.0.0.1:8000'
    data_req = '/vol?comp=^FCHI&period=1mo'
    req = url + data
    api_data = get_data_frame_api(url)
    hist_data = hist_vol(api_data)
    hist_data = pars_data(data)


