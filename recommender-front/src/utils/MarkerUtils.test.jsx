import createMarkers from './MarkerUtils';
import '@testing-library/jest-dom';

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
    const firstMarkersScore = markers[0][1];

    expect(firstMarkersScore).toEqual(0.5);
  });
});
