import React, { useState } from 'react';
import Button from '@mui/material/Button';
import MyLocationIcon from '@mui/icons-material/MyLocation';
import { useMap } from 'react-leaflet';

function LocateButton({ handleSetOrigin }) {
  const staticLat = 60.198805;
  const staticLon = 24.935671;
  const [locating, setLocating] = useState(false);

  const buttonStyle = {
    position: 'absolute',
    bottom: '60px',
    right: '40px',
    zIndex: 1000,
    backgroundColor: 'white',
    padding: '5px',
    borderRadius: '5px',
  };

  const map = useMap();

  const success = (position) => {
    console.log(`Latitude: ${position.coords.latitude}, Longitude: ${position.coords.longitude}`);
    map.flyTo([position.coords.latitude, position.coords.longitude], map.getZoom());
    handleSetOrigin(position.coords.latitude, position.coords.longitude);
    setLocating(false);
  };

  const error = () => {
    console.log('Unable to retrieve your location');
    map.flyTo([staticLat, staticLon], map.getZoom());
    handleSetOrigin(staticLat, staticLon);
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
        <MyLocationIcon />
      </Button>
    </div>
  );
}

export default LocateButton;
