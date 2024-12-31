import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib
from flask import Flask, request, jsonify

data = pd.read_csv('testdata.csv')  

data['date'] = pd.to_datetime(data['date'])  

def preprocess_data(data):
    data = data.dropna() 
    return data

data = preprocess_data(data)

# ======== BEHAVIOR PREDICTION ========

X_behavior = data[['T', 'rh', 'wd']] 
y_behavior = data['Tlog']  

X_train_b, X_test_b, y_train_b, y_test_b = train_test_split(X_behavior, y_behavior, test_size=0.2, random_state=42)

behavior_model = LinearRegression()
behavior_model.fit(X_train_b, y_train_b)
joblib.dump(behavior_model, 'behavior_model.pkl') 


# ======== ENERGY OPTIMIZATION ========
energy_data = data['SWDR'].values.reshape(-1, 1)  
scaler = MinMaxScaler()
scaled_energy_data = scaler.fit_transform(energy_data)


def seq_banao(data, seq_length):
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:i + seq_length])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

seq_length = 10
X_energy, y_energy = seq_banao(scaled_energy_data, seq_length)

split = int(0.8 * len(X_energy))
X_train_e, X_test_e = X_energy[:split], X_energy[split:]
y_train_e, y_test_e = y_energy[:split], y_energy[split:]

# LSTM model
energy_model = Sequential([
    LSTM(50, return_sequences=True, input_shape=(X_train_e.shape[1], 1)),
    LSTM(50, return_sequences=False),
    Dense(25),
    Dense(1)
])
energy_model.compile(optimizer='adam', loss='mean_squared_error')
energy_model.fit(X_train_e, y_train_e, epochs=20, batch_size=32)
energy_model.save('energy_model.h5') 

# ======== ANOMALY DETECTION ========

X_anomaly = data[['p', 'T', 'rh', 'VPact']] #for this details refer to csv files and kaggle temperature dataset ..


anomaly_model = IsolationForest(contamination=0.05, random_state=42)
anomaly_model.fit(X_anomaly)
joblib.dump(anomaly_model, 'anomaly_model.pkl')  



##Models monolithic code done
##Backend and API work starts from here...
##FlaskAPI working...
app = Flask(__name__)

# Load models
behavior_model = joblib.load('behavior_model.pkl')
energy_model = energy_model
anomaly_model = joblib.load('anomaly_model.pkl')

@app.route('/predict_behavior', methods=['POST'])
def predict_behavior():
    data = request.json
    prediction = behavior_model.predict([[data['T'], data['rh'], data['wd']]])
    return jsonify({'predicted_temperature': prediction[0]})

@app.route('/forecast_energy', methods=['POST'])
def forecast_energy():
    data = request.json
    sequence = np.array(data['sequence']).reshape(1, -1, 1)
    prediction = energy_model.predict(sequence)
    return jsonify({'forecasted_energy': prediction[0][0]})

@app.route('/detect_anomaly', methods=['POST'])
def detect_anomaly():
    data = request.json
    observation = np.array([data['p'], data['T'], data['rh'], data['VPact']]).reshape(1, -1)
    anomaly_score = anomaly_model.decision_function(observation)
    is_anomaly = anomaly_model.predict(observation)[0] == -1
    return jsonify({'is_anomaly': is_anomaly, 'anomaly_score': anomaly_score[0]})

if __name__ == '__main__':
    app.run(debug=True)
