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
  document.getElementById("cbonombre") = n.options[n.selectedIndex].text;

}

function filterFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
  var input, filter, ul, li, a, i;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  div = document.getElementById("myDropdown");
  a = div.getElementsByTagName("option");
  for (i = 0; i < a.length; i++) {
    txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = "";
    } else {
      a[i].style.display = "none";
    }
  }
}

function dobledatito() {
  document.getElementById("rsocial").value = document.getElementById("rs").value;
  document.getElementById("myInput").value = document.getElementById("rs").text;
  console.log('aqui el pr'+ document.getElementById("rs").text);
}