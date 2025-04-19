// Toggle month lists
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.folder.year').forEach(yearFolder => {
        yearFolder.addEventListener('click', () => {
            const monthList = yearFolder.nextElementSibling;
            const arrow = yearFolder.querySelector('.year-arrow');
            monthList.classList.toggle('active');
            arrow.textContent = monthList.classList.contains('active') ? '▼' : '▶';
        });
    });

    // Toggle post lists
    document.querySelectorAll('.folder.month').forEach(monthFolder => {
        monthFolder.addEventListener('click', (e) => {
            e.stopPropagation(); // Prevent bubbling to parent folders
            const postList = monthFolder.nextElementSibling;
            const arrow = monthFolder.querySelector('.month-arrow');
            postList.classList.toggle('active');
            arrow.textContent = postList.classList.contains('active') ? '▼' : '▶';
        });
    });
});
