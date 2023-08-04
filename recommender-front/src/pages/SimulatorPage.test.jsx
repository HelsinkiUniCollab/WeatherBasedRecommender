import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import SimulatorPage from './SimulatorPage';
import '@testing-library/jest-dom/extend-expect';

// eslint-disable-next-line func-names
jest.mock('../components/simulator/SimulatorFormComponent', () => function ({ handleInputChange }) {
  return (
    <div>
      SimulatorFormComponent
      <input name="air_temperature" onChange={handleInputChange} />
    </div>
  );
});
// eslint-disable-next-line func-names
jest.mock('../components/map/MapComponent', () => function () {
  return <div>MapComponent</div>;
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
});
