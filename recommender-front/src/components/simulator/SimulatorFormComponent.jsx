import React from 'react';
import Typography from '@mui/material/Typography';
import CustomTextField from './CustomTextField';

function SimulatorFormComponent({
  handleInputChange,
  simulatedWeatherData,
  handleTimeChange,
  currentTime,
  handleSunriseChange,
  sunrise,
  handleSunsetChange,
  sunset,
}) {
  const formStyle = {
    bottom: '10px',
    left: '10px',
    background: 'white',
    padding: '10px',
    borderRadius: '5px',
    display: 'grid',
    gap: '5px',
    width: '120px',
  };

  return (
    <div>
      <form style={formStyle}>
        <Typography>Air Temperature</Typography>
        <CustomTextField
          name="airTemperature"
          placeholder="Air Temperature (°C)"
          value={simulatedWeatherData.airTemperature}
          handleInputChange={handleInputChange}
          helperText="°C"
        />
        <Typography>Wind Speed</Typography>
        <CustomTextField
          name="windSpeed"
          placeholder="Wind Speed (m/s)"
          value={simulatedWeatherData.windSpeed}
          handleInputChange={handleInputChange}
          helperText="m/s"
        />
        <Typography>Humidity</Typography>
        <CustomTextField
          name="humidity"
          placeholder="Humidity (%)"
          value={simulatedWeatherData.humidity}
          handleInputChange={handleInputChange}
          helperText="%"
        />
        <Typography>Precipitation</Typography>
        <CustomTextField
          name="precipitation"
          placeholder="Precipitation (%)"
          value={simulatedWeatherData.precipitation}
          handleInputChange={handleInputChange}
          helperText="%"
        />
        <Typography>Cloud Amount</Typography>
        <CustomTextField
          name="cloudAmount"
          placeholder="Cloud Amount (%)"
          value={simulatedWeatherData.cloudAmount}
          handleInputChange={handleInputChange}
          helperText="%"
        />
        <Typography>Air Quality</Typography>
        <CustomTextField
          name="airQuality"
          placeholder="Air Quality Index"
          value={simulatedWeatherData.airQuality}
          handleInputChange={handleInputChange}
          helperText="1-5"
        />
        <Typography>Current Time</Typography>
        <CustomTextField
          name="currentTime"
          placeholder="Current Time"
          value={currentTime}
          handleInputChange={handleTimeChange}
        />
        <Typography>Sunrise</Typography>
        <CustomTextField
          name="sunrise"
          placeholder="Sunrise"
          value={sunrise}
          handleInputChange={handleSunriseChange}
        />
        <Typography>Sunset</Typography>
        <CustomTextField
          name="sunset"
          placeholder="Sunset"
          value={sunset}
          handleInputChange={handleSunsetChange}
        />
      </form>
    </div>
  );
}

export default SimulatorFormComponent;
