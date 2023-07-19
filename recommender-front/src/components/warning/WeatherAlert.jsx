import React from 'react';
import Alert from '@mui/material/Alert';

function WeatherAlert({ showAlert }) {
  if (!showAlert) {
    return null;
  }

  return (
    <Alert severity="warning" sx={{ marginBottom: '5px' }}>
      You should avoid going outside due to strong wind.
      We do not provide any recommendations and all the controls are disabled.
    </Alert>
  );
}

export default WeatherAlert;
