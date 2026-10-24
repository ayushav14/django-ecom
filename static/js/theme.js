// Theme Switcher (Dark/Light mode persistence)
(function () {
  const getStoredTheme = () => localStorage.getItem('theme');
  const setStoredTheme = (theme) => localStorage.setItem('theme', theme);

  const getPreferredTheme = () => {
    const storedTheme = getStoredTheme();
    if (storedTheme) {
      return storedTheme;
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  };

  const setTheme = (theme) => {
    document.documentElement.setAttribute('data-bs-theme', theme);
    const themeIcon = document.getElementById('theme-icon');
    const themeText = document.getElementById('theme-text');
    
    if (themeIcon) {
      if (theme === 'dark') {
        themeIcon.className = 'bi bi-moon-stars-fill text-warning';
        if (themeText) themeText.textContent = 'Dark';
      } else {
        themeIcon.className = 'bi bi-sun-fill text-warning';
        if (themeText) themeText.textContent = 'Light';
      }
    }
  };

  // Apply immediately to prevent flash of wrong theme
  setTheme(getPreferredTheme());

  window.addEventListener('DOMContentLoaded', () => {
    setTheme(getPreferredTheme());

    const toggleBtn = document.getElementById('theme-toggle');
    if (toggleBtn) {
      toggleBtn.addEventListener('click', () => {
        const currentTheme = document.documentElement.getAttribute('data-bs-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        setStoredTheme(newTheme);
        setTheme(newTheme);
      });
    }
  });
})();
