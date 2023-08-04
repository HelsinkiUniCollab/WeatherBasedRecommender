import React, { useRef } from 'react';
import { Marker, Popup } from 'react-leaflet';
import L from 'leaflet';

function UserLocationMarker({ handleSetOrigin, userPosition }) {
  const markerRef = useRef(null);
  const placeholderMarker = L.icon({
    iconUrl: 'https://cdn-icons-png.flaticon.com/512/3754/3754313.png',
    iconSize: [35, 35],
    popupAnchor: [-1, -25],
    iconAnchor: [16, 32],
  });

  const handleMarkerDragEnd = () => {
    if (markerRef.current) {
      const marker = markerRef.current;
      const pos = marker.getLatLng();
      handleSetOrigin(pos.lat, pos.lng);
    }
  };

  return userPosition === null ? null : (
    <Marker
      icon={placeholderMarker}
      position={userPosition}
      draggable
      ref={markerRef}
    >
      <Popup>
        <button type="button" onClick={() => handleMarkerDragEnd()}>Set Origin</button>
      </Popup>
    </Marker>
  );
}

export default UserLocationMarker;
