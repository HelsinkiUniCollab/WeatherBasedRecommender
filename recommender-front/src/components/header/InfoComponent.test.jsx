import React from 'react';
import { render } from '@testing-library/react';
import InfoComponent from './InfoComponent';

jest.mock('react-leaflet', () => {
  const originalModule = jest.requireActual('react-leaflet');
  return {
    ...originalModule,
    MapContainer: originalModule.MapContainer,
  };
});

describe('InfoComponent', () => {
  test('renders without crashing', () => {
    render(<InfoComponent open={false} onClose={jest.fn()} />);
  });
});
