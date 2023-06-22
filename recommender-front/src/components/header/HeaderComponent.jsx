import React from 'react';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import AccessibilityComponent from './AccessibilityComponent';
import AboutComponent from './AboutComponent';

function HeaderComponent({
  accessibility, handleChange, times, sliderValue, onChange, isMobile, open, handleOpen,
  handleClose,
}) {
  const hours = [];
  if (times) {
    for (let i = 0; i <= times.length; i += 1) {
      const value = i;
      const label = times[i] ? times[i].split(':')[0] : '';
      hours.push({ value, label });
    }
    hours[0] = { value: 0, label: 'Now' };
  }
  return (
    <Grid
      container
      spacing={1}
      justifyContent="center"
      alignItems="center"
      my={1}
      key="main"
    >
      <Grid item xs={5} sm={5} md={5} lg={5} key="title">
        <Typography variant="h1">Weather-Based Recommender</Typography>
      </Grid>
      <Grid item xs={5} sm={5} md={5} lg={5} className="dropdown-item" key="dropdown">
        <AccessibilityComponent accessibility={accessibility} handleChange={handleChange} />
      </Grid>
      <Grid item xs={5} sm={5} md={5} lg={5} className="dropdown-item" key="dropdown">
        <AboutComponent open={open} handleOpen={handleOpen} handleClose={handleClose} />
      </Grid>
      {isMobile ? (
        <Grid item xs={10} sm={10} className="slider-item" key="slider-mobile">
          <Typography variant="h2">Time</Typography>
          <Slider
            value={sliderValue}
            onChange={onChange}
            min={0}
            max={10}
            marks={hours}
          />
        </Grid>
      ) : (
        <Grid item xs={11} sm={11} md={10} lg={10} className="slider-item" key="slider">
          <Typography variant="h2">Time</Typography>
          <Slider
            value={sliderValue}
            onChange={onChange}
            min={0}
            max={24}
            marks={hours}
          />
        </Grid>
      )}
    </Grid>
  );
}
export default HeaderComponent;
