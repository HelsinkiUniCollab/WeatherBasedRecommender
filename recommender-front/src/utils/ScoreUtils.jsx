const parseScore = (poiMarker) => {
  // eslint-disable-next-line no-underscore-dangle
  const html = poiMarker._popup._content;
  const parser = new DOMParser();
  const doc = parser.parseFromString(html, 'text/html');
  const scoreElement = Array.from(doc.querySelectorAll('li')).find(
    (element) => element.textContent === 'Score',
  );
  const scoreValueElement = scoreElement?.nextSibling;
  const scoreValue = scoreValueElement?.nodeValue.trim().replace(/[^\d.]/g, '');

  return scoreValue ? parseFloat(scoreValue) : null;
};

const defineClass = (bestScore) => {
  if (bestScore < 0.1) {
    return 'custom-cluster-icon-score01';
  } if (bestScore < 0.2) {
    return 'custom-cluster-icon-score02';
  } if (bestScore < 0.3) {
    return 'custom-cluster-icon-score03';
  } if (bestScore < 0.4) {
    return 'custom-cluster-icon-score04';
  } if (bestScore < 0.5) {
    return 'custom-cluster-icon-score05';
  } if (bestScore < 0.6) {
    return 'custom-cluster-icon-score06';
  } if (bestScore < 0.7) {
    return 'custom-cluster-icon-score07';
  } if (bestScore < 0.8) {
    return 'custom-cluster-icon-score08';
  } if (bestScore < 0.9) {
    return 'custom-cluster-icon-score09';
  }
  return 'custom-cluster-icon-score10';
};

export { parseScore, defineClass };
