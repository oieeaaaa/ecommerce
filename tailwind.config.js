/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './website/**/*.{html,js,css}',
    './client/**/*.{html,js,css}',
  ],
  theme: {
    container: {
      center: true,
      padding: '1rem',
    },
  },
}
