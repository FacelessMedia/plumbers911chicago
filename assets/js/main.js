// Mobile nav toggle
document.addEventListener('DOMContentLoaded', function() {
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.querySelector('.main-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function() {
      nav.classList.toggle('open');
      var list = nav.querySelector('.nav-list');
      if (list) {
        list.style.display = list.style.display === 'flex' ? 'none' : 'flex';
      }
    });
  }
});
