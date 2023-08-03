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
        <input type="text" name="air_temperature" onChange={handleInputChange} placeholder="Air Temperature" />
        <input type="text" name="wind_speed" onChange={handleInputChange} placeholder="Wind Speed" />
        <input type="text" name="humidity" onChange={handleInputChange} placeholder="Humidity" />
        <input type="text" name="precipitation" onChange={handleInputChange} placeholder="Precipitation" />
        <input type="text" name="cloud_amount" onChange={handleInputChange} placeholder="Cloud Amount" />
        <input type="text" name="air_quality" onChange={handleInputChange} placeholder="Air Quality" />
      </form>
    </div>

  );
}

export default SimulatorFormComponent;
