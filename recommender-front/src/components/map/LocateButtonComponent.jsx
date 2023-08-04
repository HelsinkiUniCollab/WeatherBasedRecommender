import React from 'react';
import { useMapEvents } from 'react-leaflet';

function LocateButton({ handleSetOrigin }) {
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
    },
  });

  const handleClick = () => {
    console.log('Clicked!');
    map.locate();
  };

  return (
    <div style={buttonStyle}>
      <button type="button" onClick={handleClick}>Locate me!</button>
    </div>
  );
}

export default LocateButton;
