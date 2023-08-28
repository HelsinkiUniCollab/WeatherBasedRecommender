import mockPOIs from '../mockData';
import mockROUTE from '../mockRoute';

describe('Map and POI features', () => {
  beforeEach(() => {
    cy.intercept('GET', 'http://localhost:5000/api/poi', mockPOIs);
    cy.intercept('GET', 'http://localhost:5000/api/warning', JSON.stringify(false));
    cy.visit('');
  });

  it('should display the MapContainer on initial load', () => {
    cy.get('.leaflet-container', { timeout: 10000 }).should('be.visible');
  });

  it('should display all POI markers on initial load', () => {
    cy.get('.leaflet-marker-icon', { timeout: 10000 })
      .should('have.length', mockPOIs.length);
  });

  it('should display clustered markers correctly', () => {
    // Create a copy of the mock POI data
    const clusteredMockPOIs = JSON.parse(JSON.stringify(mockPOIs));
    // Move one POI closer to another so they are clustered
    clusteredMockPOIs[0].latitude = 60.190;
    cy.intercept('GET', 'http://localhost:5000/api/poi', clusteredMockPOIs);
    cy.visit('');

    cy.get('.leaflet-marker-icon', { timeout: 10000 })
      .should('have.length', mockPOIs.length - 1);
  });

  it('should update the popup content when the time slider is moved', () => {
    cy.get('.leaflet-marker-icon').first().click();

    cy.get('.leaflet-popup-content')
      .find('center')
      .should(($lis) => {
        expect($lis.eq(0)).to.contain('20.0 °C');
      });

    cy.get('span.MuiSlider-markLabel[data-index="1"]').click();

    cy.get('.leaflet-marker-icon').first().click();

    cy.get('.leaflet-popup-content')
      .find('center')
      .should(($lis) => {
        expect($lis.eq(0)).to.contain('-5.5 °C');
      });
  });

  it('should update amount of markers when accessibility is selected', () => {
    const filteredMockPOIs = mockPOIs.filter((poi) => !poi.not_accessible_for.includes('wheelchair'));

    cy.get('.MuiSelect-select').click();
    cy.get('[data-value="wheelchair"]').click();
    cy.get('.leaflet-marker-icon', { timeout: 10000 })
      .should('have.length', filteredMockPOIs.length);
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

  it('should not throw when temperature input is dash', () => {
    cy.get('input[name="airTemperature"]').clear().type('-').should('have.value', '-');
  });
});

describe('TimePickerComponent', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000/admin');
  });

  it('should select an hour correctly', () => {
    cy.get('[data-testid="current-time-hour-selector"] div[role="button"]').first().click();
    cy.get('li[data-value="00"]').click();
    cy.get('[name="current-time-hour"]').should('have.value', '00');
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

describe('PreferenceSelector component', () => {
  beforeEach(() => {
    cy.intercept('GET', 'http://localhost:5000/api/poi', mockPOIs);
    cy.intercept('GET', 'http://localhost:5000/api/warning', JSON.stringify(false));
    cy.visit('');
  });

  it('should have the "All" checkbox checked by default', () => {
    cy.get('input[name="allCheckbox"]').should('be.checked');
  });

  it('should deselect the "All" checkbox when another category is selected', () => {
    cy.get('[data-testid="menu-button"]').click();
    cy.get('input[name="Sport hallsCheckbox"]').check();
    cy.get('input[name="allCheckbox"]').should('be.not.be.checked');
  });

  it('should show only Sport halls markers when the "Sport halls" category is selected', () => {
    const sportHallsMockData = mockPOIs.filter((poi) => poi.category === 'Sport halls');

    cy.get('[data-testid="menu-button"]').click();
    cy.get('input[name="Sport hallsCheckbox"]').check();
    cy.get('.leaflet-marker-icon', { timeout: 10000 })
      .should('have.length', sportHallsMockData.length);
  });

  it('should select the "All" checkbox and deselect others when "All" is selected', () => {
    cy.get('[data-testid="menu-button"]').click();
    cy.get('input[name="Sport hallsCheckbox"]').check();
    cy.get('input[name="allCheckbox"]').check();
    cy.get('input[name="Sport hallsCheckbox"]').should('not.be.checked');
    cy.get('input[name="allCheckbox"]').should('be.checked');
  });

  it('should show all markers when the "All" category is re-selected', () => {
    cy.get('[data-testid="menu-button"]').click();
    cy.get('input[name="Sport hallsCheckbox"]').check();
    cy.get('input[name="allCheckbox"]').check();
    cy.get('.leaflet-marker-icon', { timeout: 10000 })
      .should('have.length', mockPOIs.length);
  });

  it('should show only Sport halls and wheelchair accessible markers when both filters are selected', () => {
    const filteredMockPOIs = mockPOIs.filter((poi) => !poi.not_accessible_for.includes('wheelchair')
      && poi.category === 'sport halls');

    cy.get('[data-testid="menu-button"]').click();
    cy.get('input[name="Sport hallsCheckbox"]').check();
    cy.get('button[aria-label="Close"]').click();

    cy.get('.MuiSelect-select').click();
    cy.get('[data-value="wheelchair"]').click();

    cy.get('.leaflet-marker-icon', { timeout: 10000 })
      .should('have.length', filteredMockPOIs.length);
  });
});

describe('User location and routing feature', () => {
  const latitude = 60.169520;
  const longitude = 24.935450;

  beforeEach(() => {
    cy.intercept('GET', 'http://localhost:5000/api/poi', mockPOIs);
    cy.intercept('GET', 'http://localhost:5000/api/warning', JSON.stringify(false));
    cy.window().then((win) => {
      cy.stub(win.navigator.geolocation, 'getCurrentPosition', (callback) => callback({ coords: { latitude, longitude } }));
    });
    cy.visit('');
  });

  it('should locate the user, open a POI and set a destination, draw the polyline', () => {
    cy.get('[data-testid="locate-button"]').should('be.visible').click();
    cy.get('.leaflet-marker-icon').eq(1).click();
    cy.get('.leaflet-popup-content');
    cy.intercept('GET', '**/path?start=*&end=*', { body: mockROUTE }).as('getRoute');
    cy.get('[data-cy="set-destination-button"]').click();
    cy.get('#map').find('path.leaflet-interactive').should('exist');
  });
});
