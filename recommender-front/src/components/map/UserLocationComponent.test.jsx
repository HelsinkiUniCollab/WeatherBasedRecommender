import React from 'react';
import { render } from '@testing-library/react';
import { MapContainer } from 'react-leaflet';
import UserLocationMarker from './UserLocationComponent';

jest.mock('leaflet', () => ({
    ...jest.requireActual('leaflet'),
    map: () => ({
      remove: jest.fn(),
    }),
}));

describe('UserLocationMarker', () => {
  it('renders without crashing', () => {
    const mockPosition = [60.2049, 24.9649];
    const mockHandleSetOrigin = jest.fn();

    render(
      <MapContainer center={mockPosition} zoom={10}>
        <UserLocationMarker
          userPosition={mockPosition}
          handleSetOrigin={mockHandleSetOrigin}
        />
      </MapContainer>
    );
  });
});
