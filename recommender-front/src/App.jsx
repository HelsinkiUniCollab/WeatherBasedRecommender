import React, { useState, useEffect } from 'react';
import { Helmet, HelmetProvider } from 'react-helmet-async';
import { ThemeProvider } from '@mui/material/styles';
import useMediaQuery from '@mui/material/useMediaQuery';
import Grid from '@mui/material/Grid';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import WeatherAlert from './components/warning/WeatherAlert';
import MapComponent from './components/map/MapComponent';
import HeaderComponent from './components/header/HeaderComponent';
import PathUtil from './utils/PathComponent';
import SimulatorPage from './pages/SimulatorPage';
import 'leaflet/dist/leaflet.css';
import '@fontsource/roboto/300.css';
import theme from './assets/theme';
import './assets/style.css';
// eslint-disable-next-line import/no-extraneous-dependencies
import 'leaflet.markercluster/dist/MarkerCluster.css';
// eslint-disable-next-line import/no-extraneous-dependencies
import 'leaflet.markercluster/dist/MarkerCluster.Default.css';
import medicalEnum from './MedicalFilter';

function App() {
  const [accessibility, setAccessibility] = useState('');
  const [allPoiData, setAllPoiData] = useState([]);
  const [poiData, setPoiData] = useState([]);
  const [times, setTimes] = useState(0);
  const [selectedValue, setSelectedValue] = useState(0);
  const [open, setOpen] = useState(false);
  const [showAlert, setShowAlert] = useState(false);
  const [userPosition, setUserPosition] = useState(null);
  const [destination, setDestination] = useState(null);
  const [routeCoordinates, setRouteCoordinates] = useState([]);
  const [warning, setWarning] = useState(false);
  const [headerHidden, setHeaderHidden] = useState(false);
  const [selectedCategories, setSelectedCategories] = useState(['All']);
  const [medicalCategories, setMedicalCategories] = useState(['None']);
  let poisReceived = false;
  const toggleHeader = () => {
    setHeaderHidden(!headerHidden);
  };

  const handleOptionChange = (event) => {
    setAccessibility(event);
  };

  const handleSliderChange = (event) => {
    setSelectedValue(event.target.value);
  };

  const handleOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleSetOrigin = (latitude, longitude) => {
    setUserPosition([latitude, longitude]);
  };

  const handleSetDestination = (latitude, longitude) => {
    setDestination([latitude, longitude]);
  };

  const isMobile = useMediaQuery(theme.breakpoints.down('sm'));

  const covertMedicalCategories = (medCategories) => {
    const outputCategories = [];
    for (let i = 0; i < medCategories.length; i += 1) {
      medicalEnum[medCategories[i]].forEach((element) => outputCategories.push(element));
    }
    // console.log(new Set(outputCategories));
    let tmp = new Set(outputCategories);
    tmp = Array.from(tmp);
    return tmp;
  };

  const filterPoiData = (data, access, categories, healthCategories) => {
    let filteredData = data;

    // Filter by accessibility
    if (access) {
      filteredData = filteredData.filter((poi) => !poi.not_accessible_for.includes(access));
    }

    // Get medical categories
    if (healthCategories.length > 0 && healthCategories[0] !== 'None') {
      // Narrow down categories based on medical conditions
      // console.log(filterCategories);
      const convertedCategories = covertMedicalCategories(healthCategories);
      // console.log(convertedCategories);
      filteredData = filteredData.filter((poi) => {
        const intersection = poi.all_categories.filter((element) => convertedCategories
          .includes(element));
        return intersection.length !== 0;
      });
    }
    // Filter by categories
    if (categories.length > 0 && categories[0] !== 'All') {
      filteredData = filteredData.filter((poi) => categories.includes(poi.category));
    }

    setPoiData(filteredData);
  };

  async function fetchData() {
    try {
      if (poisReceived) {
        return;
      }
      poisReceived = true;
      const apiUrl = process.env.REACT_APP_BACKEND_URL;
      const warningResponse = await fetch(`${apiUrl}/api/warning`);
      const alert = await warningResponse.json();
      setWarning(alert);
      if (!alert) {
        const poiResponse = await fetch(`${apiUrl}/api/poi`);
        const poi = await poiResponse.json();
        setAllPoiData(poi);
        filterPoiData(poi, accessibility, selectedCategories, medicalCategories);
      }
    } catch (error) {
      console.error('Error fetching the Point of Interests: ', error);
    }
  }

  useEffect(() => {
    fetchData();
  }, []);

  useEffect(() => {
    filterPoiData(allPoiData, accessibility, selectedCategories, medicalCategories);
  }, [accessibility, allPoiData, selectedCategories, medicalCategories]);

  useEffect(() => {
    if (poiData.length > 0) {
      setTimes(Object.keys(poiData[0].weather));
    }
  }, [poiData]);

  useEffect(() => {
    if (warning) {
      setShowAlert(true);
    }
  }, [warning]);

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
        <PathUtil
          origin={userPosition}
          destination={destination}
          setRouteCoordinates={setRouteCoordinates}
        />
        <Router>
          <Routes>
            <Route
              path="/"
              element={(
                <Grid container overflow="hidden" className="app-container">
                  <Grid
                    item
                    xs={12}
                    className={`header-container${showAlert || headerHidden ? ' disabled' : ''}`}
                  >
                    <HeaderComponent
                      handleChange={handleOptionChange}
                      times={times}
                      sliderValue={selectedValue}
                      onChange={handleSliderChange}
                      open={open}
                      handleOpen={handleOpen}
                      handleClose={handleClose}
                      isMobile={isMobile}
                      poiData={poiData}
                      selectedCategories={selectedCategories}
                      setSelectedCategories={setSelectedCategories}
                      medicalCategories={medicalCategories}
                      setMedicalCategories={setMedicalCategories}
                    />
                  </Grid>
                  <Grid
                    item
                    xs={12}
                    className={`map-container${showAlert ? ' disabled' : ''}${headerHidden ? ' fullscreen' : ''}`}
                  >
                    <WeatherAlert showAlert={showAlert} />
                    <MapComponent
                      accessibility={accessibility}
                      poiData={poiData}
                      time={times[selectedValue]}
                      isMobile={isMobile}
                      handleSetOrigin={handleSetOrigin}
                      userPosition={userPosition}
                      handleSetDestination={handleSetDestination}
                      routeCoordinates={routeCoordinates}
                      toggleHeader={toggleHeader}
                    />
                  </Grid>
                </Grid>
                    )}
            />
            <Route path="/admin" element={<SimulatorPage />} />
          </Routes>
        </Router>
      </HelmetProvider>
    </ThemeProvider>
  );
}

export default App;
