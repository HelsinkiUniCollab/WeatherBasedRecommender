import L from 'leaflet';
import createMarkerIcon from './Icon';

const createMarkers = (poiData, time) => {
  if (!poiData || !time) {
    return [];
  }

  return poiData.map((poi) => {
    const tags = Object.entries(poi.weather[time]);
    const markerIcon = createMarkerIcon(poi.weather[time].score);
    const marker = L.marker([poi.location.coordinates[1],
      poi.location.coordinates[0]], { icon: markerIcon });
    marker.bindPopup(
      `<h3>${poi.name.fi}</h3>
        <ul>
          ${tags.map(([key, value]) => (key !== 'Longitude' && key !== 'Latitude' && key !== 'score' ? `<li><strong>${key}</strong>: ${value}</li>` : '')).join('')}
        </ul>`,
    );

    return marker;
  });
};

export default createMarkers;
