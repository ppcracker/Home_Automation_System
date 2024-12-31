# IoT Home Automation System Workflow

## 1. Power On and Initialization
- **NodeMCU:** When powered on, the NodeMCU initializes and starts running the `setup()` function.
- **Power Supply:** Provides stable power to the NodeMCU, DHT11 sensor, LDR, and relays.

## 2. WiFi Connection
- **NodeMCU:** Attempts to connect to the WiFi network using the SSID (`ASHUTOSH`) and password (`ashu2004`). It keeps trying until a connection is established.
- **WiFi Router:** Provides internet access and local network connectivity.

## 3. Sensor and Relay Setup
- **DHT11 Sensor:** Initialized to start measuring temperature and humidity.
  - `DHTPIN (D2):` Connects to the data pin of the DHT11 sensor.
- **LDR (Light Dependent Resistor):** Set up to measure light intensity.
  - `LDRPIN (A0):` Connects to the junction between the LDR and a resistor, reading the analog value of light intensity.
- **Relays:** Configured to control external devices (e.g., lights, fans).
  - `RELAY1_PIN (D8):` Connects to the first relay.
  - `RELAY2_PIN (D7):` Connects to the second relay.
- **Digital Pins:** Set up as outputs to control the relays.

## 4. Web Server Initialization
- **NodeMCU:** Initializes the HTTP web server on port 80.
- **ESP8266WebServer Library:** Provides functions to create and handle HTTP requests.

## 5. Define Routes for Web Server
- **handleRoot():** Serves the main HTML web page.
- **handleReadSensors():** Provides the latest sensor readings in JSON format.
- **handleToggleRelay1():** Toggles the state of Relay 1.
- **handleToggleRelay2():** Toggles the state of Relay 2.

## 6. Web Interface Access
- **User:** Opens a web browser and navigates to the NodeMCU's IP address, displayed in the Serial Monitor.
- **Web Browser:** Requests the root page (`/`) from the NodeMCU.

## 7. Display Web Interface
- **NodeMCU:** Responds to the root page request with the HTML content.
- **HTML:** Displays the sensor data and toggle switches for relay control.
- **CSS:** Styles the toggle switches and sensor data display.
- **JavaScript:** Handles the toggle switch actions and periodically fetches updated sensor readings.

## 8. Real-time Sensor Data Fetching
- **JavaScript:** Sends requests to `/readSensors` every second.
- **handleReadSensors():**
  - **DHT11 Sensor:** Reads the current temperature and humidity.
  - **LDR:** Reads the current light intensity.
  - **JSON Response:** Sends the sensor data back to the web browser.

## 9. Display Sensor Data
- **Web Browser:** Receives the JSON response and updates the sensor data on the web interface.

## 10. Relay Control via Toggle Switches
- **User:** Toggles a switch to change the state of a relay.
- **JavaScript:** Sends a request to `/toggleRelay1` or `/toggleRelay2` based on the switch toggled.

## 11. Handle Relay Toggle Requests
- **handleToggleRelay1():**
  - **Relay 1:** Toggles its state and updates its GPIO pin accordingly (turns ON if it was OFF and vice versa).
  - **Response:** Sends the updated state back to the web browser.
- **handleToggleRelay2():**
  - **Relay 2:** Toggles its state and updates its GPIO pin accordingly.
  - **Response:** Sends the updated state back to the web browser.

## 12. Continuous Monitoring and Control
- The system continuously monitors sensor readings and listens for relay toggle requests, ensuring real-time control and feedback.

---

**Note:** This workflow is designed to help you understand the sequence of operations in an IoT Home Automation system using NodeMCU, DHT11, LDR, relays, and a web server.
