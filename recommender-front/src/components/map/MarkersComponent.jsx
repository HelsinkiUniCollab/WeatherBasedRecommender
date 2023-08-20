import { useEffect, useRef } from 'react';
import L from 'leaflet';
// eslint-disable-next-line import/no-extraneous-dependencies
import 'leaflet.markercluster';
import { useMap } from 'react-leaflet';
import createMarkers from '../../utils/MarkerUtils';
import defineClass from '../../utils/ScoreUtils';

function MarkersComponent({ poiData, time, handleSetDestination }) {
  const map = useMap();
  const markerClusterGroup = useRef(null);

  useEffect(() => {
    if (poiData && time) {
      const markerData = createMarkers(poiData, time, handleSetDestination);
      const markers = markerData.map(([marker]) => marker);
      const scoreMap = new Map(markerData);
      const markerGroup = L.markerClusterGroup({
        iconCreateFunction(cluster) {
          const count = cluster.getChildCount();
          let bestScore = 0.00;
          if (cluster.getChildCount() > 0) {
            cluster.getAllChildMarkers().forEach((poiMarker) => {
              const scoreValue = scoreMap.get(poiMarker);
              if (scoreValue > bestScore) {
                bestScore = parseFloat(scoreValue);
              }
            });
          }
          const iconClass = defineClass(bestScore);

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
