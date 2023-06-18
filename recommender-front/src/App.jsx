import React, { useState, useEffect } from 'react';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import { ThemeProvider } from '@mui/material/styles';
import useMediaQuery from '@mui/material/useMediaQuery';
import Grid from '@mui/material/Grid';
import MapComponent from './components/map/MapComponent';
import HeaderComponent from './components/header/HeaderComponent';
import 'leaflet/dist/leaflet.css';
import '@fontsource/roboto/300.css';
import theme from './assets/theme';
import './assets/style.css';

function App() {
  const [accessibility, setAccessibility] = useState('');
  const [poiData, setPoiData] = useState([]);
  const [times, setTimes] = useState(0);
  const [selectedValue, setSelectedValue] = useState(0);

  const handleOptionChange = (event) => {
    setAccessibility(event.target.value);
  };

  const handleSliderChange = (event) => {
    setSelectedValue(event.target.value);
  };

  useEffect(() => {
    async function fetchPoiData() {
      try {
        const apiUrl = process.env.REACT_APP_BACKEND_URL;
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

  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

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
              times={times}
              sliderValue={selectedValue}
              onChange={handleSliderChange}
              isMobile={isMobile}
            />
          </Grid>
          <Grid item xs={12} className="map-container">
            <MapComponent
              accessibility={accessibility}
              poiData={poiData}
              time={times[selectedValue]}
              isMobile={isMobile}
            />
          </Grid>
        </Grid>
      </HelmetProvider>
    </ThemeProvider>
  );
}

export default App;
