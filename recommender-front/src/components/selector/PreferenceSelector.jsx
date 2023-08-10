import React from 'react';
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';

function PreferenceSelector({ selectedCategories, onCategoryChange }) {
  const allCategories = ['Sport halls', 'Open air pools and beaches', 'Athletic fields and venues', 'Neighbourhood sports facilities and parks'];

  const isAllChecked = selectedCategories.includes('All');

  const handleAllCheckboxChange = () => {
    onCategoryChange(isAllChecked ? [] : ['All']);
  };

  const handleCategoryCheckboxChange = (category) => {
    if (selectedCategories.includes(category)) {
      onCategoryChange(selectedCategories.filter((item) => item !== category));
    } else {
      onCategoryChange([...selectedCategories.filter((item) => item !== 'All'), category]);
    }
  };

  return (
    <div>
      <FormControlLabel
        control={(
          <Checkbox
            checked={isAllChecked}
            onChange={handleAllCheckboxChange}
            name="allCheckbox"
            color="primary"
          />
        )}
        label="All"
      />

      {allCategories.map((category) => (
        <FormControlLabel
          key={category}
          control={(
            <Checkbox
              checked={selectedCategories.includes(category)}
              onChange={() => handleCategoryCheckboxChange(category)}
              name={`${category}Checkbox`}
              color="primary"
            />
          )}
          label={category}
        />
      ))}
    </div>
  );
}

export default PreferenceSelector;
