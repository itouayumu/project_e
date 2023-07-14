function enableSubmitButton() {
    var checkbox = document.getElementById("confirm");
    var submitButton = document.getElementById("submit");

    if (checkbox.checked) {
      submitButton.disabled = false;
    } else {
      submitButton.disabled = true;
    }
  }