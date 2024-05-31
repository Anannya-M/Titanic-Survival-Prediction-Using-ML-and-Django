document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.form form');

    form.addEventListener('submit', (event) => {
        alert('Prediction in progress...');
    });
});
