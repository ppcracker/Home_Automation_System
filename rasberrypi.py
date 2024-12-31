# This code is written for the hardware optimisation of the arduino.
#Flask-API Endpoints code on 5000 Gateway.

import RPi.GPIO as GPIO
import time
from flask import Flask, request, jsonify

app = Flask(__testapi__)

GPIO.setmode(GPIO.BCM)
LED_PIN = 18  
GPIO.setup(LED_PIN, GPIO.OUT)


@app.route('/control_led', methods=['POST'])
def control_led():
    data = request.json
    action = data.get('action')
    
    if action == 'on':
        GPIO.output(LED_PIN, GPIO.HIGH)
        return jsonify({'message': 'LED turned ON'})
    elif action == 'off':
        GPIO.output(LED_PIN, GPIO.LOW)
        return jsonify({'message': 'LED turned OFF'})
    else:
        return jsonify({'error': 'Invalid action'}), 400

@app.route('/shutdown', methods=['POST'])
def shutdown():
    GPIO.cleanup()
    return jsonify({'message': 'GPIO cleaned up and server shutting down'})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()

###Device-Driver-Setup
try:
    while True:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()