import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import DestinationButton from './DestinationButton';

describe('DestinationButton', () => {
  it('button responds when clicked', () => {
    const mockOnClick = jest.fn();
    const { getByText } = render(<DestinationButton onClick={mockOnClick} />);

    const button = getByText('Set destination');
    fireEvent.click(button);

    expect(mockOnClick).toHaveBeenCalledTimes(1);
  });
});
