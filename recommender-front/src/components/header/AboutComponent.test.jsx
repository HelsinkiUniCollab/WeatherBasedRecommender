import React from 'react';
import { render } from '@testing-library/react';
import AboutComponent from './AboutComponent';

jest.mock('react-leaflet', () => {
  const originalModule = jest.requireActual('react-leaflet');
  return {
    ...originalModule,
    MapContainer: originalModule.MapContainer,
  };
});

describe('AboutComponent', () => {
  test('renders without crashing', () => {
    render(<AboutComponent />);
  });
});
