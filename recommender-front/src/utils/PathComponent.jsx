import { useEffect } from 'react';
import axios from 'axios';

function PathUtil({ origin, destination, setRouteCoordinates }) {
  const handleSendCoords = async () => {
    try {
      const response = await axios.get('/path', {
        params: {
          start: origin.join(','),
          end: destination.join(','),
        },
      });
      setRouteCoordinates(response.data);
      console.log('Success!');
    } catch (error) {
      console.error('Error sending coordinates:', error);
    }
  };

  useEffect(() => {
    if (origin && destination) {
      console.log('Sending coordinates to the backend:');
      handleSendCoords();
    } else {
      console.log('Either origin or destination is missing.');
    }
  }, [origin, destination, handleSendCoords]);

  return null;
}

export default PathUtil;
