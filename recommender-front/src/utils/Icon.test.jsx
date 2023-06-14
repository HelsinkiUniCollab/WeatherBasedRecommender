import createMarkerIcon from './Icon';

describe('createMarkerIcon', () => {
  it('should return red marker icon if value is less than 0.5', () => {
    const value = 0.4;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('https://www.freepnglogos.com/uploads/pin-png/location-pin-connectsafely-37.png');
  });

  it('should return star marker icon if value is greater than or equal to 0.5', () => {
    const value = 0.5;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('https://www.freepnglogos.com/uploads/star-png/vector-graphic-star-shape-geometry-symbol-35.png');
  });
});
