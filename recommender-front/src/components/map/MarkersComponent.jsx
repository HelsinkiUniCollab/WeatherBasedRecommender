import React from 'react';
import { Marker, Popup } from 'react-leaflet';
import createMarkerIcon from '../../utils/Icon';

function MarkersComponent({ poiData }) {
  return poiData.map((poi) => {
    const tags = Object.entries(poi.weather);
    const markerIcon = createMarkerIcon(1.0);

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
                  {value}
                </li>
              )
            ))}
          </ul>
        </Popup>
      </Marker>
    );
  });
}

export default MarkersComponent;
