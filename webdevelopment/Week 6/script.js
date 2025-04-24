function checkPass(){
 
    const pass = document.getElementById("agent-password").value;

    if (pass === "1234"){
        document.body.innerHTML = "<h1>Welcome Agent</h1>";
        document.body.style.backgroundColor = "green";
    }else{
        document.getElementById("error").innerHTML = "Access Denied!";
        document.body.innerHTML = "<h1>Access Denied!</h1>";
        document.body.style.backgroundColor = "red";
    }
}

let pressTimer;
document.getElementById("secret-btn").addEventListener("mousedown", () => {
  pressTimer = setTimeout(() => {
    document.getElementById("secret-panel").style.display = "block";
  }, 2000);
});
document.getElementById("secret-btn").addEventListener("mouseup", () => clearTimeout(pressTimer));


let keySequence = "";
document.addEventListener("keydown", (e) => {
  keySequence += e.key.toUpperCase();
  if (keySequence.includes("SAVE")) {
    alert("Memory protocol engaged!");
    keySequence = "";
  }
});


const form = document.getElementById("agent-form");
const nameInput = document.getElementById("name");
const emailInput = document.getElementById("email");
const passwordInput = document.getElementById("password");
const msg = document.getElementById("msg");

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const name = nameInput.value.trim();
  const email = emailInput.value.trim();
  const pass = passwordInput.value;


  if (!name || !email || pass.length < 6) {
    msg.innerText = " Invalid input. Password must be 6+ chars.";
    msg.style.color = "tomato";
  } else {
    msg.innerText = `Welcome, Agent ${name}! Mission loaded.`;
    msg.style.color = "limegreen";

    form.reset();
  }
});
