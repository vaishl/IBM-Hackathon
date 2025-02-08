var button = document.getElementById("saveButton");
var progressBar = document.getElementById("progress-bar");
          
var saved = 0
var goal = 1000
          
function buttonHover()
{
  button.style.backgroundColor = "#DBDBDB";
}

function buttonReset()
{
  button.style.backgroundColor = "#F0F0F0";
}

function buttonClick()
{
  saved += 50
  percent = (saved/goal) * 100
  document.querySelector(".progress-bar").style.width = percent + "%";
}

button.addEventListener('mouseover', buttonHover);
button.addEventListener('mouseout', buttonReset);
button.addEventListener('click', buttonClick);
