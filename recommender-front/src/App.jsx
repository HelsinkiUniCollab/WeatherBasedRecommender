import React, { useState, useEffect } from 'react';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import { ThemeProvider } from '@mui/material/styles';
import useMediaQuery from '@mui/material/useMediaQuery';
import Grid from '@mui/material/Grid';
import Alert from '@mui/material/Alert';
import MapComponent from './components/map/MapComponent';
import HeaderComponent from './components/header/HeaderComponent';
import 'leaflet/dist/leaflet.css';
import '@fontsource/roboto/300.css';
import theme from './assets/theme';
import './assets/style.css';
// eslint-disable-next-line import/no-extraneous-dependencies
import 'leaflet.markercluster/dist/MarkerCluster.css';
// eslint-disable-next-line import/no-extraneous-dependencies
import 'leaflet.markercluster/dist/MarkerCluster.Default.css';

function App() {
  const [accessibility, setAccessibility] = useState('');
  const [poiData, setPoiData] = useState([]);
  const [weatherData, setWeatherData] = useState({});
  const [times, setTimes] = useState(0);
  const [selectedValue, setSelectedValue] = useState(0);
  const [showAlert, setShowAlert] = useState(false);

  const handleOptionChange = (event) => {
    setAccessibility(event.target.value);
  };

  const handleSliderChange = (event) => {
    setSelectedValue(event.target.value);
  };

  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

  useEffect(() => {
    async function fetchData() {
      try {
        const apiUrl = process.env.REACT_APP_BACKEND_URL;
        const weatherResponse = await fetch(`${apiUrl}/api/weather`);
        const weather = await weatherResponse.json();
        setWeatherData(weather);
        if (weather['Wind speed'].value < 17) {
          const poiResponse = await fetch(`${apiUrl}/api/poi/${accessibility}`);
          const poi = await poiResponse.json();
          setPoiData(poi);
        }
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    }
    fetchData();
  }, [accessibility]);
  useEffect(() => {
    if (poiData.length > 0) {
      setTimes(Object.keys(poiData[0].weather));
    }
  }, [poiData]);

  useEffect(() => {
    const weather = weatherData;
    const windSpeed = weather?.['Wind speed']?.value;
    setShowAlert(windSpeed >= 17);
  }, [weatherData]);

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
          <Grid item xs={12} className={`header-container${showAlert ? ' disabled' : ''}`}>
            <HeaderComponent
              accessibility={accessibility}
              handleChange={handleOptionChange}
              times={times}
              sliderValue={selectedValue}
              onChange={handleSliderChange}
              isMobile={isMobile}
            />
          </Grid>
          <Grid item xs={12} className={`map-container${showAlert ? ' disabled' : ''}`}>
            {showAlert && (
              <Alert severity="warning" sx={{ marginBottom: '5px' }}>
                We do not recommend going outside due to strong wind.
                The application interface has been disabled.
              </Alert>
            )}
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
