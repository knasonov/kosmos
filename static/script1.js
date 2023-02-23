// Get references to all sections
const sections = document.querySelectorAll("section");

// Get reference to the left navbar
const navbar = document.querySelector("nav");

// Add click event listener to the left navbar
navbar.addEventListener("click", (event) => {
  // Check if the clicked element is an anchor tag
  if (event.target.tagName === "A") {
    // Get the id of the section to show
    const sectionId = event.target.getAttribute("href").slice(1);
	//window.alert(sectionId)
  
    // Loop through all sections and hide them
    sections.forEach((section) => {
      section.style.display = "none";
    });
  
    // Show the selected section
    document.getElementById(sectionId).style.display = "block";
  }
});
