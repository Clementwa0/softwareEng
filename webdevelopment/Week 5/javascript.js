document.getElementById("greetButton").onclick = function() {
    document.getElementById("demo").innerHTML = " World!";

    const demo = document.getElementById("demo");
    demo.style.color = "red";
    demo.style.backgroundColor = "yellow";
    demo.style.fontSize = "30px"; 
    demo.style.fontFamily = "Arial, sans-serif";
    demo.style.fontWeight = "bold";

}

function changeColor(){
  const colors = ["lightcoral", "lightblue", "lightgreen", "lavender", "peachpuff", "khaki"];
  const randomColor = colors[Math.floor(Math.random() * colors.length)];
  document.body.style.backgroundColor = randomColor;
}
