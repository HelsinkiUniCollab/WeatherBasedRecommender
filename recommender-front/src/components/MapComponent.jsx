import {
  MapContainer, TileLayer, Marker, Popup,
} from 'react-leaflet';
import React, { useEffect, useState } from 'react';
import markerIcon from './icon';

function MapComponent() {
  const position = [60.2049, 24.9649];
  const [poiData, setPoiData] = useState([]);

  useEffect(() => {
    async function fetchPoiData() {
      try {
        const apiUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000';
        const response = await fetch(`${apiUrl}/api/poi`);
        const data = await response.json();
        setPoiData(data);
      } catch (error) {
        console.error('Error fetching POI data:', error);
      }
    }
    fetchPoiData();
  }, []);

  console.log(poiData);
  return (
    <MapContainer center={position} zoom={16} scrollWheelZoom={false} style={{ height: '500px', width: '500px' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {poiData.map((poi) => {
        const tags = Object.entries(poi.weather);
        return (
          <Marker
            position={[poi.location.coordinates[1], poi.location.coordinates[0]]}
            key={poi.id}
            icon={markerIcon}
          >
            <Popup>
              <h2>{poi.name.fi}</h2>
              <ul>
                {tags.map(([key, value]) => (
                  key !== 'Longitude' && key !== 'Latitude' && (
                  <li key={key}>
                    <strong>{key}</strong>
                    :
                    {' '}
                    {value}
                  </li>
                  )
                ))}
              </ul>
            </Popup>

          </Marker>
        );
      })}
    </MapContainer>
  );
}

export default MapComponent;
