import React from 'react';
import { Marker } from 'react-leaflet';
import L from 'leaflet';

function UserLocationMarker({ handleSetOrigin, userPosition }) {
  const placeholderMarker = L.icon({
    iconUrl: 'https://cdn-icons-png.flaticon.com/512/3754/3754313.png',
    iconSize: [35, 35],
    popupAnchor: [-1, -25],
    iconAnchor: [16, 32],
  });

  const handleDragEnd = (event) => {
    const newPosition = event.target.getLatLng();
    handleSetOrigin(newPosition.lat, newPosition.lng);
  };

  return userPosition === null ? null : (
    <Marker
      data-testid="usermarker"
      icon={placeholderMarker}
      position={userPosition}
      draggable
      eventHandlers={{
        dragend: handleDragEnd,
      }}
    />
  );
}

export default UserLocationMarker;
