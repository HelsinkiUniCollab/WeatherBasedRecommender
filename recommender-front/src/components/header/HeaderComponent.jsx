import React from 'react';
import Slider from '@mui/material/Slider';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import AccessibilityComponent from './AccessibilityComponent';
import LoadingIndicatorComponent from './LoadingIndicatorComponent';
import InfoComponent from './InfoComponent';
import parseSliderLabels from '../../utils/HeaderUtils';
import logo from '../../assets/WeatherBasedRecommender.svg';
import '../../assets/style.css';

function HeaderComponent({
  accessibility, handleChange, times, sliderValue, onChange, isMobile, open, handleOpen,
  handleClose, poiData,
}) {
  const hours = parseSliderLabels(times);
  return (
    <Grid
      container
      spacing={1}
      justifyContent="center"
      alignItems="center"
      my={1}
      key="main"
    >
      <Grid item xs={4} sm={5} md={5} lg={5} key="title">
        <img src={logo} alt="Weather-Based Recommender" className="logo" />
      </Grid>
      <Grid item xs={5} sm={5} md={5} lg={5} className="dropdown-item" key="dropdown">
        <AccessibilityComponent accessibility={accessibility} handleChange={handleChange} />
      </Grid>
      <Grid item xs={2} sm={1} md={1} lg={1}>
        <InfoComponent open={open} handleOpen={handleOpen} handleClose={handleClose} />
      </Grid>
      {isMobile ? (
        <Grid item xs={11} sm={11} className="slider-item" key="slider-mobile">
          <Typography variant="h2">Time</Typography>
          {poiData.length === 0 ? <LoadingIndicatorComponent />
            : (
              <Slider
                value={sliderValue}
                onChange={onChange}
                min={0}
                max={10}
                marks={hours}
              />
            )}
        </Grid>
      ) : (
        <Grid item xs={11} sm={11} md={11} lg={11} className="slider-item" key="slider">
          <Typography variant="h2">Time</Typography>
          {poiData.length === 0 ? <LoadingIndicatorComponent />
            : (
              <Slider
                value={sliderValue}
                onChange={onChange}
                min={0}
                max={24}
                marks={hours}
              />
            )}
        </Grid>
      )}
    </Grid>
  );
}
export default HeaderComponent;
