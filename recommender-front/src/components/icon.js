import L from 'leaflet';

const markerIcon = L.icon({
    iconUrl: 'https://www.freepnglogos.com/uploads/pin-png/location-pin-connectsafely-37.png',
    iconSize: [32, 32],
    popupAnchor: [1,-16]
  }
);

export { markerIcon };