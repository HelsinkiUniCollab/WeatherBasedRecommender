import { MapContainer, TileLayer } from 'react-leaflet';
import React, { useEffect, useState } from 'react';
import MarkersComponent from './MarkersComponent';
import '../../assets/style.css';

function MapComponent({ accessibility }) {
  const position = [60.2049, 24.9649];
  const minZoom = 12;
  const maxZoom = 20;
  const bounds = [[60, 24.6], [60.35, 25.355]];
  const viscosity = 1;
  const [poiData, setPoiData] = useState([]);

  useEffect(() => {
    async function fetchPoiData() {
      try {
        const apiUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000';
        const response = await fetch(`${apiUrl}/api/poi/${accessibility}`);
        const data = await response.json();
        setPoiData(data);
      } catch (error) {
        console.error('Error fetching POI data:', error);
      }
    }
    fetchPoiData();
  }, [accessibility]);

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
      <MarkersComponent poiData={poiData} />
    </MapContainer>
  );
}

export default MapComponent;
