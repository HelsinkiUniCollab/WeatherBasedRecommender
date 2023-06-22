import React from 'react';
import { Button, Dialog, DialogContent, DialogTitle } from '@mui/material';

function AboutComponent({ open, handleOpen, handleClose }) {
  return (
    <div>
      <Button onClick={handleOpen} variant="contained" color="primary" style={{ position: 'fixed', top: 10, right: 10 }}>
        About
      </Button>
      <Dialog open={open} onClose={handleClose}>
        <DialogTitle>About</DialogTitle>
        <DialogContent>
          <p>
            This website uses data from the service map (https://palvelukartta.hel.fi/en),
          </p>
          <p>
            Finnish meteorological center (https://en.ilmatieteenlaitos.fi/).
          </p>
        </DialogContent>
      </Dialog>
    </div>
  );
}

export default AboutComponent;
