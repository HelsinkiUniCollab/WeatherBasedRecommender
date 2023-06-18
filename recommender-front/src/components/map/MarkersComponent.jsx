import { useEffect, useRef } from 'react';
import L from 'leaflet';
// eslint-disable-next-line import/no-extraneous-dependencies
import 'leaflet.markercluster';
import { useMap } from 'react-leaflet';
import createMarkers from '../../utils/MarkerUtils';

function MarkersComponent({ poiData, time }) {
  const map = useMap();
  const markerClusterGroup = useRef(null);

  useEffect(() => {
    if (poiData && time) {
      const markers = createMarkers(poiData, time);
      const markerGroup = L.markerClusterGroup();

      markers.forEach((marker) => {
        markerGroup.addLayer(marker);
      });

      if (markerClusterGroup.current) {
        map.removeLayer(markerClusterGroup.current);
      }

      markerClusterGroup.current = markerGroup;
      map.addLayer(markerGroup);
    }

    return () => {
      if (markerClusterGroup.current) {
        map.removeLayer(markerClusterGroup.current);
        markerClusterGroup.current = null;
      }
    };
  }, [poiData, time, map]);

  return null;
}

export default MarkersComponent;
