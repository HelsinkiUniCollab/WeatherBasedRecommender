import React from 'react';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';

function HeaderComponent({
  accessibility, handleChange, times, sliderValue, onChange,
}) {
  const hours = [];
  if (times) {
    for (let i = 0; i <= times.length; i += 1) {
      const value = i;
      const label = times[i]; // Replace with your desired value calculation
      hours.push({ label, value });
    }
  }
  return (
    <Grid
      container
      spacing={1}
      justifyContent="center"
      alignItems="center"
      my={1}
    >
      <Grid item xs={5} sm={5} md={3} lg={3}>
        <Typography variant="h1">Weather-Based Recommender</Typography>
      </Grid>
      <Grid item xs={7} sm={7} md={3} lg={3} className="dropdown-item">
        <FormControl>
          <Select displayEmpty value={accessibility} onChange={handleChange}>
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
              <Typography variant="h2">Reduced mobility supported</Typography>
            </MenuItem>
            <MenuItem value="visually_impaired">
              <Typography variant="h2">Visually impaired supported</Typography>
            </MenuItem>
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={12} sm={12} md={6} lg={6} className="slider-item">
        <Typography variant="h2">Time</Typography>
        <Slider
          value={sliderValue}
          onChange={onChange}
          min={0}
          max={24}
          marks={hours}
        />
      </Grid>
    </Grid>
  );
}

export default HeaderComponent;
