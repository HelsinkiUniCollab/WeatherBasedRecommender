import React from 'react';
import Alert from '@mui/material/Alert';
import Typography from '@mui/material/Typography';

const fullscreenAlertStyle = {
  position: 'absolute',
  top: 0,
  bottom: 0,
  zIndex: 9999,
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
};

function WeatherAlert({ showAlert }) {
  const alertStyle = {
    ...fullscreenAlertStyle,
    left: '50%',
    transform: 'translateX(-50%)',
  };

  if (!showAlert) {
    return null;
  }

  return (
    <div style={alertStyle}>
      <Alert severity="warning" sx={{ fontSize: '40px', color: '#000000', backgroundColor: 'white', width: '100%' }}>
        <Typography variant="h1">
          <center>
            You should avoid going outside due to strong wind.
            We do not provide any recommendations and all the controls are disabled.
          </center>
        </Typography>
      </Alert>
    </div>
  );
}

export default WeatherAlert;
