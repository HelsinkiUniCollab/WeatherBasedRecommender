import mockPOIS from '../mockData';

describe('Map and POI features', () => {
  beforeEach(() => {
    cy.intercept('GET', 'http://localhost:5000/api/poi/', mockPOIS);
    cy.visit('');
  });

  it('should display the MapContainer on initial load', () => {
    cy.get('.leaflet-container', { timeout: 10000 }).should('be.visible');
  });

  it('should display all POI markers on initial load', () => {
    cy.get('.leaflet-marker-icon', { timeout: 10000 })
      .should('have.length', mockPOIS.length);
  });

  it('should display clustered markers correctly', () => {
    // Create a copy of the mock POI data
    const clusteredMockPOIs = JSON.parse(JSON.stringify(mockPOIS));
    // Move one POI closer to another so they are clustered
    clusteredMockPOIs[1].location.longitude = 24.952;
    clusteredMockPOIs[1].location.latitude = 60.171;
    cy.intercept('GET', 'http://localhost:5000/api/poi/', clusteredMockPOIs);
    cy.visit('');

    cy.get('.leaflet-marker-icon', { timeout: 10000 })
      .should('have.length', mockPOIS.length - 1);
  });

  it('should update the popup content when the time slider is moved', () => {
    cy.get('.leaflet-marker-icon').first().click();

    cy.get('.leaflet-popup-content')
      .find('ul li')
      .should(($lis) => {
        expect($lis.eq(0)).to.contain('20.0 °C');
      });

    cy.get('span.MuiSlider-markLabel[data-index="1"]').click();

    cy.get('.leaflet-marker-icon').first().click();

    cy.get('.leaflet-popup-content')
      .find('ul li')
      .should(($lis) => {
        expect($lis.eq(0)).to.contain('-5.5 °C');
      });
  });

  it('should update amount of markers when accessibility is selected', () => {
    const wheelChairMockData = mockPOIS.slice(-2);
    cy.intercept('GET', 'http://localhost:5000/api/poi/wheelchair', wheelChairMockData);
    cy.get('.MuiSelect-select').click();
    cy.get('[data-value="wheelchair"]').click();
    cy.get('.leaflet-marker-icon', { timeout: 10000 })
      .should('have.length', wheelChairMockData.length);
  });
});
