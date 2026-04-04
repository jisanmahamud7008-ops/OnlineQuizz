document.addEventListener("DOMContentLoaded", function () {
    const scorePercentage = {{ percentage }};
    const resultCard = document.querySelector('.result-card');
    
    if (scorePercentage >= 80) {
        resultCard.classList.add('excellent');
    } else if (scorePercentage >= 60) {
        resultCard.classList.add('good');
    } else if (scorePercentage >= 40) {
        resultCard.classList.add('average');
    } else {
        resultCard.classList.add('poor');
    }
    
    const scoreCircle = document.querySelector('.score-circle');
    const progress = scorePercentage;
    let currentProgress = 0;
    
    function animateScore() {
        const increment = progress / 50;
        if (currentProgress < progress) {
            currentProgress += increment;
            if (currentProgress > progress) currentProgress = progress;
            scoreCircle.style.setProperty('--progress', currentProgress + '%');
            requestAnimationFrame(animateScore);
        }
    }
    
    setTimeout(animateScore, 800);
    
    const numbers = document.querySelectorAll('.detail-value');
    const score = {{ score }};
    const total = {{ total }};
    
    function animateNumber(element, target) {
        let current = 0;
        const increment = target / 30;
        function update() {
            if (current < target) {
                current += increment;
                if (current > target) current = target;
                element.textContent = Math.round(current);
                requestAnimationFrame(update);
            }
        }
        update();
    }
    
    if (numbers[0]) animateNumber(numbers[0], score);
    if (numbers[1]) animateNumber(numbers[1], total);
    if (numbers[2]) animateNumber(numbers[2], score);
    
    const scoreCircleEl = document.querySelector('.score-circle');
    let displayProgress = 0;
    const targetProgress = scorePercentage;
    
    function animateProgress() {
        if (displayProgress < targetProgress) {
            displayProgress += 1;
            scoreCircleEl.style.setProperty('--progress', displayProgress + '%');
            requestAnimationFrame(animateProgress);
        }
    }
    
    setTimeout(animateProgress, 500);
});