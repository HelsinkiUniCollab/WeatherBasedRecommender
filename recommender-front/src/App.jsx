import React, { useState, useEffect } from 'react';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import {
  createTheme,
  ThemeProvider,
  responsiveFontSizes,
} from '@mui/material/styles';
import Grid from '@mui/material/Grid';
import MapComponent from './components/map/MapComponent';
import HeaderComponent from './components/header/HeaderComponent';
import 'leaflet/dist/leaflet.css';
import '@fontsource/roboto/300.css';
import './assets/style.css';

function App() {
  const [accessibility, setAccessibility] = useState('');
  const [poiData, setPoiData] = useState([]);
  const [startTime, setTimes] = useState(0);
  const [selectedValue, setSelectedValue] = useState(0);

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

  const handleSliderChange = (event) => {
    setSelectedValue(event.target.value);
  };

  useEffect(() => {
    async function fetchPoiData() {
      try {
        const apiUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000';
        const response = await fetch(`${apiUrl}/api/poi/${accessibility}`);
        const data = await response.json();
        setPoiData(data);
      } catch (error) {
        console.error('Error fetching POI data:', error);
      }
    }
    fetchPoiData();
  }, [accessibility]);
  useEffect(() => {
    if (poiData.length > 0) {
      setTimes(Object.keys(poiData[0].weather));
    }
  }, [poiData]);
  return (
    <ThemeProvider theme={theme}>
      <HelmetProvider>
        <Helmet>
          <title>Weather-Based Recommender</title>
          <meta name="description" content="Weather-Based Recommender" />
          <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"
          />
        </Helmet>
        <Grid container>
          <Grid item xs={12} className="header-container">
            <HeaderComponent
              accessibility={accessibility}
              handleChange={handleOptionChange}
              times={startTime}
              sliderValue={selectedValue}
              onChange={handleSliderChange}
            />
          </Grid>
          <Grid item xs={12} className="map-container">
            <MapComponent
              accessibility={accessibility}
              poiData={poiData}
              forecastIndex={startTime[selectedValue]}
            />
          </Grid>
        </Grid>
      </HelmetProvider>
    </ThemeProvider>
  );
}

export default App;
