// === Анимация карточек ===
window.addEventListener("scroll", revealCards);
window.addEventListener("load", () => {
    revealCards();
    moveGlowLine();
    initTheme();
});

function revealCards() {
    const cards = document.querySelectorAll(".card");
    const windowHeight = window.innerHeight;
    cards.forEach((card, i) => {
        const cardTop = card.getBoundingClientRect().top;
        if (cardTop < windowHeight - 50) {
            setTimeout(() => {
                card.classList.add("visible");
            }, i * 100);
        }
    });
}

// === Glow Line ===
function moveGlowLine() {
    const activeBtn = document.querySelector(".nav-btn.active");
    const glowLine = document.getElementById("glow-line");

    if (activeBtn && glowLine) {
        const rect = activeBtn.getBoundingClientRect();
        const containerRect = document.getElementById("nav-container").getBoundingClientRect();

        glowLine.style.width = rect.width + "px";
        glowLine.style.left = rect.left - containerRect.left + "px";
    }
}
window.addEventListener("resize", moveGlowLine);

// === Theme Toggle ===
function initTheme() {
    const toggle = document.getElementById("theme-toggle");
    const savedTheme = localStorage.getItem("theme");

    if (savedTheme === "dark") {
        document.body.classList.add("dark");
        toggle.checked = true;
    }

    toggle.addEventListener("change", () => {
        document.body.classList.toggle("dark");
        localStorage.setItem("theme", document.body.classList.contains("dark") ? "dark" : "light");
    });
}
