import formatTimeValue from './TimeUtils';

describe('formatTimeValue', () => {
  it('returns default value for undefined input', () => {
    expect(formatTimeValue()).toBe('00:00');
  });

  it('returns the same value for valid string input', () => {
    expect(formatTimeValue('6:00')).toBe('6:00');
  });

  it('formats object input correctly', () => {
    expect(formatTimeValue({ hours: 6, minutes: 30 })).toBe('06:30');
  });

  it('returns default value for invalid object', () => {
    expect(formatTimeValue({ hours: 6 })).toBe('00:00');
  });
});
