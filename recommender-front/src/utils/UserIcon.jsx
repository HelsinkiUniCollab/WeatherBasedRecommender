import L from 'leaflet';
import userlocation from '.../assets/markericon/userlocation.png';

function UserIcon() {
  const iconOptions = {
    iconSize: [32, 32],
    popupAnchor: [1, -16],
    iconAnchor: [16, 32],
    className: 'custom-marker-icon',
  };

  const userIcon = L.icon({
    ...iconOptions,
    iconUrl: userlocation,
  });

  let markerIcon;
  markerIcon = userIcon

  return markerIcon;
}

export default UserIcon;
