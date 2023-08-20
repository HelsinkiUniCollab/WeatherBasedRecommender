# Recommender Frontend

This is the frontend of the Weather-Based Recommender application made with React. Before running, make sure you have generated a `.env.local` -file, instructions given in the [README.md](/README.md).

## Instructions

```bash
# Install dependencies
$ npm install

# Run the app in the development mode
$ npm start
```

Runs the app in the development mode. Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes. You may also see any lint errors in the console.

### Tests

```bash
# Launches the test runner in the interactive watch mode
$ npm test

# Launches tests without the interactive watch mode
$ CI=true npm test

# Run the code validators
$ npm run lint

# Fix most of the linting issues
$ npm run lint -- --fix
```
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

### Cypress tests

For Cypress tests you need to have the frontend running locally.
API-calls to the backend are intercepted and mock-data is provided so backend is not necessary.

```bash
# Launches the test runner in a browser window
$ npm run cypress:open

# Launches tests in terminal window
$ npx cypress run
```

### Building

```bash
# Builds the app for production to the `build` folder.
$ npm run build
```
It correctly bundles React in production mode and optimizes the build for the best performance. The build is minified and the filenames include the hashes. Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.

### Docker

```bash
# Builds Docker image
$ `docker build -t recommender-frontend .`

# Run Docker container from image
$ `docker run -p 3000:3000 recommender-frontend`
```
