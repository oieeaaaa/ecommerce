const path = require('path')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    path.resolve(__dirname, 'website/**/*.{html,js,css}'),
    path.resolve(__dirname, 'client/**/*.{html,js,css}'),
  ],
  theme: {
    container: {
      center: true,
      padding: '1rem',
    },
    fontFamily: {
      sans: ['Lato', 'sans-serif'],
    }
  },
}
