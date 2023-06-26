import L from 'leaflet';
import medium from '../assets/markericon/basemarker-medium.png';
import low from '../assets/markericon/basemarker-low.png';
import high from '../assets/markericon/basemarker-high.png';

function createMarkerIcon(value) {
  const iconOptions = {
    iconSize: [32, 32],
    popupAnchor: [1, -16],
    iconAnchor: [16, 32],
    className: 'custom-marker-icon',
  };

  const markerIcons = {
    low: L.icon({
      ...iconOptions,
      iconUrl: low,
    }),
    medium: L.icon({
      ...iconOptions,
      iconUrl: medium,
    }),
    high: L.icon({
      ...iconOptions,
      iconUrl: high,
    }),
  };

  let markerIcon;

  if (value < 0.5) {
    markerIcon = markerIcons.low;
  } else if (value < 0.9) {
    markerIcon = markerIcons.medium;
  } else {
    markerIcon = markerIcons.high;
  }

  return markerIcon;
}

export default createMarkerIcon;
