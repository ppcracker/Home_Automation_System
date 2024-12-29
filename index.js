
const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');

const axios = require('axios');


const BASE_URL = 'http://127.0.0.1:5000';



const app = express();
const PORT = 3000; 
app.use(bodyParser.json());


app.post('/predict_behavior', async (req, res) => {
  const { T, rh, wd } = req.body; 
  try {
    const response = await axios.post(`${BASE_URL}/predict_behavior`, { T, rh, wd });
    res.status(200).json({ predicted_temperature: response.data.predicted_temperature });
  } catch (error) {
    console.error('Error predicting behavior:', error.message);
    res.status(500).json({ error: 'Error predicting behavior', details: error.message });
  }
});

//forecast-energy-usage
app.post('/forecast_energy', async (req, res) => {
  const { sequence } = req.body;
  try {
    const response = await axios.post(`${BASE_URL}/forecast_energy`, { sequence });
    res.status(200).json({ forecasted_energy: response.data.forecasted_energy });
  } catch (error) {
    console.error('Error forecasting energy:', error.message);
    res.status(500).json({ error: 'Error forecasting energy', details: error.message });
  }
});

//  detect anomalies
app.post('/detect_anomaly', async (req, res) => {
  const { p, T, rh, VPact } = req.body; 
  try {
    const response = await axios.post(`${BASE_URL}/detect_anomaly`, { p, T, rh, VPact });
    res.status(200).json(response.data);
  } catch (error) {
    console.error('Error detecting anomaly:', error.message);
    res.status(500).json({ error: 'Error detecting anomaly', details: error.message });
  }
});

// Server Starting...
app.listen(PORT, () => {
  console.log(`Node.js backend is running on http://localhost:${PORT}`);
});
