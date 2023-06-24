import L from 'leaflet';
import basestar from '../assets/markericon/basestar.png';
import basemarker2 from '../assets/markericon/basemarker2.png';
import basemarker3 from '../assets/markericon/basemarker3.png';
import basemarker4 from '../assets/markericon/basemarker4.png';
import basemarker5 from '../assets/markericon/basemarker5.png';
import basemarker6 from '../assets/markericon/basemarker6.png';
import basemarker7 from '../assets/markericon/basemarker7.png';
import basemarker8 from '../assets/markericon/basemarker8.png';
import basemarker9 from '../assets/markericon/basemarker9.png';
import basemarker10 from '../assets/markericon/basemarker10.png';

function createMarkerIcon(score) {
  const iconOptions = {
    iconSize: [32, 32],
    popupAnchor: [1, -16],
    iconAnchor: [16, 32],
    className: 'custom-marker-icon',
  };

  const markerIcons = {
    blue1: L.icon({
      ...iconOptions,
      iconUrl: basestar,
    }),
    blue2: L.icon({
      ...iconOptions,
      iconUrl: basemarker2,
    }),
    blue3: L.icon({
      ...iconOptions,
      iconUrl: basemarker3,
    }),
    blue4: L.icon({
      ...iconOptions,
      iconUrl: basemarker4,
    }),
    blue5: L.icon({
      ...iconOptions,
      iconUrl: basemarker5,
    }),
    red6: L.icon({
      ...iconOptions,
      iconUrl: basemarker6,
    }),
    red7: L.icon({
      ...iconOptions,
      iconUrl: basemarker7,
    }),
    red8: L.icon({
      ...iconOptions,
      iconUrl: basemarker8,
    }),
    red9: L.icon({
      ...iconOptions,
      iconUrl: basemarker9,
    }),
    red10: L.icon({
      ...iconOptions,
      iconUrl: basemarker10,
    }),
  };

  let markerIcon;

  if (score < 0.1) {
    markerIcon = markerIcons.red10;
  } else if (score < 0.4) {
    markerIcon = markerIcons.red8;
  } else if (score < 0.8) {
    markerIcon = markerIcons.blue2;
  } else {
    markerIcon = markerIcons.blue1;
  }

  return markerIcon;
}

export default createMarkerIcon;
