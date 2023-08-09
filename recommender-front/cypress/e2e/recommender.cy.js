import mockPOIS from '../mockData';

describe('Map and POI features', () => {
  beforeEach(() => {
    cy.intercept('GET', 'http://localhost:5000/api/poi/', mockPOIS);
    cy.intercept('GET', 'http://localhost:5000/api/warning', JSON.stringify(false));
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
    clusteredMockPOIs[0].latitude = 60.190;
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
    const wheelChairMockData = mockPOIS.slice(-1);
    cy.intercept('GET', 'http://localhost:5000/api/poi/wheelchair', wheelChairMockData);
    cy.get('.MuiSelect-select').click();
    cy.get('[data-value="wheelchair"]').click();
    cy.get('.leaflet-marker-icon', { timeout: 10000 })
      .should('have.length', wheelChairMockData.length);
  });

  it('should show the weather alert when /api/warning returns true', () => {
    cy.visit('');
    cy.intercept('GET', 'http://localhost:5000/api/warning', JSON.stringify(true));
    cy.contains('You should avoid going outside due to strong wind.').should('be.visible');
  });
});

describe('SimulatorPage', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/admin');
  });

  it('should load the page', () => {
    cy.url().should('include', '/admin');
  });

  it('should render the map component', () => {
    cy.get('.simulator-map-container').should('be.visible');
  });

  it('should render the simulator form', () => {
    cy.get('.simulator-form-component').should('be.visible');
  });

  it('should show the weather alert when windSpeed is over threshold', () => {
    cy.get('input[name="windSpeed"]').clear().type('420');
    cy.contains('You should avoid going outside due to strong wind.').should('be.visible');
  });

  it('should allow input change in the SimulatorFormComponent', () => {
    cy.get('input[name="airTemperature"]').clear().type('20').should('have.value', '20');
  });
});

describe('TimePickerComponent', () => {
  // visit the page or component where TimePickerComponent is rendered
  beforeEach(() => {
    cy.visit('http://localhost:3000/admin');
  });

  it('should select an hour correctly', () => {
    cy.get('[data-testid="current-time-hour-selector"] div[role="button"]').first().click();
    cy.get('li[data-value="10"]').click();
    cy.get('[name="current-time-hour"]').should('have.value', '10');
  });

  it('should select a minute correctly', () => {
    cy.get('[data-testid="current-time-minute-selector"] div[role="button"]').first().click();
    cy.get('li[data-value="10"]').click();
    cy.get('[name="current-time-minute"]').should('have.value', '10');
  });

  it('should display correct default sunrise', () => {
    cy.get('[name="sunrise-hour"]').should('have.value', '06');
    cy.get('[name="sunrise-minute"]').should('have.value', '00');
  });

  it('should display correct default sunset', () => {
    cy.get('[name="sunset-hour"]').should('have.value', '22');
    cy.get('[name="sunset-minute"]').should('have.value', '00');
  });
});
