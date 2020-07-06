const buttons = document.querySelectorAll('.project');
const overlay = document.querySelector('.overlay');
const overlayImage = document.querySelector('.overlay__inner img');

function open(e) {
  overlay.classList.add('open');
  const src= e.currentTarget.querySelector('img').src;
  overlayImage.src = src;
}

function close() {
  overlay.classList.remove('open');
}

buttons.forEach(button => button.addEventListener('click', open));
overlay.addEventListener('click', close);

function dobledato() {
  
  var rs =document.getElementById("cbonombre").value;
  var n = document.getElementById("cbonombre");
  document.getElementById("rsocial").value = document.getElementById("cbonombre").value;
  //var nom = n.options[n.selectedIndex].text;
  document.getElementById("cbonombre") = n.options[n.selectedIndex].text;
  console.log(rs+"    "+nom);
  

}