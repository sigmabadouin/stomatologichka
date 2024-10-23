/* какой-то пиздец который я не понимаю*/

document.querySelectorAll('.accordion-button').forEach(button => {
    button.addEventListener('click', () => {
        const panel = button.nextElementSibling;
        panel.style.display = panel.style.display === 'block' ? 'none' : 'block';
    });
});
