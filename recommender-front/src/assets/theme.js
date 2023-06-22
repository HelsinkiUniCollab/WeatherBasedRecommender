import {
  createTheme,
  responsiveFontSizes,
} from '@mui/material/styles';

// eslint-disable-next-line import/no-mutable-exports
let theme = createTheme({
  palette: {
    primary: {
      main: '#2196f3',
    },
    secondary: {
      main: '#f50057',
    },
  },
  typography: {
    fontFamily: 'Roboto, Arial, sans-serif',
    // Defines sizes for h1 and h2 in different viewports
    h1: {
      fontSize: '16px',
      fontWeight: 'bold',
      '@media (min-width:600px)': {
        fontSize: '18px',
        fontWeight: 'bold',
      },
      '@media (min-width:960px)': {
        fontSize: '22px',
        fontWeight: 'bold',
      },
      '@media (min-width:1280px)': {
        fontSize: '24px',
        fontWeight: 'bold',
      },
      '@media (min-width:1920px)': {
        fontSize: '28x',
        fontWeight: 'bold',
      },
    },
    h2: {
      fontSize: '12px',
      fontWeight: 'bold',
      '@media (min-width:600px)': {
        fontSize: '12px',
        fontWeight: 'bold',
      },
      '@media (min-width:960px)': {
        fontSize: '14px',
        fontWeight: 'bold',
      },
      '@media (min-width:1280px)': {
        fontSize: '16px',
        fontWeight: 'bold',
      },
      '@media (min-width:1920px)': {
        fontSize: '18px',
        fontWeight: 'bold',
      },
    },
    infotitle: {
      fontSize: '18px',
      fontWeight: 'bold',
    },
    infotext: {
      fontSize: '14px',
    },
  },
});

theme = responsiveFontSizes(theme);

export default theme;
