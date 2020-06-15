$(function() {

const passBtn = document.querySelector('.pass-btn');

passBtn.addEventListener('click', (e) => {
  e.preventDefault();
  
  let passField = e.currentTarget.closest('.form').querySelector('.form__input--password');
  
  if (passField.getAttribute('type') == 'password') {
    passField.setAttribute('type', 'text');
  } else {
    passField.setAttribute('type', 'password');
  }
});
});