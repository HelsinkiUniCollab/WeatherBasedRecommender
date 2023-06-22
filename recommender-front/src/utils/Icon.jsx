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

function createMarkerIcon(value) {
  const iconOptions = {
    iconSize: [32, 32],
    popupAnchor: [1, -16],
    iconAnchor: [16, 32],
    className: 'custom-marker-icon',
  };

  const markerIcons = {
    green1: L.icon({
      ...iconOptions,
      iconUrl: basestar,
    }),
    green2: L.icon({
      ...iconOptions,
      iconUrl: basemarker2,
    }),
    green3: L.icon({
      ...iconOptions,
      iconUrl: basemarker3,
    }),
    green4: L.icon({
      ...iconOptions,
      iconUrl: basemarker4,
    }),
    green5: L.icon({
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

  if (value < 0.1) {
    markerIcon = markerIcons.red10;
  } else if (value < 0.2) {
    markerIcon = markerIcons.red9;
  } else if (value < 0.3) {
    markerIcon = markerIcons.red8;
  } else if (value < 0.4) {
    markerIcon = markerIcons.red7;
  } else if (value < 0.5) {
    markerIcon = markerIcons.red6;
  } else if (value < 0.6) {
    markerIcon = markerIcons.green5;
  } else if (value < 0.7) {
    markerIcon = markerIcons.green4;
  } else if (value < 0.8) {
    markerIcon = markerIcons.green3;
  } else if (value < 0.9) {
    markerIcon = markerIcons.green2;
  } else {
    markerIcon = markerIcons.green1;
  }

  return markerIcon;
}

export default createMarkerIcon;
