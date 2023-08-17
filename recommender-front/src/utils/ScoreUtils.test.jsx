import defineClass from './ScoreUtils';

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
