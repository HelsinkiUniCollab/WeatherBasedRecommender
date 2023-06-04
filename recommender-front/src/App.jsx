import React from 'react';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import MapComponent from './components/MapComponent';
import 'leaflet/dist/leaflet.css';

function App() {
  return (
    <HelmetProvider>
      <div>
        <Helmet>
          <title> Weather-Based Recommender</title>
          <meta name="description" content="Weather-Based Recommender" />
          <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
        </Helmet>
        <center>
          <h1>
            Weather-Based Recommender
          </h1>
          <MapComponent />
        </center>
      </div>
    </HelmetProvider>
  );
}

export default App;
