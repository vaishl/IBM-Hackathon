var button = document.getElementById("saveButton");

function buttonHover()
{
  button.style.backgroundColor = "#DBDBDB";
}

function buttonReset()
{
  button.style.backgroundColor = "#F0F0F0";
}

button.addEventListener('mouseover', buttonHover);
button.addEventListener('mouseout', buttonReset);
