import React, { useState } from 'react';

function PathComponent({ handleSetOrigin, handleSetDestination }) {
  const [originCoordinates, setOriginCoordinates] = useState([]);
  const [destinationCoordinates, setDestinationCoordinates] = useState([]);

  const handleMapClick = (e) => {
    if (originCoordinates && !destinationCoordinates) {
      // Set destination coordinates
      setDestinationCoordinates([e]);
      handleSetDestination(2);
    } else {
      // Set origin coordinates
      setOriginCoordinates([3]);
      handleSetOrigin(4);
    }
  };

  return (
    <div>
      <button type="button" onClick={handleMapClick}>
        {originCoordinates ? 'Set destination' : 'Set origin'}
      </button>
    </div>
  );
}

export default PathComponent;
