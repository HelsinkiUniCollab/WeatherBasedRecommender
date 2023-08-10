const formatTimeValue = (timeInput) => {
  if (typeof timeInput === 'string' && /^[0-9]{1,2}:[0-9]{2}$/.test(timeInput)) {
    // If input is a valid string format like '6:00', directly return it
    return timeInput;
  }

  if (timeInput && timeInput.hours !== undefined && timeInput.minutes !== undefined) {
    const { hours, minutes } = timeInput;
    return `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}`;
  }

  return '00:00'; // Default value
};

export default formatTimeValue;
