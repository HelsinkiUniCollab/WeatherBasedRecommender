import L from 'leaflet';
import basemarker10 from '../assets/markericon/basemarker10.png';
import basemarker09 from '../assets/markericon/basemarker09.png';
import basemarker08 from '../assets/markericon/basemarker08.png';
import basemarker07 from '../assets/markericon/basemarker07.png';
import basemarker06 from '../assets/markericon/basemarker06.png';
import basemarker05 from '../assets/markericon/basemarker05.png';
import basemarker04 from '../assets/markericon/basemarker04.png';
import basemarker03 from '../assets/markericon/basemarker03.png';
import basemarker02 from '../assets/markericon/basemarker02.png';
import basemarker01 from '../assets/markericon/basemarker01.png';

function createMarkerIcon(value) {
  const iconOptions = {
    iconSize: [32, 32],
    popupAnchor: [1, -16],
    iconAnchor: [16, 32],
    className: 'custom-marker-icon',
  };

  const markerIcons = {
    score01: L.icon({
      ...iconOptions,
      iconUrl: basemarker01,
    }),
    score02: L.icon({
      ...iconOptions,
      iconUrl: basemarker02,
    }),
    score03: L.icon({
      ...iconOptions,
      iconUrl: basemarker03,
    }),
    score04: L.icon({
      ...iconOptions,
      iconUrl: basemarker04,
    }),
    score05: L.icon({
      ...iconOptions,
      iconUrl: basemarker05,
    }),
    score06: L.icon({
      ...iconOptions,
      iconUrl: basemarker06,
    }),
    score07: L.icon({
      ...iconOptions,
      iconUrl: basemarker07,
    }),
    score08: L.icon({
      ...iconOptions,
      iconUrl: basemarker08,
    }),
    score09: L.icon({
      ...iconOptions,
      iconUrl: basemarker09,
    }),
    score10: L.icon({
      ...iconOptions,
      iconUrl: basemarker10,
    }),
  };

  let markerIcon;

  if (value < 0.1) {
    markerIcon = markerIcons.score01;
  } else if (value < 0.2) {
    markerIcon = markerIcons.score02;
  } else if (value < 0.3) {
    markerIcon = markerIcons.score03;
  } else if (value < 0.4) {
    markerIcon = markerIcons.score04;
  } else if (value < 0.5) {
    markerIcon = markerIcons.score05;
  } else if (value < 0.6) {
    markerIcon = markerIcons.score06;
  } else if (value < 0.7) {
    markerIcon = markerIcons.score07;
  } else if (value < 0.8) {
    markerIcon = markerIcons.score08;
  } else if (value < 0.9) {
    markerIcon = markerIcons.score09;
  } else {
    markerIcon = markerIcons.score10;
  }

  return markerIcon;
}

export default createMarkerIcon;
