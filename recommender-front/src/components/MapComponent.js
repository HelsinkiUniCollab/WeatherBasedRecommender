import { MapContainer, TileLayer } from 'react-leaflet';

const MapComponent = () => {
    const position = [60.2049, 24.9649];
 
    return (
        <MapContainer center={position} zoom={16} scrollWheelZoom={false} style={{ height: '500px', width: '500px'}}>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            />
        </MapContainer>
    );
};

export default MapComponent;