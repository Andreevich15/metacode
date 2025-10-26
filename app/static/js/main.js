// === ТЁМНАЯ / СВЕТЛАЯ ТЕМА ===
document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");
  const body = document.body;
  const savedTheme = localStorage.getItem("theme");

  if (savedTheme === "dark") {
    body.classList.add("dark-mode");
    if (themeToggle) themeToggle.checked = true;
  }

  if (themeToggle) {
    themeToggle.addEventListener("change", () => {
      const isDark = themeToggle.checked;
      body.classList.toggle("dark-mode", isDark);
      localStorage.setItem("theme", isDark ? "dark" : "light");
    });
  }

  // === Выделение активной кнопки урока ===
  const activeLink = document.querySelector(".block-btn.active");
  if (activeLink) activeLink.scrollIntoView({ block: "center", behavior: "smooth" });

  // === Мобильное меню ===
  const mobileBtn = document.getElementById("mobile-menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");

  if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener("click", () => {
      mobileMenu.classList.toggle("open");
      document.body.classList.toggle("overflow-hidden");
    });

    document.querySelectorAll(".mobile-link").forEach(link => {
      link.addEventListener("click", () => {
        mobileMenu.classList.remove("open");
        document.body.classList.remove("overflow-hidden");
      });
    });
  }
});
