// === ТЁМНАЯ / СВЕТЛАЯ ТЕМА ===
document.addEventListener("DOMContentLoaded", () => {
  const themeToggle = document.getElementById("theme-toggle");
  const body = document.body;
  const savedTheme = localStorage.getItem("theme");
  const hljsLight = document.getElementById("hljs-theme-light");
  const hljsDark = document.getElementById("hljs-theme-dark");

  const applyHighlightTheme = isDark => {
    if (!hljsLight || !hljsDark) return;
    hljsLight.disabled = !!isDark;
    hljsDark.disabled = !isDark;
  };

  if (savedTheme === "dark") {
    body.classList.add("dark-mode");
    if (themeToggle) themeToggle.checked = true;
    applyHighlightTheme(true);
  } else {
    applyHighlightTheme(false);
  }

  if (themeToggle) {
    themeToggle.addEventListener("change", () => {
      const isDark = themeToggle.checked;
      body.classList.toggle("dark-mode", isDark);
      localStorage.setItem("theme", isDark ? "dark" : "light");
      applyHighlightTheme(isDark);
    });
  }

  // === Выделение активной кнопки урока ===
  const activeLink = document.querySelector(".block-btn.active");
  if (activeLink) activeLink.scrollIntoView({ block: "center", behavior: "smooth" });

  // === Мобильное меню ===
  const mobileBtn = document.getElementById("mobile-menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");

  const toggleBodyScroll = lock => {
    document.body.classList.toggle("overflow-hidden", lock);
  };

  if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener("click", () => {
      mobileMenu.classList.toggle("open");
      toggleBodyScroll(mobileMenu.classList.contains("open"));
    });

    document.querySelectorAll(".mobile-link").forEach(link => {
      link.addEventListener("click", () => {
        mobileMenu.classList.remove("open");
        toggleBodyScroll(false);
      });
    });
  }

  // === Панель входа администратора ===
  const adminPanel = document.getElementById("admin-login-panel");
  const adminTriggers = [
    document.getElementById("admin-login-btn"),
    document.getElementById("admin-login-mobile"),
  ].filter(Boolean);

  const closeAdminPanel = () => {
    if (!adminPanel) return;
    adminPanel.classList.remove("open");
    adminPanel.setAttribute("aria-hidden", "true");
    document.body.classList.remove("admin-login-open");
    toggleBodyScroll(false);
  };

  const openAdminPanel = () => {
    if (!adminPanel) return;
    adminPanel.classList.add("open");
    adminPanel.setAttribute("aria-hidden", "false");
    document.body.classList.add("admin-login-open");
    toggleBodyScroll(true);
    if (mobileMenu) {
      mobileMenu.classList.remove("open");
    }
  };

  adminTriggers.forEach(trigger => {
    trigger.addEventListener("click", openAdminPanel);
  });

  if (adminPanel) {
    adminPanel.addEventListener("click", event => {
      if (event.target === adminPanel) {
        closeAdminPanel();
      }
    });

    const cancelBtn = adminPanel.querySelector("[data-close-admin]");
    if (cancelBtn) {
      cancelBtn.addEventListener("click", closeAdminPanel);
    }

    document.addEventListener("keydown", event => {
      if (event.key === "Escape" && adminPanel.classList.contains("open")) {
        closeAdminPanel();
      }
    });
  }
});