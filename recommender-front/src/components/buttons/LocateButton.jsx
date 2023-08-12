import React, { useState } from 'react';
import Button from '@mui/material/Button';
import MyLocationIcon from '@mui/icons-material/MyLocation';
import { useMapEvents } from 'react-leaflet';

function LocateButton({ handleSetOrigin }) {
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

  const map = useMapEvents({
    locationfound(e) {
      map.flyTo(e.latlng, map.getZoom());
      handleSetOrigin(e.latlng.lat, e.latlng.lng);
      setLocating(false);
    },
    locationerror() {
      setLocating(false);
    },
  });

  const handleClick = () => {
    if (!locating) {
      setLocating(true);
      map.locate();
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
