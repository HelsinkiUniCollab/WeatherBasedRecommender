import React from 'react';
import { TextField } from '@mui/material';

function CustomTextField({ name, placeholder, value, handleInputChange, helperText }) {
  return (
    <TextField
      id={name}
      type="text"
      name={name}
      placeholder={placeholder}
      value={value}
      onChange={handleInputChange}
      helperText={helperText}
      inputProps={{ pattern: '\\d*' }}
      size="small"
    />
  );
}

export default CustomTextField;
