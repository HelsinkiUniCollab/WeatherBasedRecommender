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
        <Typography htmlFor="airTemperature">
          Air Temperature
          <input id="airTemperature" type="text" name="airTemperature" placeholder="Air Temperature" onChange={handleInputChange} />
        </Typography>
        <Typography htmlFor="windSpeed">
          Wind Speed
          <input id="windSpeed" type="text" name="windSpeed" placeholder="Wind Speed" onChange={handleInputChange} />
        </Typography>
        <Typography htmlFor="humidity">
          Humidity
          <input id="humidity" type="text" name="humidity" placeholder="Humidity" onChange={handleInputChange} />
        </Typography>
        <Typography htmlFor="precipitation">
          Precipitation
          <input id="precipitation" type="text" name="precipitation" placeholder="Precipitation" onChange={handleInputChange} />
        </Typography>
        <Typography htmlFor="cloudAmount">
          Cloud Amount
          <input id="cloudAmount" type="text" name="cloudAmount" placeholder="Cloud Amount" onChange={handleInputChange} />
        </Typography>
        <Typography htmlFor="airQuality">
          Air Quality
          <input id="airQuality" type="text" name="airQuality" placeholder="Air Quality" onChange={handleInputChange} />
        </Typography>
      </form>
    </div>
  );
}

export default SimulatorFormComponent;
