const alertName = () => {
  const inputElValue = document.getElementById("name").value;
  const nameDisplayEl = document.getElementById("name-display");
  nameDisplayEl.innerHTML = "hi, " + inputElValue;
};