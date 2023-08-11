import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import PreferenceSelector from './PreferenceSelector';

describe('PreferenceSelector', () => {
  it('renders without crashing', () => {
    const { getByLabelText } = render(<PreferenceSelector selectedCategories={['All']} onCategoryChange={jest.fn()} />);
    expect(getByLabelText(/sport halls/i)).toBeInTheDocument();
    expect(getByLabelText('All')).toBeInTheDocument();
  });

  it('triggers onCategoryChange when "Sport halls" is clicked', () => {
    const mockOnCategoryChange = jest.fn();
    const { getByLabelText } = render(<PreferenceSelector selectedCategories={['All']} onCategoryChange={mockOnCategoryChange} />);

    fireEvent.click(getByLabelText(/sport halls/i));

    expect(mockOnCategoryChange).toHaveBeenCalledTimes(1);
  });
});
