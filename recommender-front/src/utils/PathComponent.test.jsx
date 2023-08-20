import '@testing-library/jest-dom';
import React from 'react';
import { render } from '@testing-library/react';
import PathUtil from './PathComponent';

describe('PathUtil', () => {
  it('calls setRouteCoordinates when conditions are met', async () => {
    // Mock the fetch function and its response
    global.fetch = jest.fn(() => Promise.resolve({
      json: () => Promise.resolve([[60.2049, 24.9649], [60.35, 25.355]]), // Mocked data
    }));

    const mockSetRouteCoordinates = jest.fn();
    const origin = [60.2049, 24.9649];
    const destination = [60.35, 25.355];

    render(
      <PathUtil
        origin={origin}
        destination={destination}
        setRouteCoordinates={mockSetRouteCoordinates}
      />,
    );

    // eslint-disable-next-line no-promise-executor-return
    await new Promise((resolve) => setTimeout(resolve, 0));

    // Assertions
    expect(mockSetRouteCoordinates).toHaveBeenCalled();
  });
  it('does not call handleSendCoordinates when conditions are not met', async () => {
    const mockSetRouteCoordinates = jest.fn();
    const origin = [60.2049, 24.9649];
    const destination = null;

    render(
      <PathUtil
        origin={origin}
        destination={destination}
        setRouteCoordinates={mockSetRouteCoordinates}
      />,
    );

    expect(mockSetRouteCoordinates).not.toHaveBeenCalled();
  });
});
