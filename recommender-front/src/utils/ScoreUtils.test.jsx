import { parseScore, defineClass } from './ScoreUtils';

describe('parseScore', () => {
  it('should parse score value correctly', () => {
    const poiMarker = {
      _popup: {
        _content: '<li><strong>Score</strong>: 0.89</li>',
      },
    };

    const result = parseScore(poiMarker);

    expect(result).toEqual(0.89);
  });

  it('should return null if score value is not found', () => {
    const poiMarker = {
      _popup: {
        _content: '<li><strong>Rating</strong>: 4.5</li>',
      },
    };

    const result = parseScore(poiMarker);

    expect(result).toBeNull();
  });
});

describe('defineClass', () => {
  it('should return correct class for scores below 0.5', () => {
    const score = 0.3;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-low');
  });

  it('should return correct class for scores below 0.9', () => {
    const score = 0.8;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-medium');
  });

  it('should return correct class for scores 0.9 and above', () => {
    const score = 0.95;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-high');
  });
});
