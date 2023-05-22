import React, { useState, useEffect } from 'react';

function WeatherComponent() {
  const [data, setData] = useState({
    airtemperature: null,
    airquality: null,
  });

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000';
    fetch(`${apiUrl}/api/weather`)
      .then((res) => res.json())
      .then((responseData) => {
        setData({
          airtemperature: responseData.airtemperature,
          airquality: responseData.airquality,
        });
      })
      .catch((error) => {
        console.error('Error fetching weather data:', error);
      });
  }, []);

  return (
    <div>
      <p>
        <font size="5">
          {data.airtemperature}
          {' '}
          °C
          {' '}
          {data.airquality}
          {' '}
          AQI
        </font>
      </p>
    </div>
  );
}

export default WeatherComponent;
