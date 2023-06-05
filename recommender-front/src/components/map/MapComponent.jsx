import { MapContainer, TileLayer } from 'react-leaflet';
import React, { useEffect, useState } from 'react';
import MarkersComponent from './MarkersComponent';
import '../../assets/style.css';

function MapComponent({ accessibility }) {
  const position = [60.2049, 24.9649];
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
    <MapContainer id="map" center={position} zoom={14} scrollWheelZoom={false}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      <MarkersComponent poiData={poiData} />
    </MapContainer>
  );
}

export default MapComponent;
