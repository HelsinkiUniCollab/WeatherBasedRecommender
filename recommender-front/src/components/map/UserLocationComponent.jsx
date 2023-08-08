import React, { useEffect } from 'react';
import { Marker } from 'react-leaflet';
import L from 'leaflet';

function UserLocationMarker({ handleSetOrigin, userPosition }) {
  const placeholderMarker = L.icon({
    iconUrl: 'https://cdn-icons-png.flaticon.com/512/3754/3754313.png',
    iconSize: [35, 35],
    popupAnchor: [-1, -25],
    iconAnchor: [16, 32],
  });

  useEffect(() => {
    if (userPosition) {
      console.log('Setting origin with position:', userPosition);
      handleSetOrigin(userPosition[0], userPosition[1]);
    }
  }, [handleSetOrigin, userPosition]);

  return userPosition === null ? null : (
    <Marker
      icon={placeholderMarker}
      position={userPosition}
    />
  );
}

export default UserLocationMarker;
