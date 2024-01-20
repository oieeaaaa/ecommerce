/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './website/**/*.{html,js}',
    './client/**/*.{html,js}',
  ],
  theme: {
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
  },
}
