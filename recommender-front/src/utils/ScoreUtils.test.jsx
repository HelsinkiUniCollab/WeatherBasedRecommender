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
  it('should return correct class for scores below 0.1', () => {
    const score = 0.01;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-score01');
  });

  it('should return correct class for scores below 0.2', () => {
    const score = 0.15;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-score02');
  });

  it('should return correct class for scores below 0.3', () => {
    const score = 0.29;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-score03');
  });

  it('should return correct class for scores below 0.4', () => {
    const score = 0.39;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-score04');
  });

  it('should return correct class for scores below 0.5', () => {
    const score = 0.49;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-score05');
  });

  it('should return correct class for scores below 06', () => {
    const score = 0.59;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-score06');
  });

  it('should return correct class for scores below 07', () => {
    const score = 0.69;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-score07');
  });

  it('should return correct class for scores below 08', () => {
    const score = 0.79;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-score08');
  });

  it('should return correct class for scores below 0.9', () => {
    const score = 0.89;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-score09');
  });

  it('should return correct class for scores 0.9 and above', () => {
    const score = 0.95;

    const result = defineClass(score);

    expect(result).toEqual('custom-cluster-icon-score10');
  });
});
