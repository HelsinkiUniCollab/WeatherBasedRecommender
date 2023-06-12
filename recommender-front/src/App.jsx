import React, { useState, useEffect } from 'react';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import {
  createTheme,
  ThemeProvider,
  responsiveFontSizes,
} from '@mui/material/styles';
import MapComponent from './components/map/MapComponent';
import HeaderComponent from './components/header/HeaderComponent';
import 'leaflet/dist/leaflet.css';
import '@fontsource/roboto/300.css';

function App() {
  const [accessibility, setAccessibility] = useState('');
  const [poiData, setPoiData] = useState([]);
  const [startTime, setTimes] = useState(0);
  const [selectedValue, setSelectedValue] = useState(0);

  let theme = createTheme();
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
        <HeaderComponent
          accessibility={accessibility}
          handleChange={handleOptionChange}
          times={startTime}
          sliderValue={selectedValue}
          onChange={handleSliderChange}
        />
        <MapComponent
          accessibility={accessibility}
          poiData={poiData}
          forecastIndex={startTime[selectedValue]}
        />
      </HelmetProvider>
    </ThemeProvider>
  );
}

export default App;
