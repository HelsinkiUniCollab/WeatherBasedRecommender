import React from 'react';
import { MapContainer, TileLayer } from 'react-leaflet';
import MarkersComponent from './MarkersComponent';
import '../../assets/style.css';

function MapComponent({ poiData, forecastIndex }) {
  const position = [60.2049, 24.9649];

  return (
    <MapContainer id="map" center={position} zoom={14} scrollWheelZoom={false}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      <MarkersComponent poiData={poiData} forecast={forecastIndex} />
    </MapContainer>
  );
}

export default MapComponent;
