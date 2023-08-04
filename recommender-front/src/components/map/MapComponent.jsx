import React from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
import MarkersComponent from './MarkersComponent';
import UserLocationMarker from './PathComponent';
import LocateButton from './LocateButtonComponent';
import '../../assets/style.css';

function MapComponent({ poiData, time, handleSetOrigin, handleSetDestination }) {
  const position = [60.2049, 24.9649];
  const minZoom = 12;
  const maxZoom = 18;
  const bounds = [[60, 24.6], [60.35, 25.355]];
  const viscosity = 1;

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
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      <LocateButton
        handleSetOrigin={handleSetOrigin}
      />
      <UserLocationMarker
        handleSetOrigin={handleSetOrigin}
      />
      <MarkersComponent
        poiData={poiData}
        time={time}
        handleSetDestination={handleSetDestination}
      />
    </MapContainer>
  );
}

export default MapComponent;
