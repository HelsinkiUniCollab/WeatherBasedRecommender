import React, { useState } from 'react';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import MapComponent from './components/map/MapComponent';
import HeaderComponent from './components/header/HeaderComponent';
import 'leaflet/dist/leaflet.css';
import '@fontsource/roboto/300.css';

function App() {
  const [accessibility, setAccessibility] = useState('');

  const handleOptionChange = (event) => {
    setAccessibility(event.target.value);
  };

  return (
    <HelmetProvider>
      <Helmet>
        <title>Weather-Based Recommender</title>
        <meta name="description" content="Weather-Based Recommender" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
      </Helmet>
      <HeaderComponent
        accessibility={accessibility}
        handleChange={handleOptionChange}
      />
      <MapComponent accessibility={accessibility} />
    </HelmetProvider>
  );
}

export default App;
