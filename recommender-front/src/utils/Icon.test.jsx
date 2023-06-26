import createMarkerIcon from './Icon';

describe('createMarkerIcon', () => {
  it('should return low marker icon if value is less than 0.1', () => {
    const value = 0.1;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker-low.png');
  });

  it('should return medium marker icon if value is less than 0.9', () => {
    const value = 0.89;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker-medium.png');
  });

  it('should return star marker icon if value is greater than or equal to 0.9', () => {
    const value = 0.9;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker-high.png');
  });
});
