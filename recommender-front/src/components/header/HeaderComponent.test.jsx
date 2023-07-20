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
    const mockProps = {
      accessibility: 'wheelchair',
      handleChange: jest.fn(),
      times: [],
      sliderValue: 0,
      onChange: jest.fn(),
      open: false,
      handleOpen: jest.fn(),
      handleClose: jest.fn(),
      isMobile: false,
      poiData: [],
    };
    // eslint-disable-next-line react/jsx-props-no-spreading
    render(<HeaderComponent {...mockProps} />);
  });
});
