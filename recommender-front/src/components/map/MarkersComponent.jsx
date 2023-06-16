import React from 'react';
import { Marker, Popup } from 'react-leaflet';
import createMarkerIcon from '../../utils/Icon';

function MarkersComponent({ poiData, time }) {
  if (poiData && time) {
    return poiData.map((poi) => {
      const tags = Object.entries(poi.weather[time]);
      const markerIcon = createMarkerIcon(poi.weather[time].score);
      return (
        <Marker
          position={[poi.location.coordinates[1], poi.location.coordinates[0]]}
          key={poi.id}
          icon={markerIcon}
          data-testid={`marker-${poi.id}`}
        >
          <Popup data-testid="popup">
            <h2>{poi.name.fi}</h2>
            <ul>
              {tags.map(([key, value]) => (
                key !== 'Longitude' && key !== 'Latitude' && key !== 'score' && (
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
    });
  }
}

export default MarkersComponent;
