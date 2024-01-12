function toggleClass(element, className) {
    if (element.classList.contains(className)) {
        element.classList.remove(className);
    } else {
        element.classList.add(className);
    }
}

document.querySelectorAll('.sidebar ul li').forEach(function (li) {
    li.addEventListener('click', function () {
        document.querySelector('.sidebar ul li.active').classList.remove('active');
        this.classList.add('active');
    });
});

document.querySelector('.open-btn').addEventListener('click', function () {
    toggleClass(document.querySelector('.sidebar'), 'active');
});

document.querySelector('.close-btn').addEventListener('click', function () {
    toggleClass(document.querySelector('.sidebar'), 'active');
});


