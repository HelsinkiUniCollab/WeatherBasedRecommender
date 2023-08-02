import L from 'leaflet';
import createMarkerIcon from './Icon';

const createMarkers = (poiData, time, handleSetDestination) => {
  if (!poiData || !time) {
    return [];
  }

  return poiData.map((poi) => {
    const tags = Object.entries(poi.weather[time]);
    const markerIcon = createMarkerIcon(poi.weather[time].Score);
    const marker = L.marker([poi.latitude,
      poi.longitude], { icon: markerIcon });
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = 'Set destination';

    button.onclick = () => {
      handleSetDestination(poi.latitude, poi.longitude);
    };

    const container = document.createElement('div');
    container.innerHTML = `
      <h3>${poi.name}</h3>
      <h4>${poi.catetype} / ${poi.category}</h4>
      <ul>
        ${tags.map(([key, value]) => `<li><strong>${key}</strong>: ${value}</li>`).join('')}
      </ul>
    `;
    container.appendChild(button);

    marker.bindPopup(container).openPopup();

    return marker;
  });
};

export default createMarkers;
