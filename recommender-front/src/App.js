import MapComponent from "./components/MapComponent";
import 'leaflet/dist/leaflet.css';

function App() {
  return (
    <div>
      <h1>
        Weather Based Recommender App
      </h1>
      <div>
        <MapComponent />
      </div>
    </div>
    
  );
}

export default App;
