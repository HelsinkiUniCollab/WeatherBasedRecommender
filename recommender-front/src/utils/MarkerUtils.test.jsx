import createMarkers from './MarkerUtils';

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
        },
      },
      score: 0.5,
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
    const popupDiv = marker.getPopup().getContent();
    const popupContent = popupDiv.outerHTML;

    expect(popupContent).toContain('<h3>Marker 1</h3>');
    expect(popupContent).toContain('<li><strong>Temperature</strong>: 20°C</li>');
    expect(popupContent).toContain('<li><strong>Humidity</strong>: 50%</li>');
  });
});
