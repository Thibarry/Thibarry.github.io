// Toggle Menu
function toggleMenu() {
  const menu = document.querySelector(".menu-links");
  const icon = document.querySelector(".hamburger-icon");
  menu.classList.toggle("open");
  icon.classList.toggle("open");
}

// Intersection Observer for Fade-in Animations (Magie Disney)
const observerOptions = {
  threshold: 0.2, // Trigger when 20% visible
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
    }
  });
}, observerOptions);

document.querySelectorAll(".fade-in").forEach((el) => {
  observer.observe(el);
});

// Typewriter Effect for Role (Touche IA)
const textElement = document.getElementById("typewriter");
const text = "Frontend Developer";
let index = 0;

function typeWriter() {
  if (index < text.length) {
    textElement.innerHTML += text.charAt(index);
    index++;
    setTimeout(typeWriter, 100); // Speed of typing
  }
}

// Start typing when page loads
window.onload = () => {
  textElement.innerHTML = ""; // Clear initial text
  typeWriter();
};
