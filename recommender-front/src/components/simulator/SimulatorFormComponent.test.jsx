import { render, fireEvent } from '@testing-library/react';
import React from 'react';
import SimulatorFormComponent from './SimulatorFormComponent';

describe('SimulatorFormComponent', () => {
  it('renders the SimulatorFormComponent and checks form interactions', () => {
    const mockHandleInputChange = jest.fn();
    const { getByPlaceholderText } = render(<SimulatorFormComponent
      handleInputChange={mockHandleInputChange}
    />);

    const airTemperatureInput = getByPlaceholderText('Air Temperature (°C)');
    fireEvent.change(airTemperatureInput, { target: { value: '20' } });

    expect(mockHandleInputChange).toHaveBeenCalled();
  });
});
