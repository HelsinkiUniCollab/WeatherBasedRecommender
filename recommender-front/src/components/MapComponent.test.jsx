import React from 'react';
import { render } from '@testing-library/react';
import MapComponent from './MapComponent';

jest.mock('react-leaflet', () => {
  const originalModule = jest.requireActual('react-leaflet');
  return {
    ...originalModule,
    MapContainer: originalModule.MapContainer,
  };
});

describe('MapComponent', () => {
  it('renders without crashing', () => {
    render(<MapComponent />);
  });
});
