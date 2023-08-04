import React, { useState, useRef } from 'react';
import { Marker, Popup } from 'react-leaflet';

function UserLocationMarker({ handleSetOrigin }) {
  const [position, setPosition] = useState(null);
  const markerRef = useRef(null);

  const handleMarkerDragEnd = () => {
    if (markerRef.current) {
      console.log('clicked');
      const marker = markerRef.current;
      const pos = marker.getLatLng();
      setPosition([pos.lat, pos.lng]);
      handleSetOrigin(position[0], position[1]);
    }
  };

  return position === null ? null : (
    <Marker
      position={position}
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
