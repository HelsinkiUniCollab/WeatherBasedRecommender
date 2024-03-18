import React, { useState } from 'react';
import Button from '@mui/material/Button';
import { useMap } from 'react-leaflet';
import RotateRightIcon from '@mui/icons-material/RotateRight';

function CircleButton({ handleCircleRoute }) {
  const staticLat = 60.198805;
  const staticLon = 24.935671;
  const [locating, setLocating] = useState(false);

  const buttonStyle = {
    position: 'absolute',
    bottom: '60px',
    right: '120px',
    zIndex: 1000,
    backgroundColor: 'white',
    padding: '5px',
    borderRadius: '5px',
  };

  const map = useMap();

  const success = (position) => {
    console.log(`Latitude: ${position.coords.latitude}, Longitude: ${position.coords.longitude}`);
    map.flyTo([position.coords.latitude, position.coords.longitude], map.getZoom());
    handleCircleRoute(position.coords.latitude, position.coords.longitude);
    setLocating(false);
  };

  const error = () => {
    console.log('Unable to retrieve your location');
    map.flyTo([staticLat, staticLon], map.getZoom());
    handleCircleRoute(staticLat, staticLon);
    setLocating(false);
  };

  const handleClick = () => {
    if (!locating) {
      setLocating(true);

      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(success, error);
      } else {
        console.log('Geolocation not supported');
      }
    }
  };

  return (
    <div style={buttonStyle}>
      <Button variant="text" data-testid="locate-button" onClick={handleClick} disabled={locating}>
        <RotateRightIcon />
      </Button>
    </div>
  );
}

export default CircleButton;
