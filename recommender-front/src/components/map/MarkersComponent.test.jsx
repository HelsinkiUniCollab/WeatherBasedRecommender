import React from 'react';
import '@testing-library/jest-dom';
import { render, within } from '@testing-library/react';
import { MapContainer } from 'react-leaflet';
import MarkersComponent from './MarkersComponent';

jest.mock('react-leaflet', () => {
  const originalModule = jest.requireActual('react-leaflet');
  return {
    ...originalModule,
    Marker: ({ children, 'data-testid': testId }) => <div data-testid={testId}>{children}</div>,
    Popup: function MockPopup({ children, ...props }) {
      /* eslint-disable react/jsx-props-no-spreading */
      return <div {...props}>{children}</div>;
      /* eslint-enable react/jsx-props-no-spreading */
    },
  };
});

describe('MarkersComponent', () => {
  const poiData = [
    {
      id: '1',
      name: { fi: 'Marker 1' },
      location: {
        coordinates: [123, 456],
      },
      weather: {
        Current: {
          Temperature: '20°C',
          Humidity: '50%',
          Longitude: 123,
          Latitude: 456,
        },
      },
      score: 7,
    },
    {
      id: '2',
      name: { fi: 'Marker 2' },
      location: {
        coordinates: [789, 101],
      },
      weather: {
        Current: {
          Temperature: '25°C',
          Humidity: '60%',
          Longitude: 789,
          Latitude: 101,
        },
        score: 8,
      },
    },
  ];

  it('renders without crashing', () => {
    render(
      <MapContainer>
        <MarkersComponent poiData={poiData} time="Current" />
      </MapContainer>,
    );
  });

  it('renders the correct number of markers', () => {
    const { getAllByTestId } = render(
      <MapContainer>
        <MarkersComponent poiData={poiData} time="Current" />
      </MapContainer>,
    );

    const markers = getAllByTestId(/^marker-/);
    expect(markers.length).toBe(poiData.length);
  });

  it('renders a popup for each marker', () => {
    const { getAllByTestId } = render(
      <MapContainer>
        <MarkersComponent poiData={poiData} time="Current" />
      </MapContainer>,
    );

    const markers = getAllByTestId(/^marker-/);
    markers.forEach((marker) => {
      const popups = within(marker).queryAllByTestId('popup');
      expect(popups).toHaveLength(1);
    });
  });

  it('displays correct values for Temperature and Humidity', () => {
    const { getAllByTestId } = render(
      <MapContainer>
        <MarkersComponent poiData={poiData} time="Current" />
      </MapContainer>,
    );

    const markers = getAllByTestId(/^marker-/);

    markers.forEach((marker, index) => {
      const listItems = marker.querySelectorAll('li');

      const { weather } = poiData[index];

      expect(listItems[0]).toHaveTextContent(`Temperature: ${weather.Current.Temperature}`);
      expect(listItems[1]).toHaveTextContent(`Humidity: ${weather.Current.Humidity}`);
    });
  });
});
