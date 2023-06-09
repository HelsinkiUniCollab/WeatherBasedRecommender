import React from 'react';
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
      <Grid item xs={4} sm={4} md={4} mx={4} my={3}>
        <Typography variant="h5">Weather-Based Recommender</Typography>
      </Grid>
      <Grid item xs={4} sm={4} md={4} lg={4} mx={3} my={1}>
        <FormControl fullWidth>
          <Select displayEmpty value={accessibility} onChange={handleChange}>
            <MenuItem value="">All attractions</MenuItem>
            <MenuItem value="rollator">Rollator-accessible</MenuItem>
            <MenuItem value="stroller">Stroller-accessible</MenuItem>
            <MenuItem value="wheelchair">Wheelchair-accessible</MenuItem>
            <MenuItem value="reduced_mobility">Reduced mobility-friendly</MenuItem>
            <MenuItem value="visually_impaired">Visually impaired-friendly</MenuItem>
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={12} sm={11} md={10} lg={9} mx={5}>
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
