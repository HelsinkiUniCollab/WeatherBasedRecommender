import L from 'leaflet';
import createMarkerIcon from './Icon';

const createMarkers = (poiData, time) => {
  if (!poiData || !time) {
    return [];
  }

  return poiData.map((poi) => {
    const tags = Object.entries(poi.weather[time]);
    const markerIcon = createMarkerIcon(poi.weather[time].Score);
    const marker = L.marker([poi.latitude,
      poi.longitude], { icon: markerIcon });
    marker.bindPopup(
      `<h3>${poi.name}</h3>
        <ul>
        ${tags.map(([key, value]) => `<li><strong>${key}</strong>: ${value}</li>`).join('')}
        </ul>`,
    );

    return marker;
  });
};

export default createMarkers;
