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
            This website uses data from the following services/apis:
          </p>
          <p>
            <a href="https://palvelukartta.hel.fi/en">Servicemap</a>
          </p>
          <p>
            <a href="https://www.openstreetmap.org/#map=14/60.2046/24.9633">OpenStreetMap</a>
          </p>
          <p>
            <a href="https://en.ilmatieteenlaitos.fi/">Finnish meteorological institute</a>
          </p>
        </DialogContent>
      </Dialog>
    </div>
  );
}

export default AboutComponent;
