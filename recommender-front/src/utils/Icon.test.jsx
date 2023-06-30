import createMarkerIcon from './Icon';

describe('createMarkerIcon', () => {
  it('should return basemarker01 icon if value is less than 0.1', () => {
    const value = 0.01;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker01.png');
  });

  it('should return lbasemarker02 icon if value is less than 0.2', () => {
    const value = 0.19;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker02.png');
  });
  it('should return basemarker03 if value is less than 0.3', () => {
    const value = 0.29;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker03.png');
  });

  it('should return basemarker04 icon if value is less than 0.4', () => {
    const value = 0.39;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker04.png');
  });

  it('should return basemarker05 icon if value is less than 0.5', () => {
    const value = 0.49;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker05.png');
  });

  it('should return basemarker06 icon if value is less than 0.6', () => {
    const value = 0.59;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker06.png');
  });

  it('should return basemarker07 icon if value is less than 0.7', () => {
    const value = 0.69;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker07.png');
  });

  it('should return basemarker08 icon if value is less than 0.8', () => {
    const value = 0.79;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker08.png');
  });

  it('should return medium marker icon if value is less than 0.9', () => {
    const value = 0.89;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker09.png');
  });

  it('should return star marker icon if value is greater than or equal to 0.9', () => {
    const value = 0.9;
    const markerIcon = createMarkerIcon(value);
    expect(markerIcon.options.className).toBe('custom-marker-icon');
    expect(markerIcon.options.iconUrl).toBe('basemarker10.png');
  });
});
