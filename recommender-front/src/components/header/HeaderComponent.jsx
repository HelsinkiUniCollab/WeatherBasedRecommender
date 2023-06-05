import React from 'react';
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

function HeaderComponent({ accessibility, handleChange }) {
  return (
    <Grid
      container
      spacing={1}
      my={1}
      justifyContent="center"
      align="center"
      alignItems="center"
    >
      <Grid xs={12} sm={5} md={5} mx={3} my={1}>
        <Typography variant="h4">Weather-Based Recommender</Typography>
      </Grid>
      <Grid xs={10} sm={5} md={4} mx={3} my={1}>
        <FormControl fullWidth>
          <InputLabel>Mobility issues</InputLabel>
          <Select value={accessibility} onChange={handleChange}>
            <MenuItem value="">No mobility issues</MenuItem>
            <MenuItem value="rollator">Rollator</MenuItem>
            <MenuItem value="stroller">Stroller</MenuItem>
            <MenuItem value="wheelchair">Wheelchair</MenuItem>
            <MenuItem value="reduced_mobility">Reduced mobility</MenuItem>
            <MenuItem value="visually_impaired">Visually impaired</MenuItem>
          </Select>
        </FormControl>
      </Grid>
      <Grid xs={11} sm={11} md={10} mx={5}>
        <Typography gutterBottom>Time</Typography>
        <Slider
          defaultValue={0}
          step={1}
          valueLabelDisplay="auto"
          marks
          min={0}
          max={24}
        />
      </Grid>
    </Grid>
  );
}

export default HeaderComponent;
