import L from 'leaflet';
import React from 'react';
import ReactDOM from 'react-dom/client';
import Typography from '@mui/material/Typography';
import createMarkerIcon from './Icon';
import DestinationButton from '../components/buttons/DestinationButton';

const createMarkers = (poiData, time, handleSetDestination) => {
  if (!poiData || !time) {
    return [];
  }

  return poiData.map((poi) => {
    const tags = Object.entries(poi.weather[time]);
    const markerIcon = createMarkerIcon(poi.weather[time].Score);
    const marker = L.marker([poi.latitude, poi.longitude], {
      icon: markerIcon,
    });

    const container = (
      <div>
        <Typography variant="h5">{poi.name}</Typography>
        <Typography variant="h8">
          {poi.catetype}
          {' '}
          /
          {' '}
          {poi.category}
        </Typography>
        <ul>
          {tags.map(([key, value]) => (
            <li key={key}>
              <Typography variant="infotext">
                <strong>{key}</strong>
                :
                {' '}
                {value}
              </Typography>
            </li>
          ))}
        </ul>
        <center>
          <DestinationButton
            onClick={() => handleSetDestination(poi.latitude, poi.longitude)}
          />
        </center>
      </div>
    );

    const divElement = document.createElement('div');
    const root = ReactDOM.createRoot(divElement);
    root.render(container);
    marker.bindPopup(divElement).openPopup();

    return marker;
  });
};

export default createMarkers;
