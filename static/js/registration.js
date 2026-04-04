document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("darkModeToggle");
    const body = document.body;
    const card = document.querySelector(".auth-card");
    const inputs = document.querySelectorAll("input");

    // Dark mode toggle - match main.js system
    if (toggleBtn) {
        const isDark = localStorage.getItem("darkMode") !== "light";
        if (isDark) {
            body.classList.remove("light");
            toggleBtn.textContent = "☀️";
        } else {
            body.classList.add("light");
            toggleBtn.textContent = "🌙";
            if (card) card.classList.add("dark");
            inputs.forEach(input => input.classList.add("dark"));
        }
        
        toggleBtn.addEventListener("click", function () {
            body.classList.toggle("light");
            if (card) card.classList.toggle("dark");
            inputs.forEach(input => input.classList.toggle("dark"));

            const isLight = body.classList.contains("light");
            toggleBtn.textContent = isLight ? "🌙" : "☀️";
            localStorage.setItem("darkMode", isLight ? "light" : "dark");
        });
    }

    // Password visibility toggle
    const passwordToggles = document.querySelectorAll(".toggle-password");
    passwordToggles.forEach(toggle => {
        toggle.addEventListener("click", function() {
            const input = this.previousElementSibling;
            if (input.type === "password") {
                input.type = "text";
                this.textContent = "👁️";
            } else {
                input.type = "password";
                this.textContent = "👁️‍🗨️";
            }
        });
    });
});