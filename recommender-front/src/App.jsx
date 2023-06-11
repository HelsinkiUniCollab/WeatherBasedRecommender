import React, { useState } from 'react';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import { createTheme, ThemeProvider, responsiveFontSizes } from '@mui/material/styles';
import Grid from '@mui/material/Grid';
import MapComponent from './components/map/MapComponent';
import HeaderComponent from './components/header/HeaderComponent';
import 'leaflet/dist/leaflet.css';
import '@fontsource/roboto/300.css';
import './assets/style.css';

function App() {
  const [accessibility, setAccessibility] = useState('');
  let theme = createTheme({
    typography: {
      // Defines sizes for h1 and h2 in different viewports
      h1: {
        fontSize: '16px',
        '@media (min-width:600px)': {
          fontSize: '16px',
        },
        '@media (min-width:960px)': {
          fontSize: '24px',
        },
        '@media (min-width:1280px)': {
          fontSize: '32px',
        },
        '@media (min-width:1920px)': {
          fontSize: '40px',
        },
      },
      h2: {
        fontSize: '12px',
        '@media (min-width:600px)': {
          fontSize: '14px',
        },
        '@media (min-width:960px)': {
          fontSize: '16px',
        },
        '@media (min-width:1280px)': {
          fontSize: '18px',
        },
        '@media (min-width:1920px)': {
          fontSize: '22px',
        },
      },
    },
  });

  theme = responsiveFontSizes(theme);

  const handleOptionChange = (event) => {
    setAccessibility(event.target.value);
  };

  return (
    <ThemeProvider theme={theme}>
      <HelmetProvider>
        <Helmet>
          <title>Weather-Based Recommender</title>
          <meta name="description" content="Weather-Based Recommender" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
        </Helmet>
        <Grid container>
          <Grid item xs={12} className="header-container">
            <HeaderComponent
              accessibility={accessibility}
              handleChange={handleOptionChange}
            />
          </Grid>
          <Grid item xs={12} className="map-container">
            <MapComponent
              accessibility={accessibility}
            />
          </Grid>
        </Grid>
      </HelmetProvider>

    </ThemeProvider>
  );
}

export default App;
