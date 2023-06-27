import parseSliderLabels from './HeaderUtils';

describe('parseSliderLabels', () => {
  it('should parse time labels correctly without :00 ending', () => {
    const times = ['Current', '19:00', '20:00'];
    const result = parseSliderLabels(times);
    expect(result[0]).toEqual({ label: 'Now', value: 0 });
    expect(result[1]).toEqual({ label: '19', value: 1 });
    expect(result[2]).toEqual({ label: '20', value: 2 });
  });
});
