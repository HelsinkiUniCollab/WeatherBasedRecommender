import React from 'react';
import '@testing-library/jest-dom';
import { render, waitFor } from '@testing-library/react';
import { rest } from 'msw';
import { setupServer } from 'msw/node';
import WeatherComponent from './WeatherComponent';

const server = setupServer(
  rest.get('*/api/weather', (req, res, ctx) => res(
    ctx.json({
      current: {
        'air temperature': '22',
        'air quality': '35',
      },
    }),
  )),
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

test('renders WeatherComponent without crashing', () => {
  render(<WeatherComponent />);
});

test('fetches and displays the weather data', async () => {
  const { getByText } = render(<WeatherComponent />);
  await waitFor(() => getByText(/22 °C 35 AQI/i));
  expect(getByText(/22 °C 35 AQI/i)).toBeInTheDocument();
});

test('handles server error', async () => {
  server.use(
    rest.get('*/api/weather', (req, res, ctx) => res(ctx.status(500))),
  );

  console.error = jest.fn();

  render(<WeatherComponent />);

  await waitFor(() => {
    expect(console.error).toHaveBeenCalled();
  });
});
