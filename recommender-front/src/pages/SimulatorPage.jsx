import React, { useState, useEffect } from 'react';
import MapComponent from '../components/map/MapComponent';
import SimulatorFormComponent from '../components/simulator/SimulatorFormComponent';
import '../assets/style.css';
import WeatherAlert from '../components/warning/WeatherAlert';
import useDebounce from '../utils/DebounceUtil';

function SimulatorPage() {
  const [simulatedWeatherData, setSimulatedWeatherData] = useState({
    airTemperature: '10',
    windSpeed: '4',
    humidity: '20',
    precipitation: '0',
    cloudAmount: '0',
    airQuality: '2',
  });
  const [currentTime, setCurrentTime] = useState(new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }));
  const [sunrise, setSunrise] = useState('6:00');
  const [sunset, setSunset] = useState('22:00');
  const [poiData, setPoiData] = useState([]);
  const [isNightTime, setIsNightTime] = useState(false);

  const windSpeedOverThreshold = simulatedWeatherData.windSpeed > 17;

  const debouncedTime = useDebounce(currentTime, 500);
  const debouncedSunrise = useDebounce(sunrise, 500);
  const debouncedSunset = useDebounce(sunset, 500);

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
        const poiResponse = await fetch(`${apiUrl}/api/simulator`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            air_temperature: airTemperature,
            wind_speed: windSpeed,
            humidity,
            precipitation,
            cloud_amount: cloudAmount,
            air_quality: airQuality,
            current_time: currentTime,
            sunrise,
            sunset,
          }),
        }); const poi = await poiResponse.json();
        setPoiData(poi);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
    fetchData();
  }, [simulatedWeatherData, debouncedTime, debouncedSunrise, debouncedSunset]);

  useEffect(() => {
    const currentTimeDate = new Date(`1970-01-01T${currentTime}:00`);
    const sunriseDate = new Date(`1970-01-01T${sunrise}:00`);
    const sunsetDate = new Date(`1970-01-01T${sunset}:00`);

    if (currentTimeDate < sunriseDate || currentTimeDate > sunsetDate) {
      setIsNightTime(true);
    } else {
      setIsNightTime(false);
    }
    console.log(isNightTime);
  }, [currentTime, sunrise, sunset]);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    if (/^-?\d*\.?\d*$/.test(value)) {
      setSimulatedWeatherData((prevState) => ({
        ...prevState,
        [name]: value,
      }));
    }
  };

  const handleTimeChange = (event) => {
    const timeString = event.target.value;
    setCurrentTime(timeString);
  };

  const handleSunriseChange = (event) => {
    setSunrise(event.target.value);
  };

  const handleSunsetChange = (event) => {
    setSunset(event.target.value);
  };

  return (
    <div className="simulator-container">
      <WeatherAlert showAlert={windSpeedOverThreshold} />
      <div className="simulator-form-component">
        <SimulatorFormComponent
          handleInputChange={handleInputChange}
          simulatedWeatherData={simulatedWeatherData}
          handleTimeChange={handleTimeChange}
          currentTime={currentTime}
          handleSunriseChange={handleSunriseChange}
          sunrise={sunrise}
          handleSunsetChange={handleSunsetChange}
          sunset={sunset}
        />
      </div>
      <div id="simulator-map" className="simulator-map-container">
        <MapComponent
          poiData={poiData}
          time="Weather"
        />
        {isNightTime && <div className="night-overlay" data-testid="night-overlay" />}
      </div>
    </div>
  );
}

export default SimulatorPage;
