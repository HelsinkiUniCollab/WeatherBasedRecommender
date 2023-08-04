import React, { useState, useEffect } from 'react';
import MapComponent from '../components/map/MapComponent';
import SimulatorFormComponent from '../components/simulator/SimulatorFormComponent';
import '../assets/style.css';

function SimulatorPage() {
  const [simulatedWeatherData, setSimulatedWeatherData] = useState({
    airTemperature: '',
    windSpeed: '',
    humidity: '',
    precipitation: '',
    cloudAmount: '',
    airQuality: '',
  });
  const [poiData, setPoiData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      try {
        const apiUrl = process.env.REACT_APP_BACKEND_URL;
        const { airTemperature, windSpeed, humidity,
          precipitation, cloudAmount, airQuality } = simulatedWeatherData;
        if (!airTemperature || !windSpeed || !humidity
           || !precipitation || !cloudAmount || !airQuality) {
          console.log('One or more parameter values are empty');
          return;
        }
        const poiResponse = await fetch(`${apiUrl}/api/simulator?air_temperature=${airTemperature}&wind_speed=${windSpeed}&humidity=${humidity}&precipitation=${precipitation}&cloud_amount=${cloudAmount}&air_quality=${airQuality}`);
        const poi = await poiResponse.json();
        setPoiData(poi);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
    fetchData();
  }, [simulatedWeatherData]);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    if (/^-?\d*\.?\d*$/.test(value)) {
      setSimulatedWeatherData((prevState) => ({
        ...prevState,
        [name]: value,
      }));
    }
  };

  return (
    <div className="simulator-container">
      <div className="simulator-form-component">
        <SimulatorFormComponent handleInputChange={handleInputChange} />
      </div>
      <div className="simulator-map-container">
        <MapComponent
          poiData={poiData}
          time="Weather"
        />
      </div>
    </div>
  );
}

export default SimulatorPage;