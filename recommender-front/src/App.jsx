import React from 'react';
import MapComponent from './components/MapComponent';
import 'leaflet/dist/leaflet.css';

function App() {
  return (
    <center>
      <h1>
        Weather-Based Recommender
      </h1>
      <div>
        <MapComponent />
      </div>
    </center>
  );
}

export default App;
