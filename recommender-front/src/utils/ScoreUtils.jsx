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
  if (bestScore < 0.5) {
    return 'custom-cluster-icon-low';
  } if (bestScore < 0.9) {
    return 'custom-cluster-icon-medium';
  }
  return 'custom-cluster-icon-high';
};

export { parseScore, defineClass };
