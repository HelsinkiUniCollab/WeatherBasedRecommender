import React from 'react';
import { render } from '@testing-library/react';
import AccessibilityComponent from './AccessibilityComponent';

jest.mock('react-leaflet', () => {
  const originalModule = jest.requireActual('react-leaflet');
  return {
    ...originalModule,
    MapContainer: originalModule.MapContainer,
  };
});

describe('AccessibilityComponent', () => {
  test('renders without crashing', () => {
    const mockProps = {
      accessibility: 'wheelchair',
    };

    // eslint-disable-next-line react/jsx-props-no-spreading
    render(<AccessibilityComponent {...mockProps} />);
  });
});
