import L from 'leaflet';

function createMarkerIcon(value) {
  const iconOptions = {
    iconSize: [32, 32],
    popupAnchor: [1, -16],
    iconAnchor: [16, 32],
    className: 'custom-marker-icon',
  };

  const markerIcons = {
    red: L.icon({
      ...iconOptions,
      iconUrl: 'https://www.freepnglogos.com/uploads/pin-png/location-pin-connectsafely-37.png',
    }),
    star: L.icon({
      ...iconOptions,
      iconUrl: 'https://www.freepnglogos.com/uploads/star-png/vector-graphic-star-shape-geometry-symbol-35.png',
    }),
  };

  let markerIcon;

  if (value < 0.5) {
    markerIcon = markerIcons.red;
  } else {
    markerIcon = markerIcons.star;
  }

  return markerIcon;
}

export default createMarkerIcon;
