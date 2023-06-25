const parseScore = (poiMarker) => {
  // eslint-disable-next-line no-underscore-dangle
  const html = poiMarker._popup._content;
  const parser = new DOMParser();
  const doc = parser.parseFromString(html, 'text/html');
  const scoreElement = Array.from(doc.querySelectorAll('li strong')).find(
    (element) => element.textContent === 'Score',
  );
  const scoreValueElement = scoreElement?.nextSibling;
  const scoreValue = scoreValueElement?.nodeValue.trim().replace(/[^\d.]/g, '');

  return scoreValue ? parseFloat(scoreValue) : null;
};

const defineClass = (bestScore) => {
  if (bestScore < 0.1) {
    console.log(bestScore, ' custom-cluster-icon-score01');
    return 'custom-cluster-icon-score01';
  } if (bestScore < 0.2) {
    console.log(bestScore, ' custom-cluster-icon-score02');
    return 'custom-cluster-icon-score02';
  } if (bestScore < 0.3) {
    console.log(bestScore, ' custom-cluster-icon-score03');
    return 'custom-cluster-icon-score03';
  } if (bestScore < 0.4) {
    console.log(bestScore, ' custom-cluster-icon-score04');
    return 'custom-cluster-icon-score04';
  } if (bestScore < 0.5) {
    console.log(bestScore, ' custom-cluster-icon-score05');
    return 'custom-cluster-icon-score05';
  } if (bestScore < 0.6) {
    console.log(bestScore, ' custom-cluster-icon-score06');
    return 'custom-cluster-icon-score06';
  } if (bestScore < 0.7) {
    console.log(bestScore, ' custom-cluster-icon-score07');
    return 'custom-cluster-icon-score07';
  } if (bestScore < 0.8) {
    console.log(bestScore, ' custom-cluster-icon-score08');
    return 'custom-cluster-icon-score08';
  } if (bestScore < 0.9) {
    console.log(bestScore, ' custom-cluster-icon-score09');
    return 'custom-cluster-icon-score09';
  }
  console.log(bestScore, ' custom-cluster-icon-score10');
  return 'custom-cluster-icon-score10';
};

export { parseScore, defineClass };
