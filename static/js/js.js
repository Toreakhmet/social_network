var userMenu = document.getElementById('user-menu');
var userProfile = document.getElementById('user-profile');

userProfile.addEventListener('click', function() {
    userMenu.style.display = (userMenu.style.display === 'block') ? 'none' : 'block';
});

document.addEventListener('click', function(event) {
    var isClickInside = userProfile.contains(event.target) || userMenu.contains(event.target);

    if (!isClickInside) {
        userMenu.style.display = 'none';
    }
});
document.addEventListener('DOMContentLoaded', function() {
    var posts = document.querySelectorAll('.post-content');
    posts.forEach(function(post) {
        if (post.innerText.split(' ').length > 10) {
            var truncatedText = post.innerText.split(' ').slice(0, 10).join(' ') + '...';
            post.innerHTML = `<span class="truncated">${truncatedText}</span> <span class="read-more">Далее</span>`;
        }
    });

    document.querySelectorAll('.read-more').forEach(function(button) {
        button.addEventListener('click', function() {
            var truncatedText = this.previousElementSibling.innerText;
            this.previousElementSibling.innerHTML = truncatedText.slice(0, -3); // Убираем многоточие
            this.style.display = 'none'; // Скрываем кнопку "Далее"
        });
    });
});
