const parseSliderLabels = (times) => {
  const hours = [];
  if (times) {
    for (let i = 0; i <= times.length; i += 1) {
      const value = i;
      const label = times[i] ? times[i].split(':')[0] : '';
      hours.push({ value, label });
    }
    hours[0] = { value: 0, label: 'Now' };
  }
  return hours;
};

export default parseSliderLabels;
