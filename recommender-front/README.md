# Recommender Frontend

This is the frontend of the Weather-Based Recommender application.

### Instructions

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
```
See the section about [running tests](https://facebook.github.io/create-react-app/docs/running-tests) for more information.

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
