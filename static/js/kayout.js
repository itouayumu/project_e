window.onload = function () {
    document.getElementById("gmenuTrigger").addEventListener(
      "click",
      function () {
        document.getElementById("gmenuList").classList.toggle("js-active");
        document.getElementById("gmenuTrigger").classList.toggle("js-active");
      },
      false
    );
  }