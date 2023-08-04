import React, { useState, useEffect } from 'react';
import MapComponent from '../components/map/MapComponent';
import SimulatorFormComponent from '../components/simulator/SimulatorFormComponent';
import '../assets/style.css';

function SimulatorPage() {
  const [simulatedWeatherData, setSimulatedWeatherData] = useState({
    air_temperature: '',
    wind_speed: '',
    humidity: '',
    precipitation: '',
    cloud_amount: '',
    air_quality: '',
  });
  const [poiData, setPoiData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const apiUrl = process.env.REACT_APP_BACKEND_URL;
        const poiResponse = await fetch(`${apiUrl}/api/
        simulator?air_temperature=${simulatedWeatherData.air_temperature}
        &wind_speed=${simulatedWeatherData.wind_speed}
        &humidity=${simulatedWeatherData.humidity}
        &precipitation=${simulatedWeatherData.precipitation}
        &cloud_amount=${simulatedWeatherData.cloud_amount}
        &air_quality=${simulatedWeatherData.air_quality}`);
        const poi = await poiResponse.json();
        setPoiData(poi);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
    fetchData();
  }, [simulatedWeatherData]);

  const handleInputChange = (event) => {
    setSimulatedWeatherData({
      ...simulatedWeatherData,
      [event.target.name]: event.target.value,
    });
  };

  return (
    <div className="simulator-container">
      <div className="simulator-form-component">
        <SimulatorFormComponent handleInputChange={handleInputChange} />
      </div>
      <div className="simulator-map-container">
        <MapComponent
          poiData={poiData}
        />
      </div>

    </div>
  );
}

export default SimulatorPage;
