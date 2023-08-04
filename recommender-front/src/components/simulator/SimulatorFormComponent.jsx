import React from 'react';

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
        <label htmlFor="air_temperature">
          Air Temperature
          <input id="air_temperature" type="text" name="air_temperature" placeholder="Air Temperature" onChange={handleInputChange} />
        </label>
        <label htmlFor="wind_speed">
          Wind Speed
          <input id="wind_speed" type="text" name="wind_speed" placeholder="Wind Speed" onChange={handleInputChange} />
        </label>
        <label htmlFor="humidity">
          Humidity
          <input id="humidity" type="text" name="humidity" placeholder="Humidity" onChange={handleInputChange} />
        </label>
        <label htmlFor="precipitation">
          Precipitation
          <input id="precipitation" type="text" name="precipitation" placeholder="Precipitation" onChange={handleInputChange} />
        </label>
        <label htmlFor="cloud_amount">
          Cloud Amount
          <input id="cloud_amount" type="text" name="cloud_amount" placeholder="Cloud Amount" onChange={handleInputChange} />
        </label>
        <label htmlFor="air_quality">
          Air Quality
          <input id="air_quality" type="text" name="air_quality" placeholder="Air Quality" onChange={handleInputChange} />
        </label>
      </form>
    </div>

  );
}

export default SimulatorFormComponent;
