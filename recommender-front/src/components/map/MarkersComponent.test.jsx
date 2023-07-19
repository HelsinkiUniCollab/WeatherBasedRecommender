import React from 'react';
import { render } from '@testing-library/react';
import { useMap } from 'react-leaflet';
import MarkersComponent from './MarkersComponent';

jest.mock('react-leaflet', () => ({
  useMap: jest.fn(),
}));

jest.mock('../../utils/MarkerUtils', () => ({
  __esModule: true,
  default: jest.fn(),
}));

describe('MarkersComponent', () => {
  afterEach(() => {
    jest.clearAllMocks();
  });

  it('renders without error', () => {
    const poiData = [];
    const time = '';
    useMap.mockReturnValue({ removeLayer: jest.fn(), addLayer: jest.fn() });
    render(<MarkersComponent poiData={poiData} time={time} />);
  });
});
