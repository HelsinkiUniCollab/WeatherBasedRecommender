import { useCallback, useEffect } from 'react';
import axios from 'axios';

function PathUtil({ origin, destination, setRouteCoordinates }) {
  const handleSendCoords = useCallback(async () => {
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
  }, [origin, destination, setRouteCoordinates]);

  useEffect(() => {
    if (origin && destination && origin.length === 2 && destination.length === 2) {
      console.log('Sending coordinates to the backend:');
      handleSendCoords();
    } else {
      console.log('Either origin or destination is missing or invalid.');
    }
  }, [origin, destination, handleSendCoords]);

  return null;
}

export default PathUtil;
