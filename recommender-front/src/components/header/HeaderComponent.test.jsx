import React from 'react';
import { render } from '@testing-library/react';
import HeaderComponent from './HeaderComponent';

jest.mock('react-leaflet', () => {
  const originalModule = jest.requireActual('react-leaflet');
  return {
    ...originalModule,
    MapContainer: originalModule.MapContainer,
  };
});

describe('HeaderComponent', () => {
  test('renders without crashing', () => {
    render(<HeaderComponent />);
  });
});
