import MapComponent from "./components/MapComponent";
import 'leaflet/dist/leaflet.css';
import WeatherComponent from "./components/WeatherComponent";

function App() {
  return (
    <div>
      <h1>
        Weather Based Recommender App
      </h1>
      <div>
        <WeatherComponent />
      </div>
      <div>
        <MapComponent />
      </div>
    </div>
    
  );
}

export default App;
