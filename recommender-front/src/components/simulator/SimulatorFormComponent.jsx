import React from 'react';
import Typography from '@mui/material/Typography';

function SimulatorFormComponent({ handleInputChange }) {
  const formStyle = {
    position: 'absolute',
    bottom: '10px',
    left: '10px',
    background: 'white',
    padding: '10px',
    borderRadius: '5px',
    display: 'grid',
    gap: '10px',
  };

  return (
    <div>
      <form style={formStyle}>
        <Typography>Air Temperature</Typography>
        <input id="airTemperature" type="text" name="airTemperature" placeholder="Air Temperature (°C)" onChange={handleInputChange} />
        <Typography>Wind Speed</Typography>

        <input id="windSpeed" type="text" name="windSpeed" placeholder="Wind Speed (m/s)" onChange={handleInputChange} />

        <Typography>Humidity</Typography>

        <input id="humidity" type="text" name="humidity" placeholder="Humidity (%)" onChange={handleInputChange} />

        <Typography>Precipitation</Typography>

        <input id="precipitation" type="text" name="precipitation" placeholder="Precipitation (%)" onChange={handleInputChange} />

        <Typography>Cloud Amount</Typography>

        <input id="cloudAmount" type="text" name="cloudAmount" placeholder="Cloud Amount (%)" onChange={handleInputChange} />

        <Typography>Air Quality</Typography>

        <input id="airQuality" type="text" name="airQuality" placeholder="Air Quality Index" onChange={handleInputChange} />

      </form>
    </div>
  );
}

export default SimulatorFormComponent;
