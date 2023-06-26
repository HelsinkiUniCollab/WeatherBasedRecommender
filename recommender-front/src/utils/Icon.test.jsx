import createMarkerIcon from './Icon';

describe('createMarkerIcon', () => {
  it('should return red marker icon if value is less than 0.5', () => {
    const value = 0.4;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker05.png');
  });

  it('should return star marker icon if value is greater than or equal to 0.5', () => {
    const value = 0.5;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker06.png');
  });
});
