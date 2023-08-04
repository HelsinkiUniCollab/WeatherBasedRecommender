import React, { useRef } from 'react';
import { Marker, Popup } from 'react-leaflet';

function UserLocationMarker({ handleSetOrigin, userPosition }) {
  const markerRef = useRef(null);

  const handleMarkerDragEnd = () => {
    if (markerRef.current) {
      const marker = markerRef.current;
      const pos = marker.getLatLng();
      handleSetOrigin(pos.lat, pos.lng);
    }
  };

  return userPosition === null ? null : (
    <Marker
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
