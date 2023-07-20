import React from 'react';
import Alert from '@mui/material/Alert';

const fullscreenAlertStyle = {
  position: 'absolute',
  top: 0,
  left: 0,
  right: 0,
  bottom: 0,
  zIndex: 9999,
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  backgroundColor: 'rgba(0, 0, 0, 0.5)', // You can adjust the background color and transparency here
};

function WeatherAlert({ showAlert }) {
  if (!showAlert) {
    return null;
  }

  return (
    <div style={fullscreenAlertStyle}>
      <Alert severity="warning" sx={{ fontSize: '80px', color: '#000' }}>
        You should avoid going outside due to strong wind.
        We do not provide any recommendations and all the controls are disabled.
      </Alert>
    </div>
  );
}

export default WeatherAlert;
