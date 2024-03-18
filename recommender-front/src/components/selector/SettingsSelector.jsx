import React, { useEffect, useState } from 'react';
import FormControlLabel from '@mui/material/FormControlLabel';
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';
import '../../assets/style.css';
import Typography from '@mui/material/Typography';
import SettingsIcon from '@mui/icons-material/Settings';
import { Radio, RadioGroup } from '@mui/material';
import Slider from '@mui/material/Slider';

function SettingsSelector({ onProfileChange }) {
  const routeTypes = [{ name: 'Fast', val: 'fast' }, { name: 'Clean', val: 'clean' }];
  const mobilityTypes = [{ name: 'Foot', val: 'foot' }, { name: 'Wheelchair', val: 'wheelchair' }];
  const defaultRouteLen = 1000;
  const [routeLen, setRouteLen] = React.useState(defaultRouteLen);
  const defaultRouteType = 'fast';
  const [routeType, setRouteType] = React.useState(defaultRouteType);
  const defaultMobilityType = 'foot';
  const [mobilityType, setMobilityType] = React.useState(defaultMobilityType);

  const propagate = (data) => {
    onProfileChange(data);
  };

  useEffect(() => {
    propagate({ route_len: routeLen, route_type: routeType, mobility_type: mobilityType });
  }, []);

  const routeLenChange = (event, newValue) => {
    setRouteLen(newValue);
    propagate({ route_len: newValue, route_type: routeType, mobility_type: mobilityType });
  };

  const handleRouteTypeChange = (type) => {
    setRouteType(type);
    propagate({ route_len: routeLen, route_type: type, mobility_type: mobilityType });
  };

  const handleMobilityTypeChange = (type) => {
    setMobilityType(type);
    propagate({ route_len: routeLen, route_type: routeType, mobility_type: type });
  };

  const [anchorEl, setAnchorEl] = useState(null);

  const handleMenuClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  return (
    <div className="preference-selector-container">
      <IconButton
        data-testid="menu-button"
        aria-controls="category-menu"
        aria-haspopup="true"
        onClick={handleMenuClick}
        color="primary"
        size="small"
      >
        <SettingsIcon />
      </IconButton>
      <Typography variant="h7" onClick={handleMenuClick}>Path</Typography>
      <Menu
        id="category-menu"
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleMenuClose}
      >
        <IconButton
          aria-label="Close"
          aria-controls="category-menu"
          aria-haspopup="true"
          style={{ position: 'absolute', top: 0, right: 0, zIndex: 1 }}
          onClick={handleMenuClose}
        >
          <CloseIcon />
        </IconButton>
        <Typography variant="h7" sx={{ ml: 2, mt: 2 }}>
          Roundtrip length (in meters):
          {routeLen}
        </Typography>
        <Slider
          min={50}
          max={5000}
          defaultValue={defaultRouteLen}
          value={routeLen}
          onChange={routeLenChange}
          aria-labelledby="continuous-slider"
        />
        <Typography variant="h7" sx={{ ml: 2, mt: 2 }}>Route type</Typography>
        <RadioGroup defaultValue={defaultRouteType}>
          {routeTypes.map((category) => (
            <MenuItem key={category.val}>
              <FormControlLabel
                control={<Radio />}
                label={category.name}
                value={category.val}
                onChange={() => handleRouteTypeChange(category.val)}
              />
            </MenuItem>
          ))}
        </RadioGroup>
        <Typography variant="h7" sx={{ ml: 2, mt: 2 }}>Mobility</Typography>
        <RadioGroup defaultValue={defaultMobilityType}>
          {mobilityTypes.map((category) => (
            <MenuItem key={category.val}>
              <FormControlLabel
                control={<Radio />}
                label={category.name}
                value={category.val}
                onChange={() => handleMobilityTypeChange(category.val)}
              />
            </MenuItem>
          ))}
        </RadioGroup>
      </Menu>
    </div>
  );
}

export default SettingsSelector;
