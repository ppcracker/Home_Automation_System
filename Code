

/* Arduino IDE Code for Home Intelligence System */


#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <DHT.h>

// Constants
#define DHT_PIN D2     // DHT11 Pin
#define LDR_PIN A0      // LDR Pin
#define RELAY1_PIN D8   // Relay 1 Pin
#define RELAY2_PIN D7   // Relay 2 Pin

#define WIFI_SSID "Priyanshu "
#define WIFI_PASSWORD "priyanshu"

// Initialize Objects
DHT dht(DHT_PIN, DHT11); 
ESP8266WebServer server(80); 

// Variables
float temperature = 0;
float humidity = 0;
int lightIntensity = 0;
bool relay1State = LOW;
bool relay2State = LOW;

void setup() {
  Serial.begin(115200);
  pinMode(RELAY1_PIN, OUTPUT);
  pinMode(RELAY2_PIN, OUTPUT);
  digitalWrite(RELAY1_PIN, relay1State);
  digitalWrite(RELAY2_PIN, relay2State);
  dht.begin();
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi..");
  }
  Serial.println(WiFi.localIP());

  server.on("/", HTTP_GET, handleRoot);
  server.on("/readSensors", HTTP_GET, handleReadSensors);
  server.on("/toggleRelay1", HTTP_GET, handleToggleRelay1);
  server.on("/toggleRelay2", HTTP_GET, handleToggleRelay2);
  server.begin();
}

void loop() {
  server.handleClient();
  delay(1); 
}

void readSensors() {
  temperature = dht.readTemperature(); 
  humidity = dht.readHumidity(); 
  lightIntensity = analogRead(LDR_PIN); 
  delay(100); 
}

// HTTP Handlers

void handleRoot() {
  readSensors(); // Update sensor readings before displaying
  String html = 
  "<!DOCTYPE html><html><head><title>NodeMCU Dashboard</title>"
  "<style>"
  "body { font-family: Arial; }"
  ".container { width: 80%; margin: auto; }"
  ".sensor-data { margin-bottom: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }"
  ".switch { position: relative; display: inline-block; width: 120px; height: 68px; }"
  ".switch input { display: none; }"
  ".slider { position: absolute; top: 0; left: 0; right: 0; bottom: 0; background-color: #ccc; border-radius: 34px; }"
  ".slider:before { position: absolute; content: ''; height: 52px; width: 52px; left: 8px; bottom: 8px; background-color: white; -webkit-transition: .4s; transition: .4s; border-radius: 50%; }"
  "input:checked + .slider { background-color: #2196F3; }"
  "input:checked + .slider:before { -webkit-transform: translateX(52px); -ms-transform: translateX(52px); transform: translateX(52px); }"
  ".slider { background-color: " + String(relay1State ? "#2196F3" : "#ccc") + "; }"
  "</style>"
  "</head><body>"
  "<div class='container'>"
  "<h1>NodeMCU Sensor & Relay Dashboard</h1>"
  "<div class='sensor-data'>"
  "<h2>Sensor Readings</h2>"
  "<p id='temperature'>Temperature: <span>" + String(temperature) + "°C</span></p>"
  "<p id='humidity'>Humidity: <span>" + String(humidity) + "%</span></p>"
  "<p id='lightIntensity'>Light Intensity: <span>" + String(lightIntensity) + "</span></p>"
  "</div>"
  "<div class='sensor-data'>"
  "<h2>Relay Control</h2>"
  "<label class='switch'><input type='checkbox' id='1' " + String(relay1State ? "checked" : "") + " onclick='toggleRelay(1)'><span class='slider'></span></label> Relay 1"
  "<label class='switch'><input type='checkbox' id='2' " + String(relay2State ? "checked" : "") + " onclick='toggleRelay(2)'><span class='slider'></span></label> Relay 2"
  "</div>"
  "<script>"
  "function toggleRelay(relayNum) {"
  "  var xhr = new XMLHttpRequest();"
  "  xhr.open('GET', '/toggleRelay' + relayNum, true);"
  "  xhr.send();"
  "}"
  "setInterval(function() {"
  "  fetch('/readSensors').then(response => response.json()).then(data => {"
  "    document.getElementById('temperature').innerHTML = 'Temperature: ' + data.temperature + '°C';"
  "    document.getElementById('humidity').innerHTML = 'Humidity: ' + data.humidity + '%';"
  "    document.getElementById('lightIntensity').innerHTML = 'Light Intensity: ' + data.lightIntensity;"
  "  });"
  "}, 1000);"
  "</script>"
  "</body></html>";
  server.send(200, "text/html", html);
}

void handleReadSensors() {
  readSensors(); // Update sensor readings before sending
  String json = "{\"temperature\": " + String(temperature) +
                ", \"humidity\": " + String(humidity) +
                ", \"lightIntensity\": " + String(lightIntensity) + "}";
  server.send(200, "application/json", json);
}

void handleToggleRelay1() {
  relay1State = !relay1State;
  digitalWrite(RELAY1_PIN, relay1State);
  String state = (relay1State) ? "ON" : "OFF";
  server.send(200, "text/plain", "Relay 1 State: " + state);
}

void handleToggleRelay2() {
  relay2State = !relay2State;
  digitalWrite(RELAY2_PIN, relay2State);
  String state = (relay2State) ? "ON" : "OFF";
  server.send(200, "text/plain", "Relay 2 State: " + state);
}
