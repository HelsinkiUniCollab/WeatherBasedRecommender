import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import SimulatorPage from './SimulatorPage';
import '@testing-library/jest-dom/extend-expect';

// eslint-disable-next-line func-names
jest.mock('../components/simulator/SimulatorFormComponent', () => function ({ handleInputChange, handleTimeChange }) {
  // Initialize simulatedWeatherData
  const simulatedWeatherData = {
    airTemperature: '',
    windSpeed: '',
    humidity: '',
    precipitation: '',
    cloudAmount: '',
    airQuality: '',
  };
  const currentTime = '16:00';

  return (
    <div>
      SimulatorFormComponent
      <input
        name="windSpeed"
        placeholder="Wind Speed (m/s)"
        onChange={handleInputChange}
        value={simulatedWeatherData.windSpeed}
      />
      <input
        name="currentTime"
        placeholder="Current Time"
        onChange={handleTimeChange}
        value={currentTime}
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
    const { getByPlaceholderText } = render(<SimulatorPage />);
    fireEvent.change(getByPlaceholderText('Wind Speed (m/s)'), { target: { value: '25' } });
  });

  it('displays a weather alert when windSpeed is over 17', () => {
    const { getByPlaceholderText, getByText } = render(<SimulatorPage />);
    const windSpeedInput = getByPlaceholderText('Wind Speed (m/s)');
    fireEvent.change(windSpeedInput, { target: { value: '18' } });

    expect(getByText('Weather Alert')).toBeInTheDocument();
  });

  it('calls fetchData during initial render', () => {
    jest.spyOn(global, 'fetch').mockImplementation(() => Promise.resolve({
      json: () => Promise.resolve({ data: 'data' }),
    }));

    render(<SimulatorPage />);

    expect(global.fetch).toHaveBeenCalledTimes(1);

    global.fetch.mockRestore();
  });

  it('shows the overlay when currentTime is past sunset', () => {
    const { getByPlaceholderText, getByTestId } = render(<SimulatorPage />);
    const currentTimeInput = getByPlaceholderText('Current Time');
    fireEvent.change(currentTimeInput, { target: { value: '23:00' } });

    expect(getByTestId('night-overlay')).toBeInTheDocument();
  });

  it('does not render night overlay when isNightTime is false', () => {
    const { getByPlaceholderText, queryByTestId } = render(<SimulatorPage />);
    const currentTimeInput = getByPlaceholderText('Current Time');
    fireEvent.change(currentTimeInput, { target: { value: '16:00' } });

    expect(queryByTestId('night-overlay')).toBeNull();
  });
});
