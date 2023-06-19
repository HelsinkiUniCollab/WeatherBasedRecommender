const { defineConfig } = require('cypress');

module.exports = defineConfig({
  projectId: '2von15',
  e2e: {
    setupNodeEvents(on, config) {
    },
    baseUrl: 'http://localhost:3000',
  },
});
