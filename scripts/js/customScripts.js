function toggleHiddenProfile() {
    var x = document.getElementById("hiddenProfile");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}

function toggleHiddenSocial() {
  var hiddenLinks = document.getElementById("hiddenSocialLinks");
  var button = document.getElementById("toggleSocialBtn");
  var icon = button.querySelector("i");


  if (hiddenLinks.style.display === "none") {
    icon.classList.remove("fa-caret-down");  // Remove the caret down icon
    icon.classList.add("fa-caret-up");       // Add the caret up icon (Show Less)
    hiddenLinks.style.display = "block";
  } else {
    icon.classList.remove("fa-caret-up");    // Remove the caret up icon
    icon.classList.add("fa-caret-down");     // Add the caret down icon (Show More)
    hiddenLinks.style.display = "none";
  }
}
