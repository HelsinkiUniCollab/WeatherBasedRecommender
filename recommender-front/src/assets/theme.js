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
      '@media (min-width:600px)': {
        fontSize: '20px',
      },
      '@media (min-width:960px)': {
        fontSize: '28px',
      },
      '@media (min-width:1280px)': {
        fontSize: '30px',
      },
      '@media (min-width:1920px)': {
        fontSize: '32x',
      },
    },
    h2: {
      fontSize: '12px',
      '@media (min-width:600px)': {
        fontSize: '14px',
      },
      '@media (min-width:960px)': {
        fontSize: '16px',
      },
      '@media (min-width:1280px)': {
        fontSize: '18px',
      },
      '@media (min-width:1920px)': {
        fontSize: '22px',
      },
    },
  },
});

theme = responsiveFontSizes(theme);

export default theme;
