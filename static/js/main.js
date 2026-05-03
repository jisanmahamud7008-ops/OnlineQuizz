document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("darkModeToggle");
    const body = document.body;
    
    // Dark mode toggle
    if (toggleBtn) {
        const isDark = localStorage.getItem("darkMode") !== "light";
        if (isDark) {
            body.classList.remove("light");
            toggleBtn.textContent = "☀️";
        } else {
            body.classList.add("light");
            toggleBtn.textContent = "🌙";
        }
        
        toggleBtn.addEventListener("click", function () {
            body.classList.toggle("light");
            const isLight = body.classList.contains("light");
            toggleBtn.textContent = isLight ? "🌙" : "☀️";
            localStorage.setItem("darkMode", isLight ? "light" : "dark");
        });
    }
    
    // Quiz card click handling
    const quizCards = document.querySelectorAll(".quiz-card");
    quizCards.forEach(card => {
        card.addEventListener("click", function() {
            this.style.transform = "scale(0.95)";
            setTimeout(() => {
                this.style.transform = "";
            }, 150);
        });
    });

    // Modal functions
    function openModal() {
        const modal = document.getElementById("loginModal");
        document.body.classList.add("modal-open");
        modal.classList.add("active");
    }

    function closeModal() {
        const modal = document.getElementById("loginModal");
        modal.classList.remove("active");
        setTimeout(() => {
            document.body.classList.remove("modal-open");
        }, 250);
    }
});