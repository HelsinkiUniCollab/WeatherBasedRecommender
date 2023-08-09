import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import SimulatorPage from './SimulatorPage';
import '@testing-library/jest-dom/extend-expect';

// eslint-disable-next-line func-names
jest.mock('../components/simulator/SimulatorFormComponent', () => function ({ handleInputChange }) {
  // Initialize simulatedWeatherData
  const simulatedWeatherData = {
    airTemperature: '',
    windSpeed: '',
    humidity: '',
    precipitation: '',
    cloudAmount: '',
    airQuality: '',
  };

  return (
    <div>
      SimulatorFormComponent
      <input
        name="windSpeed"
        placeholder="Wind Speed (m/s)"
        onChange={handleInputChange}
        value={simulatedWeatherData.windSpeed}
      />
    </div>
  );
});

// eslint-disable-next-line func-names
jest.mock('../components/map/MapComponent', () => function () {
  return <div>MapComponent</div>;
});
// eslint-disable-next-line func-names
jest.mock('../components/warning/WeatherAlert', () => function ({ showAlert }) {
  return showAlert ? <div>Weather Alert</div> : null;
});

describe('SimulatorPage', () => {
  it('renders correctly', () => {
    const { getByText } = render(<SimulatorPage />);

    expect(getByText('SimulatorFormComponent')).toBeInTheDocument();
    expect(getByText('MapComponent')).toBeInTheDocument();
  });

  it('updates state on input change', () => {
    const { getByRole } = render(<SimulatorPage />);
    fireEvent.change(getByRole('textbox'), { target: { value: '25' } });
  });

  it('displays a weather alert when windSpeed is over 17', () => {
    const { getByPlaceholderText, getByText } = render(<SimulatorPage />);

    // Simulate a windSpeed input change event
    const windSpeedInput = getByPlaceholderText('Wind Speed (m/s)');
    fireEvent.change(windSpeedInput, { target: { value: '18' } });

    // Now, the weather alert should be present
    expect(getByText('Weather Alert')).toBeInTheDocument();
  });
});
