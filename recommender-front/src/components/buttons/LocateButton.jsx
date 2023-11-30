import React, { useState } from 'react';
import Button from '@mui/material/Button';
import MyLocationIcon from '@mui/icons-material/MyLocation';
import { useMap } from 'react-leaflet';

function LocateButton({ handleSetOrigin }) {
  const staticLat = 60.204178;
  const staticLon = 24.961690;
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

  const handleClick = () => {
    if (!locating) {
      setLocating(true);
      map.flyTo([staticLat, staticLon], map.getZoom());
      handleSetOrigin(staticLat, staticLon);
      setLocating(false);
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
