import { useCallback, useEffect } from 'react';

function PathUtil({ origin, destination, setRouteCoordinates }) {
  const handleSendCoords = useCallback(async () => {
    try {
      const apiUrl = process.env.REACT_APP_BACKEND_URL;
      const queryParams = new URLSearchParams({
        start: origin.join(','),
        end: destination.join(','),
      });

      const response = await fetch(`${apiUrl}/api/path?${queryParams}`);
      const routeCoordinates = await response.json();

      await setRouteCoordinates(routeCoordinates);
    } catch (error) {
      console.error('Error sending coordinates:', error);
    }
  }, [origin, destination, setRouteCoordinates]);

  useEffect(() => {
    if (origin && destination && origin.length === 2 && destination.length === 2) {
      handleSendCoords();
    }
  }, [origin, destination, handleSendCoords]);

  return null;
}

export default PathUtil;
