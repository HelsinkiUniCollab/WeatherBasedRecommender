import React from 'react';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Typography from '@mui/material/Typography';

function AccessibilityComponent({ accessibility, handleChange }) {
  return (
    <FormControl>
      <Select displayEmpty value={accessibility} onChange={handleChange} data-testid="accessibility-select">
        <MenuItem value="">
          <Typography variant="h2">All attractions</Typography>
        </MenuItem>
        <MenuItem value="rollator">
          <Typography variant="h2">Rollator accessible</Typography>
        </MenuItem>
        <MenuItem value="stroller">
          <Typography variant="h2">Stroller accessible</Typography>
        </MenuItem>
        <MenuItem value="wheelchair">
          <Typography variant="h2">Wheelchair accessible</Typography>
        </MenuItem>
        <MenuItem value="reduced_mobility">
          <Typography variant="h2">Reduced mobility</Typography>
        </MenuItem>
        <MenuItem value="visually_impaired">
          <Typography variant="h2">Visually impaired</Typography>
        </MenuItem>
      </Select>
    </FormControl>
  );
}

export default AccessibilityComponent;
