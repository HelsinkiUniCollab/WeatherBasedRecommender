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
      const markerGroup = L.markerClusterGroup({
        iconCreateFunction(cluster) {
          const count = cluster.getChildCount();
          let bestScore = 0.00;
          if (cluster.getChildCount() > 0) {
            cluster.getAllChildMarkers().forEach((poiMarker) => {
              // eslint-disable-next-line no-underscore-dangle
              const html = poiMarker._popup._content;
              const parser = new DOMParser();
              const doc = parser.parseFromString(html, 'text/html');
              const scoreElement = Array.from(doc.querySelectorAll('li strong')).find(
                // eslint-disable-next-line comma-dangle
                (element) => element.textContent === 'Score'
              );
              const scoreValue = scoreElement.nextSibling.nodeValue.trim().replace(/[^\d.]/g, '');
              console.log(scoreValue);
              bestScore = parseFloat(scoreValue);
            });
          }
          console.log('Score:', bestScore);
          let iconClass = 'custom-cluster-icon';
          if (bestScore < 0.5) {
            iconClass = 'custom-cluster-icon-red2';
          } else if (bestScore < 0.7) {
            iconClass = 'custom-cluster-icon-red1';
          } else if (bestScore < 0.9) {
            iconClass = 'custom-cluster-icon-blue2';
          } else {
            iconClass = 'custom-cluster-icon-blue1';
          }
          console.log(iconClass);

          return L.divIcon({
            html: `<div class="${iconClass}">${count}</div>`,
            className: 'custom-cluster-icon',
            iconSize: [40, 40],
          });
        },
      });

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
