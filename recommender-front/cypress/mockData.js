const mockPOIs = [
  {
    name: 'Mock POI 1',
    latitude: 60.170,
    longitude: 24.951,
    weather: {
      Current: {
        'Air temperature': '18.0 °C',
        Wind: '4.0 m/s',
        'Air pressure': '1020 mbar',
        Humidity: '50.0 %',
        Score: 1.0,
      },
      '01:00': {
        'Air temperature': '19.5 °C',
        Wind: '3.2 m/s',
        'Air pressure': '1019 mbar',
        Humidity: '45.3 %',
        Score: 0.5,
      },
      '19:00': {
        'Air temperature': '18.7 °C',
        Wind: '4.5 m/s',
        'Air pressure': '1020 mbar',
        Humidity: '47.7 %',
        Score: 1.0,
      },
    },
    category: 'Sport halls',
    not_accessible_for: ['wheelchair'],
  },
  {
    name: 'Mock POI 2',
    latitude: 60.190,
    longitude: 24.951,
    weather: {
      Current: {
        'Air temperature': '20.0 °C',
        Wind: '5.0 m/s',
        'Air pressure': '1019 mbar',
        Humidity: '45.0 %',
        Score: 1.0,
      },
      '01:00': {
        'Air temperature': '-5.5 °C',
        Wind: '3.4 m/s',
        'Air pressure': '1018 mbar',
        Humidity: '43.3 %',
        Score: 0.0,
      },
      '19:00': {
        'Air temperature': '20.7 °C',
        Wind: '4.7 m/s',
        'Air pressure': '1019 mbar',
        Humidity: '44.7 %',
        Score: 0.3,
      },
    },
    category: 'Open air pools and beaches',
    not_accessible_for: [],
  },
  {
    name: 'Mock POI 3',
    latitude: 60.180,
    longitude: 24.876,
    weather: {
      Current: {
        'Air temperature': '20.0 °C',
        Wind: '5.0 m/s',
        'Air pressure': '1019 mbar',
        Humidity: '45.0 %',
        Score: 1.0,
      },
      '01:00': {
        'Air temperature': '-5.5 °C',
        Wind: '3.4 m/s',
        'Air pressure': '1018 mbar',
        Humidity: '43.3 %',
        Score: 0.0,
      },
      '19:00': {
        'Air temperature': '20.7 °C',
        Wind: '4.7 m/s',
        'Air pressure': '1019 mbar',
        Humidity: '44.7 %',
        Score: 0.3,
      },
    },
    category: 'Fitness training parks',
    not_accessible_for: [],
  },
];

export default mockPOIs;
