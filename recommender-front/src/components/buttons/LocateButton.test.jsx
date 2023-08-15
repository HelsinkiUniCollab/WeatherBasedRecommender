import React from 'react';
import { MapContainer } from 'react-leaflet';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import LocateButton from './LocateButton';

jest.mock('leaflet', () => ({
  ...jest.requireActual('leaflet'),
  map: () => ({
    remove: jest.fn(),
  }),
}));

describe('LocateButton', () => {
  it('renders without crashing', () => {
    render(
      <MapContainer>
        <LocateButton />
      </MapContainer>,
    );
  });
});
