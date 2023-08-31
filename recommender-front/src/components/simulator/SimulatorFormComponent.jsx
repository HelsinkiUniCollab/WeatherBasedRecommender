import React from 'react';
import Typography from '@mui/material/Typography';
import CustomTextField from './CustomTextField';
import TimePickerComponent from './TimePickerComponent';

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
    width: '140px',
    height: '65vh',
    maxHeight: '65vh',
    overFlowy: 'auto',
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
          placeholder="Precipitation mm)"
          value={simulatedWeatherData.precipitation}
          handleInputChange={handleInputChange}
          helperText="mm"
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
        <TimePickerComponent
          time={currentTime}
          onTimeChange={handleTimeChange}
          namePrefix="current-time"
        />
        <Typography>Sunrise</Typography>
        <TimePickerComponent
          time={sunrise}
          onTimeChange={handleSunriseChange}
          namePrefix="sunrise"
        />
        <Typography>Sunset</Typography>
        <TimePickerComponent
          time={sunset}
          onTimeChange={handleSunsetChange}
          namePrefix="sunset"
        />
      </form>
    </div>
  );
}

export default SimulatorFormComponent;
