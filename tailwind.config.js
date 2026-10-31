module.exports = {
  content: ['./*.html', './assets/*.js'],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Poppins', 'system-ui', 'sans-serif'],
        serif: ['Poppins', 'system-ui', 'sans-serif'],
        mono: ['Poppins', 'system-ui', 'sans-serif']
      },
      colors: {
        ink: '#0B1220',
        mute: '#5B6B82',
        line: '#E6E9EF',
        brand: { 50: '#EFF5FF', 100: '#DCE9FF', 200: '#BCD4FF', 300: '#8FB4FF', 500: '#2F6BFF', 600: '#1F57F0', 700: '#1745C7', 900: '#0B1F5C' }
      },
      boxShadow: {
        soft: '0 1px 2px rgba(11,18,32,.04), 0 12px 32px -12px rgba(11,18,32,.12)',
        lift: '0 2px 4px rgba(11,18,32,.04), 0 24px 48px -20px rgba(11,18,32,.18)',
        cta: '0 1px 2px rgba(31,87,240,.35), 0 10px 24px -10px rgba(31,87,240,.55)'
      }
    }
  },
  plugins: []
};
