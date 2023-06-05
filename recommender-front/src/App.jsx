import React from 'react';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import MapComponent from './components/map/MapComponent';
import 'leaflet/dist/leaflet.css';
import HeaderComponent from './components/header/HeaderComponent';

function App() {
  return (
    <HelmetProvider>
      <div>
        <Helmet>
          <title> Weather-Based Recommender</title>
          <meta name="description" content="Weather-Based Recommender" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
        </Helmet>
        <HeaderComponent />
        <MapComponent />
      </div>
    </HelmetProvider>
  );
}

export default App;
