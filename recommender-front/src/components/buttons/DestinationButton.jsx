import React from 'react';
import Button from '@mui/material/Button';

function DestinationButton({ onClick }) {
  return (
    <Button
      size="small"
      variant="contained"
      onClick={onClick}
    >
      Set destination
    </Button>
  );
}

export default DestinationButton;
