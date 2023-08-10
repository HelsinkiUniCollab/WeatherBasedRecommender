import L from 'leaflet';
import React from 'react';
import ReactDOM from 'react-dom';
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import createMarkerIcon from './Icon';

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
          <Button
            size="small"
            variant="contained"
            onClick={() => handleSetDestination(poi.latitude, poi.longitude)}
          >
            Set destination
          </Button>
        </center>
      </div>
    );

    const divElement = document.createElement('div'); // Create a placeholder DOM element
    ReactDOM.render(container, divElement); // Render the JSX component into the DOM element

    marker.bindPopup(divElement).openPopup();

    return marker;
  });
};

export default createMarkers;
