import React from 'react';
import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import WeatherAlert from './WeatherAlert';

describe('WeatherAlert', () => {
  test('renders Alert when showAlert is true', () => {
    render(<WeatherAlert showAlert />);

    const alertElement = screen.getByText(/You should avoid going outside due to strong wind./i);

    expect(alertElement).toBeInTheDocument();
  });

  test('does not render Alert when showAlert is false', () => {
    render(<WeatherAlert showAlert={false} />);

    const alertElement = screen.queryByText(/You should avoid going outside due to strong wind./i);

    expect(alertElement).not.toBeInTheDocument();
  });
});
