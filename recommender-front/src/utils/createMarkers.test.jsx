import createMarkers from './MarkerUtils';

describe('createMarkers', () => {
  const poiData = [
    {
      id: '1',
      name: { fi: 'Marker 1' },
      location: {
        coordinates: [123, 456],
      },
      weather: {
        Current: {
          Temperature: '20°C',
          Humidity: '50%',
          Longitude: 123,
          Latitude: 456,
        },
      },
      score: 0.5,
    },
    {
      id: '2',
      name: { fi: 'Marker 2' },
      location: {
        coordinates: [789, 101],
      },
      weather: {
        Current: {
          Temperature: '25°C',
          Humidity: '60%',
          Longitude: 789,
          Latitude: 101,
        },
        score: 0.4,
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

  it('binds correct values to marker popup', () => {
    const markers = createMarkers(poiData, time);

    const marker = markers[0];
    const popupContent = marker.getPopup().getContent();

    expect(popupContent).toContain('<h2>Marker 1</h2>');
    expect(popupContent).toContain('<li><strong>Temperature</strong>: 20°C</li>');
    expect(popupContent).toContain('<li><strong>Humidity</strong>: 50%</li>');
  });
});
