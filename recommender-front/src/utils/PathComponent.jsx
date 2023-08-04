import axios from 'axios';

function PathUtil({ origin, destination }) {
  const handleSendCoords = async () => {
    try {
      const response = await axios.post('/path', {
        origin,
        destination,
      })
        .then(console.log('Success!'));
    } catch (error) {
      console.error('Error sending coordinates:', error);
    }
  };

  if (origin && destination) {
    console.log('Sending coordinates to the backend:');
    handleSendCoords();
  } else {
    console.log('Either origin or destination is missing.');
  }
}

export default PathUtil;
