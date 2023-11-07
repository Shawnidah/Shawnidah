window.addEventListener('scroll', function() {
  var navbar = document.querySelector('.navbar');
  var scrolled = window.scrollY > 0;
  if (scrolled) {
    navbar.classList.add('scrolled');
  } else {
    navbar.classList.remove('scrolled');
  }
});


document.querySelector('.action-btn').addEventListener('click',function(e){
  e.preventDefault();
  e.stopPropagation();
  document.querySelector('.logging').classList.toggle('hidden');
})

window.addEventListener('click',function(e){
  if(e.target!==document.querySelector('.logging')){
    document.querySelector('.logging').classList.add('hidden');
  }
})