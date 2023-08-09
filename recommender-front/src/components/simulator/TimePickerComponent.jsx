import React from 'react';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import Typography from '@mui/material/Typography';

function TimePickerComponent({ time, onTimeChange, namePrefix }) {
  const [hour, minute] = (time || '00:00').split(':');

  const handleHourChange = (newHour) => {
    onTimeChange(null, { hours: newHour, minutes: minute });
  };

  const handleMinuteChange = (newMinute) => {
    onTimeChange(null, { hours: hour, minutes: newMinute });
  };

  return (
    <div style={{ display: 'flex', gap: '5px' }}>
      <Select
        value={hour}
        onChange={(e) => handleHourChange(e.target.value)}
        name={`${namePrefix}-hour`}
        data-testid={`${namePrefix}-hour-selector`}
      >
        {Array.from({ length: 24 }).map((_, index) => {
          const hourValue = String(index).padStart(2, '0');
          return (
            <MenuItem key={hourValue} value={hourValue}>
              {hourValue}
            </MenuItem>
          );
        })}
      </Select>
      <Typography>:</Typography>
      <Select
        value={minute}
        onChange={(e) => handleMinuteChange(e.target.value)}
        name={`${namePrefix}-minute`}
        data-testid={`${namePrefix}-minute-selector`}
      >
        {Array.from({ length: 60 }).map((_, index) => {
          const minuteValue = String(index).padStart(2, '0');
          return (
            <MenuItem key={minuteValue} value={minuteValue}>
              {minuteValue}
            </MenuItem>
          );
        })}
      </Select>
    </div>
  );
}

export default TimePickerComponent;
