import React, { useRef, useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import MarkersComponent from './MarkersComponent';
import '../../assets/style.css';

function MapComponent({ poiData, time }) {
  const position = [60.2049, 24.9649];
  const minZoom = 12;
  const maxZoom = 18;
  const bounds = [[60, 24.6], [60.35, 25.355]];
  const viscosity = 1;
  const [userPosition, setUserPosition] = useState([60.2049, 24.9649]);
  const markerRef = useRef(null);

  const handleSetOrigin = (latitude, longitude) => {
    // setUserPosition([latitude, longitude]);
    console.log('Setting origin:', latitude, longitude);
  };

  const handleSetDestination = (latitude, longitude) => {
    console.log('Setting destination', latitude, longitude);
  };

  const handleMarkerDragEnd = () => {
    if (markerRef.current) {
      const marker = markerRef.current;
      const pos = marker.getLatLng();
      setUserPosition([pos.lat, pos.lng]);
      handleSetOrigin(userPosition[0], userPosition[1]);
    }
  };

  return (
    <MapContainer
      id="map"
      center={position}
      scrollWheelZoom={false}
      zoom={minZoom}
      minZoom={minZoom}
      maxZoom={maxZoom}
      maxBounds={bounds}
      maxBoundsViscosity={viscosity}
      // onClick={handleMapClick}
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      <Marker
        position={userPosition}
        ref={markerRef}
        draggable
        onDragEnd={handleMarkerDragEnd}
      >
        <Popup>
          <button type="button" onClick={() => handleMarkerDragEnd(Marker.position)}>Set Origin</button>
        </Popup>
      </Marker>
      <MarkersComponent
        poiData={poiData}
        time={time}
        handleSetDestination={handleSetDestination}
      />

    </MapContainer>
  );
}

export default MapComponent;
