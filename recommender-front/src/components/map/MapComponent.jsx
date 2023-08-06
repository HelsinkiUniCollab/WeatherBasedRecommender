import React from 'react';
import { MapContainer, TileLayer, Polyline } from 'react-leaflet';
import MarkersComponent from './MarkersComponent';
import UserLocationMarker from './UserLocationComponent';
import LocateButton from './LocateButtonComponent';
import '../../assets/style.css';

function MapComponent({
  poiData, time, handleSetOrigin, userPosition, handleSetDestination, routeCoordinates,
}) {
  const position = [60.2049, 24.9649];
  const minZoom = 12;
  const maxZoom = 18;
  const bounds = [[60, 24.6], [60.35, 25.355]];
  const viscosity = 1;

  return (
    <MapContainer
      id="map"
      center={position}
      scrollWheelZoom={false}
      zoom={minZoom}
      minZoom={minZoom}
      maxZoom={maxZoom}
      maxBounds={bounds}
      maxBoundsViscosity={viscosity}
      className="leaflet-map"
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution={
          '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }
      />
      <LocateButton
        handleSetOrigin={handleSetOrigin}
      />
      <UserLocationMarker
        userPosition={userPosition}
        handleSetOrigin={handleSetOrigin}
      />
      <MarkersComponent
        poiData={poiData}
        time={time}
        handleSetDestination={handleSetDestination}
      />
      {routeCoordinates && (
        <Polyline positions={routeCoordinates.map((coord) => [coord[1], coord[0]])} />
      )}
    </MapContainer>
  );
}

export default MapComponent;
