import React, { useState } from 'react';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import { createTheme, ThemeProvider, responsiveFontSizes } from '@mui/material/styles';
import MapComponent from './components/map/MapComponent';
import HeaderComponent from './components/header/HeaderComponent';
import 'leaflet/dist/leaflet.css';
import '@fontsource/roboto/300.css';
import './assets/style.css';

function App() {
  const [accessibility, setAccessibility] = useState('');
  let theme = createTheme();
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
        <div className="app-container">
          <div className="header-container">
            <HeaderComponent
              accessibility={accessibility}
              handleChange={handleOptionChange}
            />
          </div>
          <div className="map-container">
            <MapComponent
              accessibility={accessibility}
            />
          </div>
        </div>
      </HelmetProvider>

    </ThemeProvider>
  );
}

export default App;
