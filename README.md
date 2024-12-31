# IntelliHome: Advanced Smart Home Automation System


> **An intelligent and adaptive smart home system integrating Machine Learning for predictive control, energy efficiency, and enhanced security.**

## 🚀 Features

### 🏡 Home Automation
- Real-time control of appliances using temperature, humidity, and motion sensors.
- Remote monitoring and control through a mobile app or web-based dashboard.

### 🤖 Machine Learning Integration
- **Behavior Prediction**: ML models predict user preferences for temperature, lighting, and appliance usage.
- **Energy Optimization**: Time-series forecasting with LSTM reduces energy wastage.
- **Anomaly Detection**: Isolation Forests detect unusual patterns, triggering security alerts.

### 🔗 Seamless Connectivity
- **UART Communication**: Reliable microcontroller integration.
- **Wi-Fi Control**: ESP32 enables wireless device updates and monitoring.

### 🔒 Enhanced Security
- Motion detection with PIR sensors and real-time anomaly alerts for unexpected events.
- Future-proof system with modular design for additional security features like facial recognition*.

---

## 🛠️ Tech Stack

### **Hardware**
- **Microcontrollers**: Arduino Uno, ESP32.
- **Sensors**: DHT22 (temperature & humidity), PIR (motion), LDR (light intensity).
- **Actuators**: Relay modules.
- **Central Processor**: Raspberry Pi.

### **Software**
- **Languages**: Python, Arduino C.
- **Libraries**: scikit-learn, TensorFlow/Keras.
- **Backend**: Flask/Django.
- **Database**: SQLite/MySQL.
- **Communication**: UART, MQTT.

---

## 📐 System Architecture



1. **Data Collection**: Sensors collect real-time environmental data.
2. **Data Processing**: Raspberry Pi processes data with ML models.
3. **Command Execution**: Commands sent to Arduino via UART for appliance control.
4. **User Interaction**: Dashboard or mobile app displays real-time stats and allows manual overrides.

---

## 📋 Installation

### Prerequisites
- Python 3.x
- Arduino IDE
- Raspberry Pi OS (Debian-based)
- Libraries: scikit-learn, TensorFlow/Keras, Flask
- MQTT broker (e.g., Mosquitto)

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/IntelliHome.git
   cd IntelliHome
   ```
2. **Install Python Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Upload Arduino Code**:
   - Open the `arduino/automation.ino` file in the Arduino IDE.
   - Select the appropriate board (e.g., Arduino Uno) and upload the code.
4. **Run Flask Server**:
   ```bash
   python app.py
   ```
5. **Launch Dashboard**:
   Open `http://localhost:5000` in your browser.

---

## ⚙️ Usage

1. **Connect Sensors**: Attach DHT22, PIR, and LDR to the Arduino board as per the provided pin diagram.
2. **Power On**: Turn on the system. The Raspberry Pi will boot and run the ML models.
3. **Monitor and Control**: Use the dashboard to monitor sensor data and control appliances.
4. **Analyze Predictions**: View energy usage predictions and automated decisions in the dashboard logs.

---

## 🤖 Machine Learning Models

### Behavior Prediction
- **Model**: Linear Regression
- **Input**: Sensor data (temperature, humidity, time of day).
- **Output**: Predicted appliance usage.

### Energy Optimization
- **Model**: LSTM (Long Short-Term Memory).
- **Purpose**: Forecast energy consumption to optimize schedules.

### Anomaly Detection
- **Model**: Isolation Forest.
- **Purpose**: Detect unusual patterns for enhanced security.


---

## 🔍 Future Enhancements
- **Voice Integration**: Add Alexa/Google Assistant support.
- **Facial Recognition**: Use ESP32 Camera for door lock automation.
- **Advanced Scheduling**: Implement deep reinforcement learning for real-time adaptive scheduling.

---

## 🤝 Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## 🌟 Acknowledgements
- Open-source libraries and tools.
- Community contributions.

---

## 📬 Contact
- **Email**: priyanshs.ece@gmail.com
- **GitHub**: [priyanshuhbti](https://github.com/priyanshuhbti)

---

- ## 📬 Collabrator
- **Name**: Deepika Yadav
- **GitHub**: [ppcracker](https://github.com/ppcracker)
