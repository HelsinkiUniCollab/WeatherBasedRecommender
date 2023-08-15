import createMarkers from './MarkerUtils';
import '@testing-library/jest-dom';
// import { renderToString } from 'react-dom/server';
// import { act } from '@testing-library/react';

describe('createMarkers', () => {
  const poiData = [
    {
      id: '1',
      name: 'Marker 1',
      longitude: 123,
      latitude: 456,
      weather: {
        Current: {
          Temperature: '20°C',
          Humidity: '50%',
          Score: 0.5,
        },
      },
    },
    {
      id: '2',
      name: 'Marker 2',
      longitude: 789,
      latitude: 101,
      weather: {
        Current: {
          Temperature: '25°C',
          Humidity: '60%',
          Score: 0.4,
        },
      },
    },
  ];

  const time = 'Current';

  it('returns an empty array if poiData or time are not provided', () => {
    expect(createMarkers()).toEqual([]);
    expect(createMarkers(null, time)).toEqual([]);
    expect(createMarkers([], null)).toEqual([]);
  });

  it('creates markers from poiData', () => {
    const markers = createMarkers(poiData, time);
    expect(markers.length).toEqual(poiData.length);
  });

  it('binds correct score to marker', () => {
    const markers = createMarkers(poiData, time);
    const first_markers_score = markers[0][1]
    expect(first_markers_score).toEqual(0.5);
   
  });

  /*it('binds correct values to marker popup', async () => {
    act(() => {
      const markers = createMarkers(poiData, time);
      const marker = markers[0][0];
      const popupDiv = marker.getPopup()._content;
      console.log(popupDiv);
      const popupContent = popupDiv.outerHTML;
      console.log(popupContent);
      const renderi = renderToString(popupContent);
      console.log(renderi);
      expect(popupContent).toContain('<h3>Marker 1</h3>');
      expect(popupContent).toContain('<li><strong>Temperature</strong>: 20°C</li>');
      expect(popupContent).toContain('<li><strong>Humidity</strong>: 50%</li>');
    })
  });*/
});
