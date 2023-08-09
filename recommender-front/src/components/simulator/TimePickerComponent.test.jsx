import { render } from '@testing-library/react';
import React from 'react';
import TimePickerComponent from './TimePickerComponent';
import '@testing-library/jest-dom/extend-expect';

describe('TimePickerComponent', () => {
  it('renders without crashing', () => {
    render(<TimePickerComponent />);
  });

  it('displays the correct initial value', () => {
    const { getByDisplayValue } = render(<TimePickerComponent time="06:30" />);
    expect(getByDisplayValue('06')).toBeInTheDocument();
    expect(getByDisplayValue('30')).toBeInTheDocument();
  });
});
