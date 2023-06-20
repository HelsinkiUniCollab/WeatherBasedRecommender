const mockPOIs = [
  {
    name: {
      fi: 'Mock POI 1',
      sv: 'Mock POI 1',
    },
    street_address: {
      fi: 'Mock Address 1',
      sv: 'Mock Address 1',
      en: 'Mock Address 1',
    },
    municipality: 'helsinki',
    service_nodes: [686],
    location: {
      type: 'Point',
      coordinates: [24.951, 60.170],
    },
    accessibility_shortcoming_count: {
      wheelchair: 7,
    },
    object_type: 'unit',
    weather: {
      Current: {
        'Air temperature': '18.0 °C',
        Wind: '4.0 m/s',
        'Air pressure': '1020 mbar',
        Humidity: '50.0 %',
        Latitude: 60.17523,
        Longitude: 24.94459,
        score: 1.0,
      },
      '01:00': {
        'Air temperature': '19.5 °C',
        Wind: '3.2 m/s',
        'Air pressure': '1019 mbar',
        Humidity: '45.3 %',
        score: 0.5,
      },
      '19:00': {
        'Air temperature': '18.7 °C',
        Wind: '4.5 m/s',
        'Air pressure': '1020 mbar',
        Humidity: '47.7 %',
        score: 1.0,
      },
    },
  },
  {
    name: {
      fi: 'Mock POI 2',
      sv: 'Mock POI 2',
    },
    street_address: {
      fi: 'Mock Address 2',
      sv: 'Mock Address 2',
      en: 'Mock Address 2',
    },
    municipality: 'helsinki',
    service_nodes: [686],
    location: {
      type: 'Point',
      coordinates: [24.952, 60.191],
    },
    accessibility_shortcoming_count: {
      rollator: 7,
    },
    object_type: 'unit',
    weather: {
      Current: {
        'Air temperature': '20.0 °C',
        Wind: '5.0 m/s',
        'Air pressure': '1019 mbar',
        Humidity: '45.0 %',
        Latitude: 60.17523,
        Longitude: 24.94459,
        score: 1.0,
      },
      '01:00': {
        'Air temperature': '21.5 °C',
        Wind: '3.4 m/s',
        'Air pressure': '1018 mbar',
        Humidity: '43.3 %',
        score: 0.5,
      },
      '19:00': {
        'Air temperature': '20.7 °C',
        Wind: '4.7 m/s',
        'Air pressure': '1019 mbar',
        Humidity: '44.7 %',
        score: 0.3,
      },
    },
  },
  {
    name: {
      fi: 'Mock POI 3',
      sv: 'Mock POI 3',
    },
    street_address: {
      fi: 'Mock Address 3',
      sv: 'Mock Address 3',
      en: 'Mock Address 3',
    },
    municipality: 'helsinki',
    service_nodes: [686],
    location: {
      type: 'Point',
      coordinates: [24.852, 60.178],
    },
    accessibility_shortcoming_count: {
      visually_impaired: 4,
    },
    object_type: 'unit',
    weather: {
      Current: {
        'Air temperature': '20.0 °C',
        Wind: '5.0 m/s',
        'Air pressure': '1019 mbar',
        Humidity: '45.0 %',
        Latitude: 60.17523,
        Longitude: 24.94459,
        score: 1.0,
      },
      '01:00': {
        'Air temperature': '-5.5 °C',
        Wind: '3.4 m/s',
        'Air pressure': '1018 mbar',
        Humidity: '43.3 %',
        score: 0.0,
      },
      '19:00': {
        'Air temperature': '20.7 °C',
        Wind: '4.7 m/s',
        'Air pressure': '1019 mbar',
        Humidity: '44.7 %',
        score: 0.3,
      },
    },
  },
];

export default mockPOIs;
