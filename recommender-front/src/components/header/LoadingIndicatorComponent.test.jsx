import * as React from 'react';
import { render } from '@testing-library/react';
import Box from '@mui/material/Box';
import LinearProgress from '@mui/material/LinearProgress';
import LoadingIndicatorComponent from './LoadingIndicatorComponent';

export default function LinearIndeterminate() {
  return (
    <Box sx={{ width: '100%' }}>
      <LinearProgress />
    </Box>
  );
}
jest.mock('react-leaflet', () => {
  const originalModule = jest.requireActual('react-leaflet');
  return {
    ...originalModule,
    MapContainer: originalModule.MapContainer,
  };
});

describe('LoadingIndicatorComponent', () => {
  test('renders without crashing', () => {
    render(<LoadingIndicatorComponent />);
  });
});
