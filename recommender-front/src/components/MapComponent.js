import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import React, { useEffect, useState } from 'react';
import { markerIcon } from './icon';

const MapComponent = () => {
    const position = [60.2049, 24.9649];
    const [poiData, setPoiData] = useState([]);

    useEffect(() => {
        async function fetchPoiData() {
          try {
            const apiUrl = `https://overpass-api.de/api/interpreter?data=
              [out:json];
              (
                node(around:1000,60.2049,24.9649)["tourism"];
                node(around:1000,60.2049,24.9649)["leisure"];
              );
              out;`;
            const response = await fetch(apiUrl);
            const data = await response.json();
            setPoiData(data.elements);
          } catch (error) {
            console.error('Error fetching POI data:', error);
          }
        }
    
        fetchPoiData();
      }, []);

    return (
        <MapContainer center={position} zoom={16} scrollWheelZoom={false} style={{ height: '500px', width: '500px'}}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'/>
                {poiData.map((poi) => {
                  if (!poi.tags.name) return null;

                  const tags = Object.entries(poi.tags)

                  return (
                    <Marker position={[poi.lat, poi.lon]} key={poi.id} icon={markerIcon}>
                      <Popup>
                      <h2>{poi.tags.name}</h2>
                      <ul>
                          {tags.map(([key,value]) => (
                            <li key={key}>
                                <strong>{key}</strong>: {value}
                            </li>
                          ))}
                      </ul>
                      </Popup>
                    </Marker>
                  );
                })}
        </MapContainer>
    );
};

export default MapComponent;