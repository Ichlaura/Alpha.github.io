var atom = document.getElementById("atom");

function moveAtom() {
  var x = Math.random() * window.innerWidth;
  var y = Math.random() * window.innerHeight;

  atom.style.left = x + "px";
  atom.style.top = y + "px";
}

setInterval(moveAtom, 2000);
