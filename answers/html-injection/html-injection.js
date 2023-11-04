const displayName = () => {
  const inputElValue = document.getElementById("name").value;
  const nameDisplayEl = document.getElementById("name-display");
  nameDisplayEl.textContent = "hi, " + inputElValue;
};