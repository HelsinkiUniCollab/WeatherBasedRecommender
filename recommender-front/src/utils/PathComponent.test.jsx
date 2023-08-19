import '@testing-library/jest-dom';
import React from 'react';
import axios from 'axios';
import { render } from '@testing-library/react';
import PathUtil from './PathComponent';

jest.mock('axios');

describe('PathUtil', () => {
  it('calls setRouteCoordinates when conditions are met', async () => {
    const mockSetRouteCoordinates = jest.fn();
    const origin = [60.2049, 24.9649];
    const destination = [60.35, 25.355];
    const mockData = [[60.2049, 24.9649],[60.35, 25.355]]

    axios.get.mockResolvedValue({ data: mockData });

    render(
      <PathUtil
        origin={origin}
        destination={destination}
        setRouteCoordinates={mockSetRouteCoordinates}
      />,
    );
    // eslint-disable-next-line no-promise-executor-return
    await new Promise((resolve) => setTimeout(resolve, 0));

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
