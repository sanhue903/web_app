/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [".index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        "primary": "579BB1",
        "secondary": "ECE8DD",
        "background": "F8F4EA",
      },
    },
    fontFamily: {
      Roboto: ["Roboto, sans-serif"],
    },
  },
  plugins: [],
};






